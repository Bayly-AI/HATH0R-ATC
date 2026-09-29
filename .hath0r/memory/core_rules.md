# Core Rules — HATH0R ATC

1. **CR-DOCKER-HATH0R-GROUP-001**: All services and containers under the OpenSource project must belong to the `hath0r` Docker group, attach to `hath0r-net`, and carry `com.hath0r.*` labels.
2. **CLI-First (cr-cli-first-001)**: Prefer `hath0r` operator CLI (`../hathor-cli`) and standard Make targets (`make docker-up`, `make smoke`).
3. **Bots not Daemons**: Autonomous processes are bots or factories.
4. **Zero Git Secrets**: External credentials resolve via `/Users/raybayly/Development/.credentials/`.
5. **Promotion Path (CR-BRANCH-GOV-001)**: `feature/refactor/* -> development -> testing -> staging -> master`.
