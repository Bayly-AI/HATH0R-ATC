# Observation (Hath0r ATC)

**Hath0r ATC** is the OpenSource Project **observation** hub as well as infrastructure and group controller.

## Current surfaces

| Surface | Path / command |
|---------|----------------|
| Docker group status | `make docker-status` |
| Smoke (edge + Redis + optional MCP) | `make smoke` / `./deploy/docker/smoke-test.sh` |
| SPC status panel (R_task, tiers, cost, latency; Cpk) | `make observe-spc` · [`spc-panel.md`](spc-panel.md) |
| Reports | `docs/reports/` |
| Runtime archive | `docs/archive/` |

## Direction

Expand toward fuller Observe capabilities while keeping **status and smoke ownership in ATC** so the control tower remains the single place operators check suite health for framework builds.
