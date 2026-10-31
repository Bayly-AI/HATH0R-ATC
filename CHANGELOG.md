# Changelog

All notable changes to **HATH0R-ATC** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.7] - 2026-10-31

### Added
- **HATH0R MCP-Central Architecture, SuperSqueeze & Bot Execution Plan (`#80`)**:
  - Published canonical cross-repo roadmap [`docs/observe/mcp-central-architecture-roadmap-20261031.md`](docs/observe/mcp-central-architecture-roadmap-20261031.md) tracking GitHub Issues `Bayly-AI/HATH0R-MCP#85`, `Bayly-AI/HATH0R-MCP#86`, `Bayly-AI/HATH0R-CLI#551`–`#554`, `Bayly-AI/HATH0R-Agentic-Framework#313`, and `Bayly-AI/HATH0R-ATC#80`.
  - Codified the `Task → Hath0r-CLI (⇄ Hath0r-MCP) → Computer → Web` 4-stage iteration cascade, `SuperSqueeze` (`SuperCompressBot`) middleware pipeline, 7 architecture-preserving bots, and mandatory per-issue Test + 4-Tier Eval (`CR-TASK-EVAL-001`) + SemVer PR gate.
  - Added canonical OpenObservation stub [`cfg/observability/openobservation.json`](cfg/observability/openobservation.json), populated OpenFeature catalog flags in [`cfg/feature-flags/catalog.example.json`](cfg/feature-flags/catalog.example.json), updated [`docs/governance/SUITE_STANDARDS.md`](docs/governance/SUITE_STANDARDS.md), and enforced **OpenFeature + OpenObserve (`OpenObservation`) + OpenTelemetry (`OTel`)** core architecture adherence across all 8 GitHub Issues and bot contracts.
  - Aligned [`cfg/observability/otel.json`](cfg/observability/otel.json) (`default_endpoint: http://localhost:38000/phoenix`, `network_services` topology) and [`deploy/docker/docker-compose.yml`](deploy/docker/docker-compose.yml) with live **`hath0r-net`** endpoints for **Arize Phoenix (`Hath0r-phoenix`)**, **MLflow (`Hathor-MLFLOW`)**, and **Cruise Control (`Hath0r-Cruise-Control`)**.
  - Added **Automated 4-Hour Agent Calibration TTL (`max_age_hours = 4.0`) & Automatic Pre-Task Calibration Execution (`ensure_calibrated(max_age_hours=4.0)`)** across `.hath0r/cccd_state.json`, OpenFeature (`cccd.auto_calibrate.pre_task_enabled`, `cccd.auto_calibrate.ttl_hours`), OpenObservation (`cccd.calibration.freshness_4h_rate`), the roadmap, and all linked GitHub Issues.
  - Linked `Bayly-AI/HATH0R-CLI#555` eliminating binary `1.0000` score inflation in `TaskEvaluatorBot` in favor of continuous Taguchi, FinOps, AST diff, and semantic goal-alignment grading.

## [0.5.6] - 2026-10-29

### Added
- **Automatic Post-Task Evaluation & Pre-Push Verification Hooks (`CR-TASK-EVAL-001`)**:
  - Provisioned `cfg/evals/task-eval.json` (`auto_run_after_every_task: true`, `require_scorecard_summary: true`), `.hath0r/evals/post-task-hook.sh`, `.git/hooks/pre-push` (`hath0r evals verify --auto-run`), and 1:1 `CLAUDE.md` ↔ `AGENTS.md` synchronization.

## [0.5.5] - 2026-10-29

### Changed
- **Rule Harmonization, `CLAUDE.md` 1:1 Sync & Workflow Upgrade (`CR-CLAUDE-SYNC-001` · `CR-AGENTIC-SEC-001`)**:
  - Added `CR-CLAUDE-SYNC-001`, `CR-AGENTIC-SEC-001`, and `CR-MEMORY-COMPOUND-001` to `AGENTS.md`, synchronized `CLAUDE.md` 1:1 with `AGENTS.md`, initialized `THREATMODEL.md`, and updated `.agents/skills/clean-repos/SKILL.md` and `.agents/skills/orient/SKILL.md`.

