"""Entry point for HATH0R ATC service and Airflow Webhook Server."""

from __future__ import annotations

import http.server
import json
import logging
import os
import sys

from lib.webhook_receiver import AirflowWebhookReceiver

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("hath0r_atc")

receiver = AirflowWebhookReceiver()


class ATCHTTPServer(http.server.BaseHTTPRequestHandler):
    """HTTP request handler for ATC health and webhook ingestion."""

    def do_GET(self) -> None:
        if self.path in ("/health", "/healthz", "/"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            payload = {"status": "healthy", "service": "hath0r-atc", "stats": receiver.get_stats()}
            self.wfile.write(json.dumps(payload).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self) -> None:
        if self.path in ("/webhook/airflow", "/api/v1/airflow/webhook"):
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            sig = self.headers.get("X-Airflow-Signature") or self.headers.get("X-Hub-Signature-256")
            res = receiver.process_webhook(body, signature=sig)

            self.send_response(res.get("status_code", 200))
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(res).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format: str, *args) -> None:
        logger.info("%s - - [%s] %s", self.client_address[0], self.log_date_time_string(), format % args)


def main() -> None:
    port = int(os.getenv("PORT", os.getenv("ATC_PORT", "8000")))
    server_address = ("0.0.0.0", port)
    httpd = http.server.HTTPServer(server_address, ATCHTTPServer)
    logger.info("Starting HATH0R ATC Webhook Server on port %d...", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Stopping HATH0R ATC Webhook Server.")
        httpd.server_close()


if __name__ == "__main__":
    main()
