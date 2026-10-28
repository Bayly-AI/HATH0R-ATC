# Changelog

All notable changes to **HATH0R-ATC** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
