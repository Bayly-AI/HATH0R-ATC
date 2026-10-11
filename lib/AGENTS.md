# AGENTS.md — Library Subsystem (HATH0R-ATC)

> Hyper-context node for **HATH0R ATC Shared Libraries & Scripts Subsystem**.
> Parent Node: [`../AGENTS.md`](../AGENTS.md)

## Subsystem Identity & Role

| Field | Value |
|---|---|
| Subsystem | `lib` |
| Scope | Shared helper scripts, telemetry utilities, asset bundles |

## Operational Guidelines

1. **Self-Contained Utilities**: Helper scripts and modules should be modular and avoid external dependency bloat.
2. **Python Compatibility**: All python scripts in `lib/` must support Python 3.10+.
3. **No Side Effects on Import**: Modules in `lib/` must not perform network or filesystem mutations on import.

## Key Files & Direct Links

- [rules.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/lib/rules.md): Library design rules.
- [canonical.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/lib/canonical.md): Library assets index.
