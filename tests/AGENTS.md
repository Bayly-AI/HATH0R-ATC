# AGENTS.md — Tests Subsystem (HATH0R-ATC)

> Hyper-context node for **HATH0R ATC Test Subsystem**.
> Parent Node: [`../AGENTS.md`](../AGENTS.md)

## Subsystem Identity & Role

| Field | Value |
|---|---|
| Subsystem | `tests` |
| Scope | Infrastructure Smoke Tests, Bootstrap Verification, Contract Testing |
| Entrypoints | `make smoke`, `make bootstrap`, `./bin/hath0r-bootstrap.sh` |

## Operational Guidelines

1. **Bootstrap Validation**: Always run `make bootstrap` or `./bin/hath0r-bootstrap.sh` to ensure layout and identity conformance.
2. **Smoke Testing**: Run `make smoke` against live local containers to verify edge NGINX and Redis connectivity.
3. **Contract Tests**: Verify that ATC schemas validate against the canonical framework schemas.

## Key Files & Direct Links

- [hath0r-bootstrap.sh](file:///Users/raybayly/Development/OpenSource/hath0r-atc/bin/hath0r-bootstrap.sh): Local fileset and environment verification script.
- [smoke-test.sh](file:///Users/raybayly/Development/OpenSource/hath0r-atc/deploy/docker/smoke-test.sh): Automated edge and state connectivity smoke test.
- [rules.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/tests/rules.md): Testing rules and assertions.
- [canonical.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/tests/canonical.md): Test harness reference.
