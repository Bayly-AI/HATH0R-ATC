---
id: cr-branch-gov-001
title: Canonical Branch & PR Governance
version: 0.2.0
severity: CRITICAL
applies_to: "hath0r-opensource"
effective_date: 2026-05-16
last_updated: 2026-09-23
---

# CR-BRANCH-GOV-001 — Canonical Branch & PR Governance (CRITICAL)

## Integration (long-lived) branches

```
development → testing → staging → master
```

- Do **not** skip stages or reverse-promote.
- `development` is the **default integration branch** for day-to-day delivery.
- `master` is the **production** line (not a day-to-day PR target).
- `main` is not used as an integration branch; prefer `master` for production.

## Feature-branch workflow (CANONICAL)

1. Branch from **`development`**.
2. Implement on `feature/*`, `fix/*`, `chore/*`, or `docs/*` (issue number required).
3. Open PR with **base = `development`**.
4. Merge into **`development` only**.
5. Promote: `development` → `testing` → `staging` → `master` (release path).

### Forbidden

- Normal delivery PRs targeting `master` or `main`
- Feature PRs targeting `testing` or `staging`
- Unreviewed pushes of delivery work to `master`

## Agent checklist

- [ ] Work branch is not `master` / `main` / `development`
- [ ] Branched from latest `development`
- [ ] PR base is `development`
