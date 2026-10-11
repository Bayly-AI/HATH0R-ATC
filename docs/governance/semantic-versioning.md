# Semantic Versioning — HATH0R ATC

Canonical suite policy: [HATH0R-CLI semantic-versioning.md](https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/semantic-versioning.md) (SemVer 2.0.0).

## ATC Rules & Single Canonical Source of Truth

The root [`VERSION`](../../VERSION) file is the **exclusive canonical source of truth** for HATH0R ATC version state.

| Rule | Value | Description |
|------|-------|-------------|
| Canonical version file | [`VERSION`](../../VERSION) | Single-line SemVer string (`MAJOR.MINOR.PATCH`) |
| Changelog alignment | [`CHANGELOG.md`](../../CHANGELOG.md) | Must contain matching section `## [X.Y.Z]` |
| PR Declaration | `version-policy-guard.yml` | All PRs must declare impact (`semver:patch`, `minor`, `major`, `none`) |
| Release Runbook | [`release-runbook.md`](playbooks/release-runbook.md) | Step-by-step operational release procedures |
| Tag Format | `vX.Y.Z` (e.g. `v0.2.2`) | Annotated Git tags triggering `.github/workflows/release.yml` |

## SemVer Impact Taxonomy

- **MAJOR (`semver:major`)**: Breaking architectural changes, incompatible configuration schema shifts, or backwards-incompatible API changes.
- **MINOR (`semver:minor`)**: New services, new Docker compose profiles, backwards-compatible feature additions.
- **PATCH (`semver:patch`)**: Bug fixes, security hardening, lint/docs refactoring.
- **NONE (`semver:none`)**: Non-functional documentation updates or CI fixes that do not change runtime behavior.
