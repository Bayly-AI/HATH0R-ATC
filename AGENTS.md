# AGENTS.md — HATH0R ATC (Control Tower)

> **Canonical control tower** for the **OpenSource Project** (`hath0r-opensource`).  
> Roles: **infrastructure repo** · **observation hub** · **central group controller**.  
> ATC and MCP are **standalone**; both support building the HATHOR framework.

| Field | Value |
|-------|-------|
| Product | **HATH0R ATC** |
| Product ID | `hath0r-atc` |
| Role | Control Tower — infrastructure / observation / group controller (`is_control_tower: true`) |
| GitHub | **[Bayly-AI/HATH0R-ATC](https://github.com/Bayly-AI/HATH0R-ATC)** (CANONICAL) |
| Local path | `/Users/raybayly/Development/OpenSource/hath0r-atc` |
| Group | `hath0r-opensource` / **OpenSource Project** |
| Docker group | **`hath0r`** (CANONICAL) |
| Docker network | **`hath0r-net`** (CANONICAL) |
| Shared edge / state | `hath0r-nginx` / `hath0r-redis` / `Hathor-MLFLOW` |
| Members root | `/Users/raybayly/Development/OpenSource` |
| Operator CLI | **`hath0r`** (`../hathor-cli`) |
| Standalone MCP | `../hath0r-mcp` (`hath0r-mcp` container) |
| Framework | `../hath0r` |
| Tech runbook | [`docs/runbook.md`](docs/runbook.md) |
| Setup playbook | `../hathor-cli/docs/hathor-playbook-001-repo-init-setup-20260919.md` |
| Local Memory Space | [`.hath0r/memory/`](.hath0r/memory/) (`hath0r memory read <topic>`) |
| Tri-Graph Substrate | KnowledgeGraph AST · ContextGraph Subsystems · MemoryGraph |

## CR-CLI-ENTRY-001: Start with the CLI (CRITICAL — Org-Wide · CANONICAL)

1. **Start with the CLI (CRITICAL ENTRY GATE)**: When receiving ANY request or starting any task, agents **MUST ALWAYS START WITH THE OPERATOR CLI (`hath0r`)** rather than inventing ad-hoc scripts. Check `hath0r --help` and the matching `hath0r <group> --help` first.
2. **Missing Capability Offer**: If the required connection, MCP, workflow, bot, or factory does not exist in `hath0r`, offer to register the missing capability, using the original request as the acceptance test.
3. **Docs before code**: Require procedure/playbook/runbook before scaffolding implementation.

Canonical: [HATH0R-CLI `docs/governance/cli-first-rules.md`](https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/cli-first-rules.md).

## ATC responsibilities (CRITICAL)

This repository is the **infrastructure control tower** for OpenSource. It owns:

1. **Infrastructure** — canonical local Docker group, compose, NGINX edge, Redis state, Postgres volume policy, suite networks/labels (`deploy/docker/`, `CR-DOCKER-HATH0R-GROUP-001`).
2. **Observation** — suite health, smoke baselines, status surfaces, and operational archives under `docs/observe/` / `docs/archive/`.
3. **Central group controller** — suite identity (`cfg/suite.yaml`), tower config (`cfg/control-tower.yaml`), membership policy for **all** repos under this workspace.

**MCP is standalone** — process lifecycle lives in `hath0r-mcp`. It joins `hath0r-net` / project `hath0r` but is not started/stopped by ATC compose.

**HATH0R-CLI** remains the operator/developer CLI (`hath0r` binary). ATC does not replace the CLI package; it owns Docker-group and observation control.

Member product remotes stay independent. **Docker group membership and suite infra policy always resolve here.**

## CR-DOCKER-HATH0R-GROUP-001 — Docker group membership (CRITICAL · CANONICAL)

**All repositories and deployable services under OpenSource are members of the `hath0r` Docker group.**

| Requirement | Canonical value |
|-------------|-----------------|
| Compose top-level `name:` | `hath0r` |
| Network | external `hath0r-net` |
| Image prefix | `hath0r/{component}:tag` |
| Labels | `com.hath0r.org=bayly-ai`, `com.hath0r.project=hath0r-opensource`, `com.hath0r.component`, `com.hath0r.container` |
| Shared edge / state | Prefer `hath0r-nginx` + `hath0r-redis` from ATC `deploy/docker` |

Policy: [`docs/rules/cr-docker-hath0r-group-001.md`](docs/rules/cr-docker-hath0r-group-001.md)  
Deploy: [`docs/deployment-local-docker.md`](docs/deployment-local-docker.md)

### Operator entry

```sh
cd /Users/raybayly/Development/OpenSource/hath0r-atc
make docker-up
make docker-status
make smoke
# optional standalone MCP
make -C ../hath0r-mcp docker-up
```

## Orientation

1. **This ATC wins** for suite Docker group policy, infrastructure, and observation.
2. Nearest product `AGENTS.md` wins for product identity only.
3. Secrets stay out of git — `/Users/raybayly/Development/.credentials/`.
4. Tower configs: `cfg/control-tower.yaml`, `cfg/suite.yaml`, `cfg/products.yaml`.
5. Hidden root: **`.hath0r/` only** (`cr-hath0r-root-001`).
6. **CR-CLI-FEATURE-STANDARD-001 (Shared Code in CLI & Artifact Hexad — CRITICAL · CANONICAL)**:
   - **Zero Code Duplication**: Anything usable across multiple repos MUST live in `HATH0R-CLI`.
   - **Complete Feature Package**: When adding any feature that should be a CLI command, deliver the CLI commands (`src/hath0r_cli/commands/`), managing bot(s) (`src/hath0r_cli/bots/`), workflows/scripts, and the Governance Documentation Hexad (Strategy, Procedure, Playbook, Runbook, Workflow, Bot Spec).
   - **Configuration-Only Member Repos**: Member repositories only contain declarative configuration files (`cfg/`, `otel.json`, factory YAMLs) that configure and bind to the CLI's tools.

## Branch & PR targets (CRITICAL — CR-BRANCH-GOV-001)

```text
feature/* → development → testing → staging → master
```

- Day-to-day PRs **base = `development`** only.
- Rule: [`docs/rules/cr-branch-gov-001-canonical-branches.md`](docs/rules/cr-branch-gov-001-canonical-branches.md)
- CI: `.github/workflows/enforce-promotion-path.yml`

## CR-HATH0R-INIT-001

Before initializing repos with Hath0r:

1. Follow setup playbook: `../hathor-cli/docs/hathor-playbook-001-repo-init-setup-20260919.md`
2. Ensure same-tech runbook exists (this repo: [`docs/runbook.md`](docs/runbook.md))
3. Then apply layout / `.hath0r/` / `cfg/` / bootstrap

## CR-SEMVER-BUMP-001 (Semantic Version Bump on Every PR — CANONICAL)
- Every pull request that is created and merged must create or bump this product's Semantic Version (`MAJOR.MINOR.PATCH`, https://semver.org). The root `VERSION` file is the source of truth; keep `VERSION` and `CHANGELOG.md` in step with it.
- Pick the bump by impact: MAJOR for breaking changes, MINOR for backward-compatible features, PATCH for fixes, docs, chores and everything else. `Version Impact: none` is not allowed.
- New products start at `0.1.0`.
- Declare the bump in the PR body as `Version Impact: patch|minor|major` and add a matching `CHANGELOG.md` entry. Verify with `hath0r release validate` before announcing complete.
- A PR merged without a version bump is not Complete.

## Peer reference

Structure and ops patterns mirror **1-Nation ATC** at `/Users/raybayly/Development/1-Nation/ATC` with Hath0r naming (`hath0r` / `hath0r-net` / `com.hath0r.*` / ports `38xxx`).

## Branch rules (pointer)

See `docs/governance/branch-rules.md` (cr-branch-gov-001 / CR-BAI-001). Work PRs → `development` only; release trains use `release/x.x.x`.
## PR workflow hardening

See `docs/governance/pr-workflow.md`. Work PRs → `development` (agents + CODEOWNERS). **Human gate** before staging/master.
## SonarCloud Quality Gate (CRITICAL)

- Canonical thresholds: SonarCloud Quality Gate only — do not modify gate thresholds ad hoc.
- PR check **SonarCloud Quality Gate** is a hard stop on failure.
- See `docs/governance/sonarcloud-quality-gates.md`
- Secret required: `SONAR_TOKEN`
## Documentation → MCP

Docs are published to the **proper group MCP** via control-tower
`python3 scripts/publish-docs-to-mcp.py` (`cfg/mcp-doc-publish.json`).
See HATH0R-CLI `docs/governance/mcp-doc-publish.md`.

## CLI-first (CRITICAL — cr-cli-first-001)

For connections, MCP, workflows, factories, Docker workflows, KB path, or suite orientation:

1. Prefer the operator CLI **`hath0r`** (`../hathor-cli`) when installed.
2. Prefer ATC Make targets for Docker group lifecycle (`make docker-up`, `make smoke`).
3. Do not invent parallel ad-hoc scripts that bypass CLI/ATC entrypoints.

Canonical: [HATH0R-CLI cli-first-rules.md](https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/cli-first-rules.md)  
Local pointer: [`docs/governance/cli-first-rules.md`](docs/governance/cli-first-rules.md)

## Suite standards fan-out

Shared epics (OTel, OpenFeature, OpenObservation, SemVer, Docker group templates, workflow docs, MCP priority) are defined in **HATH0R-CLI** on `development`. ATC pins them via:

- [`docs/governance/SUITE_STANDARDS.md`](docs/governance/SUITE_STANDARDS.md)
- Stubs: `cfg/observability/otel.json`, `cfg/feature-flags/openfeature.json`
- Docker runtime: `deploy/docker/` · template pointer: `cfg/docker/groups/hath0r/`
- MCP priority: [`cfg/mcp.priority.md`](cfg/mcp.priority.md) → CLI `cfg/mcp.servers.json` (project MCP = priority 1)
- Adopt audit: [`.hath0r/ADOPT_AUDIT.md`](.hath0r/ADOPT_AUDIT.md)

## Hyper Context Pointers (ContextGraph)

- **Deploy Subsystem**: [`deploy/AGENTS.md`](deploy/AGENTS.md)
- **Contracts Subsystem**: [`contracts/AGENTS.md`](contracts/AGENTS.md)
- **Tests Subsystem**: [`tests/AGENTS.md`](tests/AGENTS.md)
- **Docs Subsystem**: [`docs/AGENTS.md`](docs/AGENTS.md)
- **Cfg Subsystem**: [`cfg/AGENTS.md`](cfg/AGENTS.md)
- **Lib Subsystem**: [`lib/AGENTS.md`](lib/AGENTS.md)
- **Site Subsystem**: [`site/AGENTS.md`](site/AGENTS.md)

## AgentGraph Substrate

This repository is governed by the Hath0r AgentGraph substrate. Dynamic rule retrieval, role RBAC, and policy graphs are stored under `.hath0r/agentgraph/`.
- Query status: `hath0r agentgraph status`
- Query rules: `hath0r agentgraph query "<topic>"`
- Route role: `hath0r agentgraph route --role <role>`
- Validate rules: `hath0r agentgraph validate`

---

## CR-SONAR-PREANNOUNCE-001 (SonarCloud Thresholds Before Announcing Complete — CANONICAL)
- **Pre-Announcement SonarCloud Gate**: Before announcing any work as Complete, the agent MUST analyze the code and confirm it meets this repository's SonarCloud Quality Gate thresholds (coverage on new code, duplication, reliability, security, maintainability, and security hotspots reviewed).
- **How to Verify**: Use `hath0r quality sonar` (project key from `sonar-project.properties`) together with local test and coverage runs. If the gate cannot be checked, state that plainly instead of announcing Complete.
- **Not Complete Until Green**: A failing or unverified Quality Gate means the work is not Complete.

---

## CR-TASK-EVAL-001 (Automatic Task Evaluation Before Announcing Complete — CRITICAL · CANONICAL)
- **Mandatory Pre-Announcement Task Evaluation Gate**: Every task MUST be evaluated across the 4-tier hybrid evaluation pipeline (Tier 1 Deterministic Rubrics, Tier 2 Trajectory & FinOps Efficiency, Tier 3 Adversarial & Diff Critics, Tier 4 Goal Alignment & Consensus) prior to announcing work as Complete.
- **Composite Reward Threshold**: Task completion requires `passed_gate: true` and composite reward score `R_task >= 0.80` persisted in `.hath0r/evals/latest.json` and compounded as an `eval:<task_id>` node in `.hath0r/memory/graph.json`.
- **How to Verify**: Run `hath0r evals run` and `hath0r evals verify` before announcing Complete (`EndOfTaskBot`, `TaskAnnouncerBot.announce_complete`, and `CleanReposWorkflowBot` enforce this gate automatically).
- **Mandatory Eval Scorecard Summary After Every Task (CRITICAL · CANONICAL)**: Immediately after running task evaluations (`hath0r evals run`), the agent MUST always return a structured summary of the **Eval Scorecard** (`eval_id`, `task_id`, `passed_gate`, composite `R_task`, Tier 1–4 scores, and `.hath0r/evals/latest.json` path) in its completion response to the user.
- **Not Complete Until Evaluated & Scorecard Returned**: A missing, failing, unverified, or unreported task evaluation scorecard means the work is not Complete.
