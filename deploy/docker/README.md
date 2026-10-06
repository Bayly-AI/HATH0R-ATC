# Hath0r Docker group

**CANONICAL:** every repository under `/Users/raybayly/Development/OpenSource` belongs to this group (`CR-DOCKER-HATH0R-GROUP-001`) for local suite runtime.

| Artifact | Canonical value |
|----------|-----------------|
| Compose project (Docker Desktop group) | `hath0r` |
| Network | `hath0r-net` |
| Membership scope | All repos under the `OpenSource` workspace folder |
| Shared edge | `hath0r-nginx` → host `localhost:38000` |
| Shared state | `hath0r-redis` (internal `redis://hath0r-redis:6379`) |
| Database (optional profile) | `hath0r-postgres` → host `localhost:35432` |
| MCP (standalone member) | `hath0r-mcp` from sibling `../hath0r-mcp` |

All Hath0r containers MUST use `name: hath0r` so they appear in one Docker group. No per-repo alternate project names for suite peers.

## Quick start

```bash
cd /Users/raybayly/Development/OpenSource/hath0r-atc
make docker-up          # hath0r-redis + hath0r-nginx
make docker-up-db       # + hath0r-postgres
make docker-status
make smoke
```

## Routes (hath0r-nginx)

| Path | Upstream |
|------|----------|
| `/healthz` | edge self-check |
| `/` | edge banner |
| `/mcp/` | `hath0r-mcp:8083` (when standalone MCP is running) |

## Naming rule

- Images: `hath0r/{component}:tag`
- Labels: `com.hath0r.org`, `com.hath0r.project=hath0r-opensource`, `com.hath0r.component`, `com.hath0r.container`

## MCP member (standalone)

`../hath0r-mcp` owns service `hath0r-mcp`, image `hath0r/mcp:local`, on external `hath0r-net`.

```bash
# From ATC root — start shared edge/state first
make docker-up
# Then start MCP from its own repo (do not lifecycle-manage from ATC compose)
make -C ../hath0r-mcp docker-up
make -C ../hath0r-mcp smoke
```

ATC never tears down MCP. MCP never tears down shared ATC infra. Stop MCP only with its scoped `docker-stop`.

## Full documentation

[`../../docs/deployment-local-docker.md`](../../docs/deployment-local-docker.md)

## Suite template pointer

- ATC cfg pointer: [`../../cfg/docker/groups/hath0r/README.md`](../../cfg/docker/groups/hath0r/README.md)
- Control-tower standard: https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/docker-group-standard.md
- Control-tower template: https://github.com/Bayly-AI/HATH0R-CLI/tree/development/cfg/docker/groups/hath0r
- Suite hub: [`../../docs/governance/SUITE_STANDARDS.md`](../../docs/governance/SUITE_STANDARDS.md)
