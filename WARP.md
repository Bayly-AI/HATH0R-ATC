# WARP.md — HATH0R ATC / OpenSource Project policy

> Group: `hath0r-opensource`  
> Infrastructure control tower: `HATH0R-ATC` (`Bayly-AI/HATH0R-ATC`)  
> Operator CLI: `HATH0R-CLI` (`Bayly-AI/HATH0R-CLI`) · binary `hath0r`  
> Updated: 2026-09-23

## Purpose

Agent and operator policy for the **OpenSource Project**: every canonical repo under `/Users/raybayly/Development/OpenSource`.

## Control surfaces

| Surface | Product | Path | Role |
|---------|---------|------|------|
| Infrastructure / observation / Docker group | **HATH0R-ATC** | `OpenSource/hath0r-atc` | Control tower |
| Operator CLI | HATH0R-CLI | `OpenSource/hathor-cli` | `hath0r` binary + packaging |
| Standalone MCP | HATH0R-MCP | `OpenSource/hath0r-mcp` | MCP member on `hath0r-net` |
| Framework | HATHOR Framework | `OpenSource/hath0r` | App framework + docs corpus |

Members point Docker-group / observation questions at **ATC**. Use **`hath0r`** CLI for doctor/path helpers when installed.

## Membership

- **In scope**: all sibling git repositories under the OpenSource folder.
- **Registry**: ATC `cfg/products.yaml` (and CLI catalog until fully migrated).
- New sibling repos join by default and should add member `AGENTS.md` + stub KB pointer.

## Knowledge & docs

| Surface | Path | Role |
|---------|------|------|
| Group KB hub | `OpenSource/.hath0r/knowledgebase` | Canonical local knowledge |
| Member KB | `<repo>/.hath0r/knowledgebase` | Stub/pointer only |
| Docs corpus | `OpenSource/hath0r/docs` | Canonical documentation |
| Tower configs | `OpenSource/hath0r-atc/cfg/*` | Suite infra governance |
| ATC runbook | `hath0r-atc/docs/runbook.md` | Ops path |

## Hidden root

Only `.hath0r/`. Forbidden: `.ai/`, `.customerSystem/`, `.infraOS/`.

## Docker group (CR-DOCKER-HATH0R-GROUP-001)

```text
compose name: hath0r
network: hath0r-net
edge/state: hath0r-nginx / hath0r-redis
```

## Branch protection & promotion (CR-BAI-001 / cr-branch-gov-001)

```text
local → development → testing → staging → master (Production)
```

- Issue before branch
- Feature work merges to `development` only
- Stage PRs: `development→testing`, `testing→staging`, `staging→master`
- No force-push/deletes on canonical branches; code owner review required

## Secrets

Never commit secrets. Use `/Users/raybayly/Development/.credentials/<service>/.env`.

## CR-HATH0R-INIT-001

1. Setup playbook — `hathor-cli/docs/hathor-playbook-001-repo-init-setup-20260919.md` (or framework mirror when present)
2. Same-technology runbook — e.g. ATC `docs/runbook.md`
3. Then layout / `.hath0r/` / `cfg/` / bootstrap

---

## CR-TASK-EVAL-001 (Automatic Task Evaluation Before Announcing Complete — CRITICAL · CANONICAL)
- **Mandatory Pre-Announcement Task Evaluation Gate**: Every task MUST be evaluated across the 4-tier hybrid evaluation pipeline (Tier 1 Deterministic Rubrics, Tier 2 Trajectory & FinOps Efficiency, Tier 3 Adversarial & Diff Critics, Tier 4 Goal Alignment & Consensus) prior to announcing work as Complete.
- **Composite Reward Threshold**: Task completion requires `passed_gate: true` and composite reward score `R_task >= 0.80` persisted in `.hath0r/evals/latest.json` and compounded as an `eval:<task_id>` node in `.hath0r/memory/graph.json`.
- **How to Verify**: Run `hath0r evals run` and `hath0r evals verify` before announcing Complete (`EndOfTaskBot`, `TaskAnnouncerBot.announce_complete`, and `CleanReposWorkflowBot` enforce this gate automatically).
- **Not Complete Until Evaluated**: A missing, failing, or unverified task evaluation means the work is not Complete.
