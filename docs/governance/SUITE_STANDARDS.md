# Suite standards (HATH0R-ATC member pointer)

> **Role:** HATH0R-ATC is the OpenSource **infrastructure / observation / Docker-group control tower**.  
> **Canonical policy prose and shared cfg templates** for suite-wide epics live in the operator control tower **HATH0R-CLI** (`Bayly-AI/HATH0R-CLI`, branch `development`).  
> This document pins ATC to those standards and lists local stubs.

Updated: 2026-09-24 · Fan-out issues: #11–#16, #8–#10, #2, #21

## Control tower (canonical)

| Surface | GitHub (`development`) |
|---------|-------------------------|
| Repo | https://github.com/Bayly-AI/HATH0R-CLI |
| OTel standards | https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/opentelemetry-standards.md |
| OTel cfg | https://github.com/Bayly-AI/HATH0R-CLI/blob/development/cfg/observability/otel.json |
| OpenFeature standards | https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/openfeature-standards.md |
| OpenFeature cfg | https://github.com/Bayly-AI/HATH0R-CLI/blob/development/cfg/feature-flags/openfeature.json |
| OpenObservation | https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/openobservation-standards.md |
| CLI-first | https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/cli-first-rules.md |
| Workflow docs | https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/workflow-documentation-standard.md |
| Docker group standard | https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/docker-group-standard.md |
| Docker group template (`hath0r`) | https://github.com/Bayly-AI/HATH0R-CLI/tree/development/cfg/docker/groups/hath0r |
| SemVer | https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/semantic-versioning.md |
| MCP configuration | https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/mcp-configuration.md |
| Project MCP servers (priority 1) | https://github.com/Bayly-AI/HATH0R-CLI/blob/development/cfg/mcp.servers.json |

Local CLI checkout (operators): `/Users/raybayly/Development/OpenSource/hathor-cli` (or `HATH0R-CLI`).

## ATC local stubs / ownership

| Topic | ATC path | Notes |
|-------|----------|-------|
| OTel | [`cfg/observability/otel.json`](../../cfg/observability/otel.json) | `service.name=hath0r-atc` |
| OpenFeature | [`cfg/feature-flags/openfeature.json`](../../cfg/feature-flags/openfeature.json) | product `HATH0R-ATC` |
| Docker group (runtime) | [`deploy/docker/`](../../deploy/docker/) | **Canonical runtime** compose for `hath0r` / `hath0r-net` |
| Docker group (template pointer) | [`cfg/docker/groups/hath0r/`](../../cfg/docker/groups/hath0r/) | Points at CLI template + ATC deploy |
| Observation hub | [`docs/observe/`](../observe/) | Suite health / smoke surfaces |
| Contracts (UPL pin) | [`contracts/`](../../contracts/) | Pin refresh notes in README |
| Hidden root | [`.hath0r/`](../../.hath0r/) | Only allowed agent root |
| Adopt audit | [`.hath0r/ADOPT_AUDIT.md`](../../.hath0r/ADOPT_AUDIT.md) | Framework adopt checklist |
| SemVer pointer | [`semantic-versioning.md`](semantic-versioning.md) | `VERSION` is canonical |
| Workflow docs pointer | [`workflow-documentation-standard.md`](workflow-documentation-standard.md) | Procedure/strategy/playbook |
| MCP priority | [`cfg/mcp.priority.md`](../../cfg/mcp.priority.md) | Project MCP before group/org |

## Non-negotiables (suite)

1. **Hidden root:** `.hath0r/` only — never `.ai/`, `.customerSystem/`, `.infraOS/`.
2. **Secrets:** only under `/Users/raybayly/Development/.credentials/<service>/.env` — never commit.
3. **Branches:** feature work → PR base **`development`** only (`CR-BRANCH-GOV-001`).
4. **Docker group:** compose `name: hath0r`, network `hath0r-net`, shared edge/state via ATC deploy.
5. **CLI-first:** prefer `hath0r` for doctor/path/MCP/docker workflow/factory orientation before ad-hoc scripts.
6. **Issue-first:** open GitHub issue before branch; branch `feature|<type>/<issue>-slug`.

## Related ATC docs

- [`branch-rules.md`](branch-rules.md)
- [`pr-workflow.md`](pr-workflow.md)
- [`../runbook.md`](../runbook.md)
- [`../deployment-local-docker.md`](../deployment-local-docker.md)
- [`../rules/cr-docker-hath0r-group-001.md`](../rules/cr-docker-hath0r-group-001.md)
