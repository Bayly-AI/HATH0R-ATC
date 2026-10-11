# AGENTS.md — Contracts Subsystem (HATH0R-ATC)

> Hyper-context node for **HATH0R ATC Contracts & JSON Schemas Subsystem**.
> Parent Node: [`../AGENTS.md`](../AGENTS.md)

## Subsystem Identity & Role

| Field | Value |
|---|---|
| Subsystem | `contracts` |
| Scope | JSON Schemas, Exit Code Registry, CLI/Tower Interoperability Contracts |
| Standards Authority | `Bayly-AI/HATH0R-Agentic-Framework` |
| Pinned Version | `0.2.0` / `0.3.0` / `0.4.0` |

## Operational Guidelines

1. **Schema Authority**: Pinned schemas define the invariant envelope contracts between CLI, Control Tower, and member services.
2. **Backward Compatibility**: Schema additions must be backward compatible; removing or altering required fields is prohibited without explicit SemVer major bump.
3. **Exit Code Mapping**: All automated processes and bots must emit standard exit codes defined in [`exit-codes.yaml`](exit-codes.yaml).

## Key Files & Direct Links

- [exit-codes.yaml](file:///Users/raybayly/Development/OpenSource/hath0r-atc/contracts/exit-codes.yaml): Canonical process return codes.
- [hath0r-factory-v1.schema.json](file:///Users/raybayly/Development/OpenSource/hath0r-atc/contracts/hath0r-factory-v1.schema.json): Schema contract for declarative automation factories.
- [hath0r-docker-workflow-v1.schema.json](file:///Users/raybayly/Development/OpenSource/hath0r-atc/contracts/hath0r-docker-workflow-v1.schema.json): Schema contract for Docker group workflows.
- [rules.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/contracts/rules.md): Contract immutability rules.
- [canonical.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/contracts/canonical.md): Contract registry index.
