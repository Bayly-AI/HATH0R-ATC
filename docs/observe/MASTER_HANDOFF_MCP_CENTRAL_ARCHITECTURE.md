# Master Hand-Off: Hath0r MCP-Central Architecture, Two-Level `AgentGraph`, Workflow-First & Continuous Evals

> **Document ID**: `MASTER-HANDOFF-MCP-ARCH-20261031`  
> **Control Tower**: `Bayly-AI/HATH0R-ATC` (`/Users/raybayly/Development/OpenSource/hath0r-atc`)  
> **Canonical Roadmap**: [`docs/observe/mcp-central-architecture-roadmap-20261031.md`](mcp-central-architecture-roadmap-20261031.md)  
> **Last Updated**: 2026-10-31 (After Completing Ticket #2 `Bayly-AI/HATH0R-MCP#86` → [PR #88](https://github.com/Bayly-AI/HATH0R-MCP/pull/88), Ticket #1 `Bayly-AI/HATH0R-MCP#85` → [PR #87](https://github.com/Bayly-AI/HATH0R-MCP/pull/87), & Ticket #9 `Bayly-AI/HATH0R-ATC#80` → [PR #81](https://github.com/Bayly-AI/HATH0R-ATC/pull/81))  
> **Mandatory Rule for All Subsequent Sessions**: **After completing EVERY ticket, you MUST update this Master Hand-Off document (`docs/observe/MASTER_HANDOFF_MCP_CENTRAL_ARCHITECTURE.md`) with the ticket's status, branch/PR URL, test results, and Continuous 4-Tier Eval Scorecard (`R_task`), commit, and push before handing off to the next session.**

---

## 1. Non-Negotiable Architectural Invariants (Read Before Starting Any Ticket)

1. **Canonical Feature Definition (`CR-FEATURE-WORKFLOW-STANDARD-001`)**:
   - **Every Feature Is a Service Run by `>= 1` Bot**: Every feature, CLI command, MCP tool, or workflow MUST be backed by a formal Service and owned by at least one registered Bot in `BotRegistry` (`src/hath0r_cli/factories/step_runner.py`).
   - **Two-Level Topology on `AgentGraph`**:
     - **Level 1 (`HATH0R-MCP` — `Priority 1`)**: Central suite tools, declarative workflows, factories, and canonical knowledge reside on **`HATH0R-MCP`** (`http://127.0.0.1:38083` / `http://localhost:38000/mcp/`), indexed and governed by **`AgentGraph`**.
     - **Level 2 (`HATH0R-CLI` & Bot Memory)**: Operator CLI execution (`hath0r`) and Bot Memory (`.hath0r/memory/graph.json`, micro-sessions) reside at **Level 2**, synchronized with Level 1 via **`AgentGraph`** (`.hath0r/agentgraph/snapshot.json`).
   - **Workflow-First Standard ("Everything We Do Is a Workflow")**: Every task executes as a declarative workflow (`cfg/factories/*.yaml` or `mcp_workflow_*`). If a workflow does not exist for a task, halt ad-hoc execution and **offer to create and register the workflow first** (`hath0r workflow offer` / `mcp_workflow_scaffold`) using the original request as its acceptance test.
2. **4-Hour Automated Pre-Task Calibration (`max_age_hours = 4.0`)**:
   - Prior to starting any task, check `hath0r cccd status` (`.hath0r/cccd_state.json`, `ttl_hours: 4.0`). If calibration is `> 4.0` hours old, automatically run `hath0r cccd calibrate` (`ensure_calibrated(max_age_hours=4.0)`).
3. **4-Stage Iteration Cascade & `SuperSqueeze`**:
   - Strictly follow `Stage 1: Task (Workflow-First + 4h Calibration + Cruise Control) → Stage 2: Hath0r-CLI (Level 2) ⇄ Hath0r-MCP (Level 1) on AgentGraph + SuperSqueeze → Stage 3: Computer → Stage 4: Web`.
4. **OpenFeature, OpenObserve (`OpenObservation`), OpenTelemetry (`OTel`) & `hath0r-net`**:
   - Export OTel/OpenInference traces to **`Hath0r-phoenix`** (`http://localhost:38000/phoenix` / `http://Hath0r-phoenix:6006`), log evals & calibration runs to **`Hathor-MLFLOW`** (`http://localhost:38000/mlflow/` / `http://Hathor-MLFLOW:5000`), and sync work boundaries & settled facts with **`Hath0r-Cruise-Control`** (`http://localhost:38000/cruise/radar` / `http://Hath0r-Cruise-Control:8090`).
5. **Continuous, Non-Binary 4-Tier Task Evaluations (`CR-TASK-EVAL-001`)**:
   - Every ticket MUST run `pytest -q` and `hath0r evals run --task-id "issue-<N>"` + `hath0r evals verify`, producing a real continuous score (`0.80 <= R_task < 1.00`, never a hardcoded binary `1.0000`) via upgraded `TaskEvaluatorBot`, and return the structured **Eval Scorecard Summary**.

---

## 2. Master Ticket Tracker (Update After Every Ticket)

| Order | Repo | Ticket | Title | Status | Branch & PR | Tests | Continuous Eval (`R_task`) |
|---|---|---|---|---|---|---|---|
| **1** | `Bayly-AI/HATH0R-MCP` | [#85](https://github.com/Bayly-AI/HATH0R-MCP/issues/85) | `feat(mcp): centralize Level 1 suite tools & knowledge on AgentGraph, SuperSqueeze middleware, and OTel/OpenObserve/OpenFeature in HATH0R-MCP` | **COMPLETED (PR Open)** | `feature/85-centralize-l1-suite-tools-supersqueeze` ([PR #87](https://github.com/Bayly-AI/HATH0R-MCP/pull/87)) | `610 passed, 1 skipped` | **`0.9335`** (`eval-20261031-111203-55dc85`) |
| **2** | `Bayly-AI/HATH0R-MCP` | [#86](https://github.com/Bayly-AI/HATH0R-MCP/issues/86) | `feat(mcp): expose Workflow-First engine, missing-workflow offer, BotRegistry dispatch, Level 1/2 AgentGraph & MemoryGraph sync, 4h calibration, and Phoenix/MLflow/Cruise Control tools in HATH0R-MCP` | **COMPLETED (PR Open)** | `feature/86-workflow-first-engine-cruise-mlflow-phoenix` ([PR #88](https://github.com/Bayly-AI/HATH0R-MCP/pull/88)) | `617 passed, 1 skipped` | **`0.9374`** (`eval-20261031-113824-c66d32`) |
| **3** | `Bayly-AI/HATH0R-CLI` | [#551](https://github.com/Bayly-AI/HATH0R-CLI/issues/551) | `feat(bots): register all 69 bots as feature service owners in BotRegistry, enforce 4-hour pre-task auto-calibration, and wire SuperSqueeze across Level 1/2 AgentGraph` | **NEXT UP (Ready)** | `feature/551-register-69-bots-4h-calibration-supersqueeze` | — | — |
| **4** | `Bayly-AI/HATH0R-CLI` | [#552](https://github.com/Bayly-AI/HATH0R-CLI/issues/552) | `feat(mcp): implement MCPCentralizationBot & MCPWorkflowEngineBot, enforce Workflow-First missing-workflow offer, and bridge Level 1 (HATH0R-MCP) & Level 2 (HATH0R-CLI/Memory) on AgentGraph` | **QUEUED** | `feature/552-mcp-centralization-workflow-engine-bots` | — | — |
| **5** | `Bayly-AI/HATH0R-CLI` | [#553](https://github.com/Bayly-AI/HATH0R-CLI/issues/553) | `feat(bots): implement IterationCascadeBot to enforce Workflow-First Stage 1 (Task + 4h Calibration) -> Stage 2 (Level 1 MCP + Level 2 CLI/Memory on AgentGraph) -> Stage 3 (Computer) -> Stage 4 (Web)` | **QUEUED** | `feature/553-iteration-cascade-bot` | — | — |
| **6** | `Bayly-AI/HATH0R-CLI` | [#554](https://github.com/Bayly-AI/HATH0R-CLI/issues/554) | `feat(bots): implement ArchitecturePreservationBot, SubstrateUtilizationBot & TaskCompletionVerifierBot to enforce CR-FEATURE-WORKFLOW-STANDARD-001 across all 5 repos` | **QUEUED** | `feature/554-arch-preservation-substrate-verifier-bots` | — | — |
| **7** | `Bayly-AI/HATH0R-CLI` | [#555](https://github.com/Bayly-AI/HATH0R-CLI/issues/555) | `feat(evals): replace binary 1.00 score inflation in TaskEvaluatorBot with continuous Taguchi, FinOps, AST diff, Workflow-First, Level 1/2 AgentGraph, and semantic goal-alignment grading` | **CODE & TESTS READY IN WORKTREE (Needs Branch + PR)** | `feature/555-continuous-task-evaluator-bot` | `5 passed` (`test_task_evaluator_bot.py`) | Ready to PR |
| **8** | `Bayly-AI/HATH0R-Agentic-Framework` | [#313](https://github.com/Bayly-AI/HATH0R-Agentic-Framework/issues/313) | `feat(engine): add Workflow-First & Service-Bot contracts (CR-FEATURE-WORKFLOW-STANDARD-001), Level 1/2 AgentGraph routing, 4h CalibrationGateStage, SuperSqueezeStage, and IterationCascade to hath0r-framework` | **QUEUED** | `feature/313-engine-workflow-first-calibration-supersqueeze` | — | — |
| **9** | `Bayly-AI/HATH0R-ATC` | [#80](https://github.com/Bayly-AI/HATH0R-ATC/issues/80) | `docs(architecture): codify CR-FEATURE-WORKFLOW-STANDARD-001, Level 1/2 AgentGraph topology, 4h auto-calibration, continuous evals, and hath0r-net Phoenix/MLflow/Cruise Control in HATH0R-ATC` | **COMPLETED (PR Open)** | `chore/80-mcp-central-architecture-issue` ([PR #81](https://github.com/Bayly-AI/HATH0R-ATC/pull/81)) | `12 passed` (`pytest`) + `24/24` (`make smoke`) | **`0.9689`** (`eval-20261031-105640-d31751`) |

---

## 3. Completed Ticket Details & Hand-Off Log

### Ticket #9 — `Bayly-AI/HATH0R-ATC#80` (COMPLETED · [PR #81](https://github.com/Bayly-AI/HATH0R-ATC/pull/81))
- **Workspace**: `/Users/raybayly/Development/OpenSource/hath0r-atc`
- **Deliverables**:
  - Codified `CR-FEATURE-WORKFLOW-STANDARD-001` in `AGENTS.md` and `CLAUDE.md` (1:1 synced).
  - Published canonical roadmap `docs/observe/mcp-central-architecture-roadmap-20261031.md` and this Master Hand-Off `docs/observe/MASTER_HANDOFF_MCP_CENTRAL_ARCHITECTURE.md`.
  - Updated `cfg/observability/otel.json` (`http://localhost:38000/phoenix`, `network_services` map), `cfg/observability/openobservation.json` (`cccd.calibration.freshness_4h_rate`, `workflow.first.coverage_rate`), `cfg/feature-flags/catalog.example.json` (`workflow.first.strict_offer`, `feature.service_bot.enforce`, `cccd.auto_calibrate.pre_task_enabled`), `deploy/docker/docker-compose.yml`, and `.hath0r/cccd_state.json` (`ttl_hours: 4.0`).
  - Bumped `VERSION` and `CHANGELOG.md` to `0.5.0`.
- **Eval Scorecard (`eval-20261031-105640-d31751`)**: `R_task = 0.9689` (`Tier 1 = 0.9900`, `Tier 2 = 0.9467`, `Tier 3 = 0.9775`, `Tier 4 = 0.9277`).

### Ticket #1 — `Bayly-AI/HATH0R-MCP#85` (COMPLETED · [PR #87](https://github.com/Bayly-AI/HATH0R-MCP/pull/87))
- **Workspace**: `/Users/raybayly/Development/OpenSource/hath0r-mcp`
- **Branch & PR**: `feature/85-centralize-l1-suite-tools-supersqueeze` → [PR #87](https://github.com/Bayly-AI/HATH0R-MCP/pull/87) (commit `7d7dd4b`, SemVer `1.3.2` → `1.4.0`)
- **Deliverables**:
  - Created `src/knowledgebase/core/suite_tools.py` implementing `SERVICE_BOT_WORKFLOW_REGISTRY` (`x-hath0r-owning-bot`, `x-hath0r-workflow-id`, `x-hath0r-agentgraph-level`), Level 1 `AgentGraph` tools (`mcp_agentgraph_status|query|route|sync|validate`), `hath0r_workflow_offer` (Missing-Workflow Offer using the request as acceptance test), and 28+ centralized suite tools ported from `HATH0R-CLI`.
  - Created `src/knowledgebase/core/supersqueeze.py` implementing `SuperSqueezeEngine` (`hath0r_supersqueeze`) and OpenFeature-gated response middleware (`mcp.supersqueeze.enabled`) achieving `>= 45%` token reduction on verbose payloads (`> 1024` tokens).
  - Upgraded `src/knowledgebase/core/observability.py` and `src/knowledgebase/core/feature_flags.py` to replace `ddtrace` with OpenTelemetry exporting to `Hath0r-phoenix` (`http://localhost:38000/phoenix`) + non-blocking `.hath0r/spool/mcp_telemetry.jsonl` OpenObservation telemetry.
  - Purged legacy `infraos_*` tool prefixes from `src/knowledgebase/core/mcp_tools.py`, `src/knowledgebase/api/main.py`, and `src/knowledgebase/services/status_service.py`.
  - Added unit & API tests in `tests/unit/test_issue85_level1_suite_tools_supersqueeze.py` (`610 passed, 1 skipped` total) and bumped SemVer to `1.4.0`.
- **Eval Scorecard (`eval-20261031-111203-55dc85`)**: `R_task = 0.9335` (`Tier 1 = 0.97`, `Tier 2 = 0.89`, `Tier 3 = 0.90`, `Tier 4 = 0.93`).

### Ticket #2 — `Bayly-AI/HATH0R-MCP#86` (COMPLETED · [PR #88](https://github.com/Bayly-AI/HATH0R-MCP/pull/88))
- **Workspace**: `/Users/raybayly/Development/OpenSource/hath0r-mcp`
- **Branch & PR**: `feature/86-workflow-first-engine-cruise-mlflow-phoenix` → [PR #88](https://github.com/Bayly-AI/HATH0R-MCP/pull/88) (commit `0c7e3b7`, SemVer `1.4.0` → `1.5.0`)
- **Deliverables**:
  - Created `src/knowledgebase/core/workflow_engine.py` and registered 24 Level 1 MCP tools across `src/knowledgebase/core/suite_tools.py`, `src/knowledgebase/core/mcp_tools.py`, `src/knowledgebase/api/main.py`, and `src/knowledgebase/server.py`:
    - Workflow-First Engine & Factories: `mcp_workflow_list`, `mcp_workflow_match` (with automatic Missing-Workflow Offer using the request as acceptance test), `mcp_workflow_scaffold`, `mcp_workflow_run` (with pre-task 4-hour calibration gate), `mcp_workflow_status`, `mcp_workflow_validate`, `mcp_factory_list`, `mcp_factory_execute`.
    - `BotRegistry` Service Dispatch: `mcp_bot_list`, `mcp_bot_invoke` (enforcing `feature.service_bot.enforce`), `mcp_bot_health`.
    - Level 1 ↔ Level 2 `MemoryGraph` Bridge: `mcp_memory_read`, `mcp_memory_compound`, `mcp_memory_verify`.
    - 4-Hour Pre-Task Agent Calibration (`max_age_hours = 4.0`): `mcp_cccd_status`, `mcp_cccd_calibrate`, `mcp_cccd_ensure_calibrated`.
    - `hath0r-net` Bridges: `mcp_cruise_status`, `mcp_cruise_decisions`, `mcp_cruise_approve_boundary`, `mcp_cruise_settle` (`Hath0r-Cruise-Control`), `mcp_mlflow_log_eval`, `mcp_mlflow_query_runs` (`Hathor-MLFLOW`), and `mcp_phoenix_query_spans` (`Hath0r-phoenix`).
  - Added unit & API tests in `tests/unit/test_issue86_workflow_engine_bot_dispatch_and_bridges.py` (`617 passed, 1 skipped` total) and bumped SemVer to `1.5.0`.
- **Eval Scorecard (`eval-20261031-113824-c66d32`)**: `R_task = 0.9374` (`Tier 1 = 0.97`, `Tier 2 = 0.89`, `Tier 3 = 0.92`, `Tier 4 = 0.93`).

---

## 4. Exact Instructions for Next Agent Session (Ticket #3: `Bayly-AI/HATH0R-CLI#551`)

To execute **Ticket #3 (`Bayly-AI/HATH0R-CLI#551`)**:
1. **Orient & Check 4-Hour Calibration in `/Users/raybayly/Development/OpenSource/hathor-cli`**:
   ```bash
   cd /Users/raybayly/Development/OpenSource/hathor-cli
   hath0r cccd status # Run `hath0r cccd calibrate` if age > 4.0h
   git checkout development
   git checkout -b feature/551-register-69-bots-4h-calibration-supersqueeze
   hath0r memory session start --task "Issue #551: register all 69 bots as feature service owners in BotRegistry, enforce 4-hour pre-task auto-calibration, and wire SuperSqueeze across Level 1/2 AgentGraph"
   hath0r memory session read
   ```
2. **Implement Scope of `Bayly-AI/HATH0R-CLI#551`**:
   - Register all 69+ bots in `src/hath0r_cli/factories/step_runner.py` (`BotRegistry`) with Service-Bot ownership metadata (`service_name`, `agentgraph_levels`, `workflow_ids`) so `CR-FEATURE-WORKFLOW-STANDARD-001` (`Every Feature is a Service run by >= 1 Bot`) is 100% covered (`69/69`).
   - Add `ensure_calibrated(max_age_hours: float = 4.0)` to `CICCCDManagingBot` (`src/hath0r_cli/bots/cicccd_bot.py`) and wire it into `StartOfTaskBot` (`src/hath0r_cli/bots/task_lifecycle_bots.py`) and `StepRunner` so calibration runs automatically prior to any task when expired (`> 4.0` hours).
   - Wire `SuperCompressBot` (`src/hath0r_cli/bots/super_compress_bot.py`) into `CAGCacheBot`, `RAGRetrieverBot`, `GraphRAGBot`, `MemoryCompoundBot`, and `AgentGraphBot` so Level 2 CLI/Memory retrieval and Level 1 MCP responses share unified `SuperSqueeze` token compression.
   - Add unit tests in `tests/unit/test_issue551_bot_registry_calibration_supersqueeze.py`.
3. **Run Tests, Memory Compounding, Continuous 4-Tier Evals, Open PR & Update This Hand-Off**:
   ```bash
   pytest -q tests/unit/test_issue551_bot_registry_calibration_supersqueeze.py
   hath0r agentgraph sync && hath0r agentgraph validate
   # Bump VERSION, pyproject.toml, CHANGELOG.md
   hath0r release validate
   hath0r memory session write --summary "<summary>" --kind action
   hath0r memory compound --id "episode:issue-551-botregistry-4h-calibration-supersqueeze" --type episode --label "<label>" --content "<content>"
   hath0r memory session end --summary "Completed Issue #551"
   hath0r memory hash --sync && hath0r memory verify
   hath0r evals run --task-id "issue-551" && hath0r memory hash --sync && hath0r evals verify
   git push -u origin feature/551-register-69-bots-4h-calibration-supersqueeze
   gh pr create --repo Bayly-AI/HATH0R-CLI --base development --head feature/551-register-69-bots-4h-calibration-supersqueeze ...
   ```
4. **Update `docs/observe/MASTER_HANDOFF_MCP_CENTRAL_ARCHITECTURE.md` in `hath0r-atc`** with Ticket #3's PR URL and Eval Scorecard before ending the session.
