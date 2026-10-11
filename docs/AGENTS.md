# AGENTS.md — Documentation Subsystem (HATH0R-ATC)

> Hyper-context node for **HATH0R ATC Documentation Subsystem**.
> Parent Node: [`../AGENTS.md`](../AGENTS.md)

## Subsystem Identity & Role

| Field | Value |
|---|---|
| Subsystem | `docs` |
| Scope | Operational Runbooks, Governance Rules, Observation Logs, Deployment Guides |
| Standard | Standard Playbook → Procedure → Runbook taxonomy (`HATHOR-GUIDE-001`) |

## Operational Guidelines

1. **Docs Before Code**: Before changing operational infrastructure, verify or update the runbook at [`docs/runbook.md`](runbook.md).
2. **Observation Archives**: Operational smoke test logs and health snapshots are archived in `docs/observe/` and `docs/archive/`.
3. **Governance References**: Branch promotion, PR workflow hardening, SonarCloud gates, and Docker group rules live in `docs/governance/` and `docs/rules/`.

## Key Files & Direct Links

- [runbook.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/docs/runbook.md): Technology operations runbook for HATH0R-ATC.
- [deployment-local-docker.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/docs/deployment-local-docker.md): Local Docker deployment procedures.
- [INDEX.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/docs/INDEX.md): Index of documentation taxonomy.
- [rules.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/docs/rules.md): Documentation rules and formatting standards.
- [canonical.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/docs/canonical.md): Documentation taxonomy and reference structure.
