# Hath0r adopt audit — HATH0R-ATC

Date: 2026-09-24 · Issue: #21

| Check | Status | Evidence |
|-------|--------|----------|
| Hidden root `.hath0r/` only | PASS | `.hath0r/` present; no `.ai/` / `.aegis/` / `.infraOS/` |
| Knowledgebase stub | PASS | `.hath0r/knowledgebase/README.md` → group KB |
| `VERSION` SemVer | PASS | root `VERSION` |
| Runbook | PASS | `docs/runbook.md` |
| AGENTS.md | PASS | root `AGENTS.md` (control tower + CLI-first) |
| Tower cfg | PASS | `cfg/control-tower.yaml`, `cfg/suite.yaml`, `cfg/products.yaml` |
| Docker group runtime | PASS | `deploy/docker/` (`hath0r` / `hath0r-net`) |
| Docker group cfg pointer | PASS | `cfg/docker/groups/hath0r/README.md` |
| Suite standards pointer | PASS | `docs/governance/SUITE_STANDARDS.md` |
| OTel stub | PASS | `cfg/observability/otel.json` |
| OpenFeature stub | PASS | `cfg/feature-flags/openfeature.json` |
| MCP priority note | PASS | `cfg/mcp.priority.md` → CLI `cfg/mcp.servers.json` |
| Contracts pin | PASS | `contracts/` + README UPL pin section |
| Secrets policy | PASS | credentials only under Development/.credentials/ (documented) |
| Control tower standards | PASS | Point at `Bayly-AI/HATH0R-CLI` `development` |

## Gaps / follow-ups

- Runtime OTel/OpenFeature **instrumentation** is out of scope for this docs/cfg fan-out; stubs define defaults when ATC surfaces emit telemetry/flags.
- Standalone MCP lifecycle remains `hath0r-mcp` (not ATC compose).
- Ensure CI `SONAR_TOKEN` is org infra (not committed).

## Operator verify

```bash
test -d .hath0r && test -f VERSION && test -f docs/runbook.md
test -f docs/governance/SUITE_STANDARDS.md
test -f cfg/observability/otel.json
test -f deploy/docker/docker-compose.yml
```
