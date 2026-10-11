# Changelog

All notable changes to HATH0R ATC (Air Traffic Control) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Updated canonical container names across Docker Compose, NGINX edge proxy, and Makefile (#47):
  - `phoenix` -> `Hath0r-phoenix` (Canonical)
  - `nginx` -> `Hath0r-Edge` (Canonical)
  - `postgres` -> `Hath0r-Data` (Canonical)
  - `redis` -> `Hath0r-Sessions` (Canonical)
  - `mcp` -> `Hath0r-MCP` (Canonical)
- Maintained legacy `hath0r-*` network aliases for backwards-compatible service discovery.

## [0.3.0] - 2026-10-11

### Added
- Integrated MLflow MLOps experiment tracking container (`Hathor-MLFLOW`) into the `hath0r` canonical Docker group.
- Added NGINX edge reverse proxy route `/mlflow/` and DNS aliases on `hath0r-net`.
- Added contract tests in `tests/test_contracts.py` for Docker compose configuration.

## [0.2.2] - 2026-10-11

### Added
- Implemented Semantic Versioning 2.0.0 compliance and PR Version Policy Guard (`.github/workflows/version-policy-guard.yml`).
- Added automated release workflow (`.github/workflows/release.yml`) and release governance runbook (`docs/governance/playbooks/release-runbook.md`).
- Enhanced SonarCloud Quality Gate workflow and project properties alignment.
- Added MLflow experiment tracking container configuration in Docker Compose.

### Changed
- Standardized canonical versioning across manifests and suite catalog pointers.
- Aligned branch governance and promotion environment gates (`CR-BAI-001`).

## [0.2.1] - 2026-10-05

### Added
- Integrated Arize Phoenix observability container in Docker Compose layout.
- Added health probes and Redis edge router integration.

### Fixed
- Fixed SonarCloud project key configuration and API quality gate checks.

## [0.2.0] - 2026-09-23

### Added
- Initial OpenSource control tower release for infrastructure, observation, and Docker-group membership.
- Reverse proxy configurations, Redis cache container, and basic network bridges.
