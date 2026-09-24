# Semantic versioning (ATC pointer)

Canonical suite policy: [HATH0R-CLI semantic-versioning.md](https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/semantic-versioning.md) (SemVer 2.0.0).

## ATC rules

| Rule | Value |
|------|-------|
| Canonical version file | [`VERSION`](../../VERSION) at repo root (currently single-line SemVer) |
| Align | `VERSION`, package/metadata manifests, release tags, and changelog entries |
| Pre-release | Use SemVer pre-release labels when needed (`-rc.N`, `-beta.N`) |
| Breaking | MAJOR; features MINOR; fixes PATCH |
| Control tower | Do not fork policy — update CLI standards, then refresh this pointer if paths change |

Issue: #10
