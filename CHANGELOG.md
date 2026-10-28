# Changelog

All notable changes to **HATH0R-ATC** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
