# Tests Subsystem — Canonical Harness & Harness Matrix

> Canonical reference for test suites and harnesses in HATH0R-ATC.

## Test Harnesses

| Suite | Entrypoint | Scope |
|---|---|---|
| Bootstrap | `./bin/hath0r-bootstrap.sh` | Layout, hidden root (`.hath0r/`), MANIFEST, VERSION checks |
| Smoke | `./deploy/docker/smoke-test.sh` | NGINX edge port `38080` & Redis port `38079` ping |
| Doctor | `hath0r doctor` | Group root, tower, and member pointer discovery |
