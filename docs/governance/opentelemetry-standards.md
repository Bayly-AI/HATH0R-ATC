# OpenTelemetry standards (ATC pointer)

Canonical: [HATH0R-CLI opentelemetry-standards.md](https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/opentelemetry-standards.md).

Local stub: [`../../cfg/observability/otel.json`](../../cfg/observability/otel.json) — `service.name=hath0r-atc`, namespace `hath0r-opensource`.

Required resource attributes follow the control tower: `service.name`, `service.namespace`, `deployment.environment`, `service.version` (from `VERSION` when instrumented).

Secrets / OTLP headers: credentials root only — never commit.

Issue: #13
