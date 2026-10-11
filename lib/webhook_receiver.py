"""Airflow Webhook Receiver and Event Dispatcher for HATH0R-ATC."""

from __future__ import annotations

import hashlib
import hmac
import json
import logging
import os
import time
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger("hath0r_atc.webhook_receiver")


class AirflowWebhookReceiver:
    """Validates and processes incoming HTTP webhooks from Apache Airflow.

    Provides HMAC-SHA256 signature verification, event classification,
    and dispatch to Redis pub/sub or event queues.
    """

    def __init__(
        self,
        secret: Optional[str] = None,
        redis_client: Optional[Any] = None,
        event_channel: str = "hath0r:events:airflow",
    ) -> None:
        self.secret = secret or os.getenv("AIRFLOW_WEBHOOK_SECRET", "hath0r-dev-webhook-secret")
        self.redis_client = redis_client
        self.event_channel = event_channel
        self.processed_count = 0
        self.rejected_count = 0
        self.events_history: List[Dict[str, Any]] = []

    def verify_signature(self, payload_bytes: bytes, signature_header: Optional[str]) -> bool:
        """Verify HMAC-SHA256 signature from the incoming request header."""
        if not signature_header:
            return False

        # Support 'sha256=...' prefix or raw hex
        expected_prefix = "sha256="
        clean_sig = signature_header[len(expected_prefix):] if signature_header.startswith(expected_prefix) else signature_header

        computed = hmac.new(
            self.secret.encode("utf-8"),
            msg=payload_bytes,
            digestmod=hashlib.sha256,
        ).hexdigest()

        return hmac.compare_digest(computed.lower(), clean_sig.lower())

    def process_webhook(
        self,
        raw_body: bytes,
        signature: Optional[str] = None,
        skip_auth: bool = False,
    ) -> Dict[str, Any]:
        """Validate and dispatch an incoming webhook."""
        if not skip_auth and not self.verify_signature(raw_body, signature):
            self.rejected_count += 1
            return {
                "status": "rejected",
                "reason": "Invalid or missing HMAC signature",
                "status_code": 401,
            }

        try:
            payload = json.loads(raw_body.decode("utf-8"))
        except Exception as e:
            self.rejected_count += 1
            return {
                "status": "rejected",
                "reason": f"Malformed JSON: {str(e)}",
                "status_code": 400,
            }

        event_type = payload.get("event", payload.get("event_type", "dag_run.unknown"))
        dag_id = payload.get("dag_id", "unknown_dag")
        state = payload.get("state", payload.get("status", "unknown"))

        envelope = {
            "schema_version": "hath0r.atc.webhook_event/1",
            "received_at": time.time(),
            "event_type": event_type,
            "dag_id": dag_id,
            "state": state,
            "data": payload,
        }

        self.processed_count += 1
        self.events_history.append(envelope)
        if len(self.events_history) > 100:
            self.events_history.pop(0)

        # Dispatch to Redis if client provided
        redis_dispatched = False
        if self.redis_client is not None:
            try:
                self.redis_client.publish(self.event_channel, json.dumps(envelope))
                redis_dispatched = True
            except Exception as e:
                logger.warning(f"Failed to publish webhook to Redis: {e}")

        return {
            "status": "accepted",
            "event_type": event_type,
            "dag_id": dag_id,
            "redis_dispatched": redis_dispatched,
            "status_code": 200,
        }

    def get_stats(self) -> Dict[str, Any]:
        """Return operational stats for ATC health checks."""
        return {
            "status": "healthy",
            "processed_count": self.processed_count,
            "rejected_count": self.rejected_count,
            "recent_events_count": len(self.events_history),
        }
