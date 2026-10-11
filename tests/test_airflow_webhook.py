"""Tests for Airflow Webhook Receiver and Docker Compose Stack Configuration in HATH0R-ATC."""

from __future__ import annotations

import hashlib
import hmac
import json
from pathlib import Path
import sys
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.webhook_receiver import AirflowWebhookReceiver



class TestAirflowWebhookReceiver:
    """Test suite for Airflow webhook receiver and docker configuration."""

    def test_verify_signature_valid(self):
        secret = "super-secret-key"
        receiver = AirflowWebhookReceiver(secret=secret)
        payload = b'{"event": "dag_run.success", "dag_id": "elt_pipeline"}'

        sig = hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()
        assert receiver.verify_signature(payload, sig) is True
        assert receiver.verify_signature(payload, f"sha256={sig}") is True

    def test_verify_signature_invalid(self):
        secret = "super-secret-key"
        receiver = AirflowWebhookReceiver(secret=secret)
        payload = b'{"event": "dag_run.success"}'

        assert receiver.verify_signature(payload, "invalid_signature_hex") is False
        assert receiver.verify_signature(payload, None) is False

    def test_process_webhook_success(self):
        secret = "test-secret"
        mock_redis = MagicMock()
        receiver = AirflowWebhookReceiver(secret=secret, redis_client=mock_redis)

        payload_dict = {
            "event": "dag_run.success",
            "dag_id": "elt_daily_sync",
            "state": "success",
            "execution_date": "2026-10-11T12:00:00Z",
        }
        raw_body = json.dumps(payload_dict).encode("utf-8")
        sig = hmac.new(secret.encode("utf-8"), raw_body, hashlib.sha256).hexdigest()

        res = receiver.process_webhook(raw_body, signature=sig)
        assert res["status"] == "accepted"
        assert res["status_code"] == 200
        assert res["dag_id"] == "elt_daily_sync"
        assert res["redis_dispatched"] is True
        mock_redis.publish.assert_called_once()

        stats = receiver.get_stats()
        assert stats["processed_count"] == 1
        assert stats["rejected_count"] == 0

    def test_process_webhook_unauthorized(self):
        receiver = AirflowWebhookReceiver(secret="correct-secret")
        res = receiver.process_webhook(b'{"test": 1}', signature="wrong-sig")
        assert res["status"] == "rejected"
        assert res["status_code"] == 401

    def test_process_webhook_malformed_json(self):
        secret = "secret"
        receiver = AirflowWebhookReceiver(secret=secret)
        raw_body = b"not-valid-json{"
        sig = hmac.new(secret.encode("utf-8"), raw_body, hashlib.sha256).hexdigest()

        res = receiver.process_webhook(raw_body, signature=sig)
        assert res["status"] == "rejected"
        assert res["status_code"] == 400

    def test_docker_compose_airflow_service(self):
        compose_path = Path(__file__).parent.parent / "deploy" / "docker" / "docker-compose.yml"
        assert compose_path.is_file()
        content = compose_path.read_text(encoding="utf-8")
        assert "container_name: Hath0r-Airflow" in content
        assert "profiles: [\"airflow\"]" in content
        assert "hath0r_airflow_data" in content

    def test_nginx_airflow_proxy_route(self):
        nginx_conf_path = Path(__file__).parent.parent / "deploy" / "docker" / "nginx" / "conf.d" / "default.conf"
        assert nginx_conf_path.is_file()
        content = nginx_conf_path.read_text(encoding="utf-8")
        assert "location /airflow/ {" in content
        assert "proxy_pass http://Hath0r-Airflow:8080/;" in content