## [0.5.4] - 2026-10-29

### Added
- **`CR-CLI-ENTRY-001` (Start with the CLI — CANONICAL)** in `AGENTS.md`: agents check the `hath0r` operator CLI first on every request, offer to register missing capabilities, and require docs before code.

### Fixed
- **Cruise Control keeps real decisions (Bayly-AI/HATH0R-CLI#532)**: the `cruise-control` service no longer starts with `--seed-demo`, which wiped the decision store and reseeded the reference topology on every container start. Seed on demand with `POST /api/decisions/seed`.

## [0.5.3] - 2026-10-28

### Changed
- **Mandatory Eval Scorecard Summary Rule (`CR-TASK-EVAL-001` — `#76`)**:
  - Updated `CR-TASK-EVAL-001` in `AGENTS.md`, `WARP.md`, and `.hath0r/memory/core_rules.md` to mandate as **CRITICAL · CANONICAL** that agents always return a structured summary of the Eval Scorecard after completion of every task.

## [0.5.2] - 2026-10-28

### Changed
- **Clean Repositories Skill & Standard Operating Procedure (`.agents/skills/clean-repos/SKILL.md` — `#73`)**:
  - Updated the 13-step Clean Repo workflow specification to review all local and remote non-canonical branches, merge branches with unmerged changes into `development` while resolving conflicts, delete stale local and remote feature branches (`git branch -D` and `git push origin --delete`), run `CR-TASK-EVAL-001` & `CR-MEMORY-COMPOUND-001` before final commit, and switch back to `development` with `git pull --rebase origin development` and `git push origin development`.

## [0.5.1] - 2026-10-28

### Changed
- **Cruise Control & Task Evaluation Documentation (`#71`)**:
  - Added `Hath0r-Cruise-Control`, `Hathor-MLFLOW`, and `Hath0r-phoenix` to `canonical_containers` in `cfg/suite.yaml`.
  - Documented `Hath0r-Cruise-Control` (`38090` -> `8090`, edge `/cruise/radar`) in `docs/deployment-local-docker.md`.
  - Synchronized `CR-TASK-EVAL-001` governance rules in `AGENTS.md`, `WARP.md`, `.hath0r/evals/`, and `.hath0r/memory/`.

## [0.5.0] - 2026-10-28

### Added
- **Hath0r Cruise Control Container (`Hath0r-Cruise-Control` — `#69`)**:
  - Added canonical `cruise-control` (`Hath0r-Cruise-Control`, image `hath0r/cruise-control:local`, port `38090:8090`, volume `hath0r_cruise_data`) service to `deploy/docker/docker-compose.yml` in the `hath0r` Docker group (`CR-DOCKER-HATH0R-GROUP-001`).
  - Added `/cruise/` and `/api/decisions` reverse-proxy routes to `Hath0r-Edge` NGINX (`deploy/docker/nginx/conf.d/default.conf`).
  - Updated `deploy/docker/Makefile` and `deploy/docker/smoke-test.sh` to start and verify `Hath0r-Cruise-Control` alongside `Hath0r-Edge`, `Hath0r-Sessions`, `Hath0r-phoenix`, and `Hathor-MLFLOW`.
  - Added contract tests in `tests/test_contracts.py`.

## [0.4.4] - 2026-10-28

### Added
- **Automatic Task Evaluation Configuration (`CR-TASK-EVAL-001`)**: Added declarative `cfg/evals/task-eval.json` binding `HATH0R-ATC` to `TaskEvaluatorBot` (`hath0r evals run`), `.hath0r/evals/` gitignore negation rules, and Phoenix/MLflow task evaluation observability (#67).

## [0.4.3] - 2026-10-28

### Added
- CR-SEMVER-BUMP-001: every created or merged PR must create or bump the product's Semantic Version (`VERSION` is the source of truth).

## [0.4.2] - 2026-10-28

### Changed
- Added `CR-SONAR-PREANNOUNCE-001` to the agent instructions: confirm SonarCloud Quality Gate thresholds before announcing work Complete.

## [0.4.1] - 2026-10-12

### Added
- Adopted Infrastructure as Code, Container Salting, and AWS EKS Fargate Deployment.
