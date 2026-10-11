# AGENTS.md — Configuration Subsystem (HATH0R-ATC)

> Hyper-context node for **HATH0R ATC Configuration & Governance Subsystem**.
> Parent Node: [`../AGENTS.md`](../AGENTS.md)

## Subsystem Identity & Role

| Field | Value |
|---|---|
| Subsystem | `cfg` |
| Scope | Suite Identity, Product Catalog, Control Tower Topology, Observability Pointers |
| Role | Central configuration registry for OpenSource suite members |

## Operational Guidelines

1. **Central Group Controller**: Suite configuration in [`cfg/suite.yaml`](suite.yaml) and [`cfg/control-tower.yaml`](control-tower.yaml) governs membership policies across all repositories in this workspace.
2. **Product Catalog**: Canonical repository metadata, paths, and remotes are indexed in [`cfg/products.yaml`](products.yaml).
3. **Observability & Feature Flags**: Pointers to OpenTelemetry (`cfg/observability/`) and OpenFeature (`cfg/feature-flags/`) stubs are maintained here.
4. **Zero Git Secrets**: Never commit tokens, passwords, or credentials into `cfg/`.

## Key Files & Direct Links

- [suite.yaml](file:///Users/raybayly/Development/OpenSource/hath0r-atc/cfg/suite.yaml): OpenSource suite definition and global policies.
- [control-tower.yaml](file:///Users/raybayly/Development/OpenSource/hath0r-atc/cfg/control-tower.yaml): Control Tower operational specifications.
- [products.yaml](file:///Users/raybayly/Development/OpenSource/hath0r-atc/cfg/products.yaml): Suite product catalog.
- [rules.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/cfg/rules.md): Configuration governance rules.
- [canonical.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/cfg/canonical.md): Configuration reference index.
