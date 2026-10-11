# Release Runbook — HATH0R ATC

> Role: Operational guide for versioning, release validation, and tag publishing.  
> Status: Canonical · Member of `hath0r-opensource`  
> Policy: [Semantic Versioning](../semantic-versioning.md) · [HATH0R-CLI SemVer](https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/semantic-versioning.md)

---

## 1. Prerequisites

Before cutting a release:
1. All PRs merged into `development`.
2. Promotion gates satisfied: `development` -> `testing` -> `staging` -> `master`.
3. Working tree is clean: `git status`.
4. Quality checks pass: SonarCloud quality gate and branch governance.

---

## 2. Release Steps

### Step 1: Validate Version and Changelog
Verify alignment between `VERSION` and `CHANGELOG.md`:
```bash
hath0r release validate
```

### Step 2: Bump Version (if necessary)
For new releases, update the root `VERSION` file:
```bash
echo "0.2.3" > VERSION
```
Update `CHANGELOG.md` with the new version section under `## [X.Y.Z] - YYYY-MM-DD`.

### Step 3: Promote along Canonical Path
Promote branch following CR-BAI-001:
```bash
git checkout testing && git merge development
git checkout staging && git merge testing
git checkout master && git merge staging
```

### Step 4: Tag Release on Master
Create an annotated Git tag on `master`:
```bash
git tag -a v0.2.2 -m "Release v0.2.2"
git push origin v0.2.2
```

### Step 5: Verify Automated Release Workflow
The `.github/workflows/release.yml` workflow triggers on push of `v*` tags, extracting release notes from `CHANGELOG.md` and generating the GitHub Release.
