# HATH0R MCP-Central Architecture, SuperSqueeze & Bot Execution Plan

> **Control Tower**: `HATH0R-ATC` (`Bayly-AI/HATH0R-ATC` · Issue [#80](https://github.com/Bayly-AI/HATH0R-ATC/issues/80))  
> **Paired Governance & MCP Hub**: `HATH0R-CLI` (`Bayly-AI/HATH0R-CLI`) ⇄ `HATH0R-MCP` (`Bayly-AI/HATH0R-MCP`)  
> **Cognitive Substrate**: `HATH0R-Agentic-Framework` (`Bayly-AI/HATH0R-Agentic-Framework`)  
> **Date**: 2026-10-31 · **Rules**: `CR-CLI-ENTRY-001` · `CR-CLI-MCP-ECOSYSTEM-001` · `CR-SUBSTRATE-001` · `CR-MEMORY-COMPOUND-001` · `CR-TASK-EVAL-001` · `CR-SEMVER-BUMP-001`

---

## 1. Executive Summary & Architectural Directive

To maximize technology utilization across the Hath0r OpenSource Suite and guarantee that every task is **finished, completed, and accurate**, the suite architecture is unified around three core invariants:

1. **HATH0R-MCP as the Single Central Hub (`Priority 1`)**:
   - All shared tools, declarative workflows (`cfg/factories/*.yaml`), `BotRegistry` dispatches, Quad-Graph queries (`KnowledgeGraph`, `ContextGraph`, `MemoryGraph`, `RulesGraph`), and **SuperSqueeze** (`SuperCompressBot`) compression pipelines reside centrally in **`HATH0R-MCP`** (`http://127.0.0.1:38083` / `https://mcp.hath0r-cli.com`).
   - **`HATH0R-CLI` (`hath0r`)** remains the mandatory operator and agent entry gate (`CR-CLI-ENTRY-001`), dispatching commands and workflows through `HATH0R-MCP` (`Priority 1`) with deterministic local fallback when offline.
2. **Strict 4-Stage Iteration Cascade (`Task → Hath0r-CLI ⇄ Hath0r-MCP → Computer → Web`)**:
   - **Stage 1 (`Task`)**: Check active micro-memory session (`< 2KB`), active `TaskExecutionDAG`, settled facts (`FactSettlementEngine`), and pre-warmed CAG context first.
   - **Stage 2 (`Hath0r-CLI ⇄ Hath0r-MCP`)**: Invoke `hath0r` CLI subcommands, which route tool, workflow, bot, and knowledge operations to `HATH0R-MCP` (`Priority 1`). Every MCP response passes through `PBACPolicyEngine` → `L2OutputSanitizer` → **SuperSqueeze (`SuperCompressBot`)** → `KVCachePrewarmer` 16-token block alignment.
   - **Stage 3 (`Computer`)**: Execute bounded local file line-slices, AST outlines, sandboxed commands (`LocalSandboxProvider` / `WasmSandbox`), `hath0r` Docker group containers, or offline `DeepSeek-R1` (`LocalModelBot`).
   - **Stage 4 (`Web`)**: Query external web/APIs/Playwright only as the final escalation tier, and immediately **SuperSqueeze + L2-sanitize + compound** discovered facts back into `HATH0R-MCP` (`kb_upsert_document`) and `.hath0r/memory/graph.json` so subsequent iterations resolve at Stage 1 or Stage 2.
3. **Mandatory Per-Issue Test + 4-Tier Eval + SemVer + PR Gate**:
   - Every issue in the roadmap MUST execute the full verification lifecycle (Unit/Integration Tests + MemoryGraph Compounding + 4-Tier Task Evaluation with `R_task >= 0.80` + SemVer Bump + PR to `development` + SonarCloud Quality Gate) before advancing to the next issue.

---

## 2. Cross-Repository GitHub Issue Matrix

| Order | Repository | Issue | Title & Scope |
|---|---|---|---|
| **1** | `Bayly-AI/HATH0R-MCP` | [#85](https://github.com/Bayly-AI/HATH0R-MCP/issues/85) | **Centralize Suite Tools, SuperSqueeze Middleware & Clean Legacy `infraos_*` Schemas in HATH0R-MCP**: Port 28+ CLI-trapped MCP tools from `hathor-cli` into `hath0r-mcp`, expose `hath0r_supersqueeze`, wire automatic SuperSqueeze output compression into `kb_search`/`kb_get_document`/`docs_read_content`/`runbook_get_prompt`, and remove legacy `infraos_*` references. |
| **2** | `Bayly-AI/HATH0R-MCP` | [#86](https://github.com/Bayly-AI/HATH0R-MCP/issues/86) | **Expose Declarative Workflows, Factories, BotRegistry Dispatch, MemoryGraph & Cruise Control in HATH0R-MCP**: Add `hath0r_workflow_list`, `hath0r_workflow_run`, `hath0r_bot_list`, `hath0r_bot_invoke`, `hath0r_task_start`, `hath0r_task_finish`, `hath0r_task_evaluate`, `hath0r_memory_*`, `hath0r_decision_radar`, and `hath0r_tlp_plan` endpoints to `HATH0R-MCP`. |
| **3** | `Bayly-AI/HATH0R-CLI` | [#551](https://github.com/Bayly-AI/HATH0R-CLI/issues/551) | **Register All 69 Bots in `BotRegistry` & Wire `SuperSqueezeBot` Across CAG, Hybrid Router, HAHP & CLI**: Map all 22+ unmapped cognitive/security/optimization bots in `step_runner.py`, add `hath0r supersqueeze` / `hath0r context squeeze`, and wire `SuperCompressBot` into `CAGEngine`, `HybridCAGRAGRouter`, and `HAHPEnvelope`. |
| **4** | `Bayly-AI/HATH0R-CLI` | [#552](https://github.com/Bayly-AI/HATH0R-CLI/issues/552) | **Implement `MCPCentralizationBot` & `MCPWorkflowEngineBot` and Route CLI Commands Through HATH0R-MCP (`Priority 1`)**: Route `hath0r` CLI commands (`kb`, `agentgraph`, `context`, `factory`, `task`) and `hath0r mcp serve` through `HATH0R-MCP` first with deterministic local fallback, and enforce `SchemaPruner` + `BITEVerifierBot` SHA-256 schema pinning. |
| **5** | `Bayly-AI/HATH0R-CLI` | [#553](https://github.com/Bayly-AI/HATH0R-CLI/issues/553) | **Implement `IterationCascadeBot` to Enforce `Task → Hath0r-CLI/MCP → Computer → Web` Escalation**: Upgrade `NeuralIntentClassifier` in `cag_rag_router.py` to 4 cascade stages (`STAGE_1_TASK`, `STAGE_2_CLI_MCP`, `STAGE_3_COMPUTER`, `STAGE_4_WEB`) and score trajectory order compliance inside `TaskEvaluatorBot` Tier 2. |
| **6** | `Bayly-AI/HATH0R-CLI` | [#554](https://github.com/Bayly-AI/HATH0R-CLI/issues/554) | **Implement `ArchitecturePreservationBot`, `SubstrateUtilizationBot` & `TaskCompletionVerifierBot` and Wire Task Factories**: Enforce `CR-CLI-FEATURE-STANDARD-001`, `CR-SUBSTRATE-001`, and 100% DAG/Decision/MCP-sync completion inside `start-of-task-factory.yaml` and `end-of-task-factory.yaml`. |
| **7** | `Bayly-AI/HATH0R-Agentic-Framework` | [#313](https://github.com/Bayly-AI/HATH0R-Agentic-Framework/issues/313) | **Add Engine-Level `SuperSqueeze` Pipeline Stage, 4-Stage `IterationCascade` Contract & `CR-MCP-CENTRAL-001` Governance**: Add `contracts/hath0r-iteration-cascade-v1.schema.json` and `contracts/hath0r-mcp-workflow-v1.schema.json`, update `DynamicToolRouter` / `ContextGraph`, and ratify `CR-ITERATION-CASCADE-001` and `CR-MCP-CENTRAL-001`. |
| **8** | `Bayly-AI/HATH0R-ATC` | [#80](https://github.com/Bayly-AI/HATH0R-ATC/issues/80) | **Publish Canonical Suite Execution Plan & Tower Config for MCP-Central Tools, Workflows, SuperSqueeze & Architecture Bots**: Commit this roadmap to `HATH0R-ATC`, validate tests & 4-tier evals, bump SemVer, and merge PR to `development`. |

---

## 3. Architecture-Preserving Bots Specification

1. **`MCPCentralizationBot` (`mcp-centralization-bot`)**: Audits tool, workflow, and schema parity between `HATH0R-CLI` and `HATH0R-MCP`, prunes verbose JSON schemas via `SchemaPruner`, and pins SHA-256 digests via `BITEVerifierBot` (`hath0r mcp audit`).
2. **`MCPWorkflowEngineBot` (`mcp-workflow-engine-bot`)**: Exposes declarative `cfg/factories/*.yaml` workflows and all 69 `BotRegistry` bots as `HATH0R-MCP` tools and routes CLI invocations through `HATH0R-MCP` (`Priority 1`) with offline local fallback.
3. **`SuperSqueezeBot` (`supersqueeze-bot` / `supercompress-bot`)**: Applies query-aware semantic context compression across `HATH0R-MCP` tool outputs, `CAGEngine.pack_context()`, `HybridCAGRAGRouter.rag_search()`, and `HAHPEnvelope` handoffs prior to `KVCachePrewarmer` block alignment.
4. **`IterationCascadeBot` (`iteration-cascade-bot`)**: Enforces the `Task → Hath0r-CLI (⇄ Hath0r-MCP) → Computer → Web` execution order and verifies that Stage 3/4 discoveries are compounded back into `HATH0R-MCP` and `MemoryGraph`.
5. **`ArchitecturePreservationBot` (`architecture-preservation-bot`)**: Enforces `CR-CLI-FEATURE-STANDARD-001` (zero code duplication in member repos), 100% `BotRegistry` registration coverage, control-tower role separation, `.hath0r/` hidden root (`cr-hath0r-root-001`), and `.hath0r/mcp.json` Priority 1 config.
6. **`SubstrateUtilizationBot` (`substrate-utilization-bot`)**: Enforces `CR-SUBSTRATE-001` and `CR-CLI-AGENT-SUBSTRATE-002` (`GuardrailsManager`, `AIGatewayClient`/`TieredRouter`, `PBACPolicyEngine`, `L2OutputSanitizer`, `KVCachePrewarmer`, `TokenTreeBudgetGuard`, and `CCCD <= 24h`).
7. **`TaskCompletionVerifierBot` (`task-completion-verifier-bot`)**: Hard pre-merge gate verifying all `TaskExecutionDAG` nodes are `COMPLETED`, zero `CruiseControlBot` blockers remain open, knowledge is synced to `HATH0R-MCP`, `CLAUDE.md == AGENTS.md`, `THREATMODEL.md` is valid, SemVer is bumped, SonarCloud is green, and `R_task >= 0.80`.

---

## 4. Mandatory Per-Issue Execution Protocol (Tests + Evals + PR)

Every issue above MUST be executed using the canonical 7-step CLI lifecycle:

```bash
# 1. Start work branch & micro-memory session
hath0r task start --issue <ISSUE_NUMBER> --slug <SHORT_SLUG> --prefix feature

# 2. Author Governance Documentation Hexad + Implementation + Unit/Integration Tests
pytest

# 3. Compound MemoryGraph & synchronize SHA-256 file hashes (CR-MEMORY-COMPOUND-001)
hath0r memory session read
hath0r memory session write --summary "<SUMMARY>" --kind finding
hath0r memory compound --id "episode:issue-<ISSUE_NUMBER>" --type episode --label "<LABEL>" --content "<CONTENT>"
hath0r memory session end --summary "Completed Issue #<ISSUE_NUMBER>"
hath0r memory hash --sync
hath0r memory verify

# 4. Run & verify 4-Tier Hybrid Task Evaluation Gate (CR-TASK-EVAL-001: R_task >= 0.80)
hath0r evals run --task-id "issue-<ISSUE_NUMBER>"
hath0r memory hash --sync
hath0r evals verify

# 5. Bump SemVer (VERSION, pyproject.toml, CHANGELOG.md) & validate (CR-SEMVER-BUMP-001)
hath0r release validate

# 6. Check SonarCloud & preflight gates (CR-SONAR-PREANNOUNCE-001)
hath0r preflight

# 7. Open Pull Request targeting development & monitor checks (CR-BRANCH-GOV-001)
hath0r pr create --semver minor
```
