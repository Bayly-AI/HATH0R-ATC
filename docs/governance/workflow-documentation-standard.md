# Workflow documentation standard (ATC pointer)

Canonical suite policy: [HATH0R-CLI workflow-documentation-standard.md](https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/workflow-documentation-standard.md).

## Required document types (suite)

| Type | Purpose | ATC home |
|------|---------|----------|
| Procedure | Step sequences operators follow | `docs/governance/checklists/`, `docs/governance/playbooks/` |
| Strategy | Why/when choices | Prefer CLI `docs/governance/strategies/` unless ATC-specific |
| Playbook | Multi-step incident/release narratives | `docs/governance/playbooks/` |
| Runbook | Day-2 ops for this product | [`docs/runbook.md`](../runbook.md) |
| Checklist | PR/gate gates | `docs/governance/checklists/` |

## ATC notes

- ATC already carries PR workflow playbooks/checklists under `docs/governance/`.
- Docker workflows for the suite should follow CLI factory/workflow JSON when present; runtime compose remains [`deploy/docker/`](../../deploy/docker/).
- New operator procedures for observation or group control should land here and link this standard.

Issue: #15 · related docker workflows: #9
