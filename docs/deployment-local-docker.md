# Deployment — Hath0r local Docker group

Local suite runtime for the **OpenSource Project**, owned by **Hath0r ATC**: one Docker Compose project, one network, shared edge (NGINX) and shared state (Redis). MCP remains a **standalone** sibling that joins the same network.

| Field | Value |
|-------|-------|
| Status | **Scaffolded (local)** · **CANONICAL** |
| Documented | 2026-09-23 |
| Rule | `CR-DOCKER-HATH0R-GROUP-001` |
| Compose project | `hath0r` |
| Network | `hath0r-net` |
| Workspace root | `/Users/raybayly/Development/OpenSource` (ATC at `hath0r-atc/`) |
| GitHub | [Bayly-AI/HATH0R-ATC](https://github.com/Bayly-AI/HATH0R-ATC) |
| Membership scope | **All repos under the workspace root** |
| Canonical compose | `hath0r-atc/deploy/docker/docker-compose.yml` |
| Ops entry | `cd hath0r-atc && make docker-up` |

## Canonical membership (CRITICAL)

**Every repository under `/Users/raybayly/Development/OpenSource` is part of the `hath0r` Docker group** for local suite runtime. Product git remotes may differ; Docker project name does **not**.

Policy: [`docs/rules/cr-docker-hath0r-group-001.md`](rules/cr-docker-hath0r-group-001.md) · [`AGENTS.md`](../AGENTS.md)

## Purpose

1. Keep **all** Hath0r containers—from **all** OpenSource repos—in a single Docker group (`com.docker.compose.project=hath0r`).
2. Always launch shared **communication** (`hath0r-nginx`) and **state** (`hath0r-redis`) from ATC.
3. Keep **MCP standalone** — lifecycle in `hath0r-mcp`, network join only.
4. Support **framework** development (`hath0r`) with shared infra without coupling app code into ATC.

## Architecture

```text
Host browser / curl
  → hath0r-nginx :38000     (suite edge, reverse proxy)
       ├─ /healthz          (edge self-check)
       └─ /mcp/*          → hath0r-mcp:8083   (standalone member)

hath0r-net
  ├── hath0r-nginx
  ├── hath0r-redis         (redis://hath0r-redis:6379 — AOF volume hath0r_redis_data)
  ├── hath0r-postgres      (:35432 host → 5432, volume hath0r_postgres_data) [profile db]
  └── hath0r-mcp           (standalone compose from ../hath0r-mcp)
```

## Canonical naming (mandatory)

| Artifact | Value |
|----------|--------|
| Compose `name:` | `hath0r` |
| Network | `hath0r-net` (external) |
| Images | `hath0r/{component}:tag` |
| Containers | `hath0r-nginx`, `hath0r-redis`, `hath0r-postgres`, `hath0r-mcp`, … |
| Labels | `com.hath0r.org=bayly-ai`, `com.hath0r.project=hath0r-opensource`, `com.hath0r.component`, `com.hath0r.container` |

## Layout

```text
/Users/raybayly/Development/OpenSource/
  hath0r-atc/                    # THIS REPO — control tower
    Makefile
    cfg/
    deploy/docker/
    docs/
  hath0r-mcp/                    # standalone MCP member
  hathor-cli/                    # operator CLI
  hath0r/                        # framework (supported by ATC+MCP)
  hath0r-poc/                    # archived optional fixture
```

## Profiles

| Make target | Compose | Containers |
|-------------|---------|------------|
| `make docker-up` | default | `hath0r-redis`, `hath0r-nginx` |
| `make docker-up-db` | `--profile db` | + `hath0r-postgres` |
| `make docker-down` | down | stops ATC stack; **keeps** named volumes |

## Host ports

| Service | Host port | Container | Notes |
|---------|-----------|-----------|--------|
| hath0r-nginx | `38000` (`HATH0R_NGINX_HOST_PORT`) | `80` | Suite edge |
| hath0r-postgres | `35432` (`POSTGRES_HOST_PORT`) | `5432` | Optional db profile |
| hath0r-redis | _(not published)_ | `6379` | Reach only on `hath0r-net` |
| hath0r-mcp | `38083` (MCP repo) | `8083` | Standalone member |

Port range `38xxx` avoids collision with 1-Nation suite (`58xxx`).

## Operator quick start

```sh
cd /Users/raybayly/Development/OpenSource/hath0r-atc
make docker-up
make docker-status
make smoke

# Optional standalone MCP
make -C ../hath0r-mcp docker-up
make smoke   # now includes /mcp/health when MCP is up
```

## Adding a new Hath0r service

1. Use compose top-level `name: hath0r`.
2. Set `container_name` to the registry name (`hath0r-<component>`).
3. Attach to external network `hath0r-net` with stable aliases.
4. Apply `com.hath0r.*` labels.
5. Prefer Redis at `redis://hath0r-redis:6379/<db>` and Postgres at `hath0r-postgres:5432`.
6. If HTTP, add an upstream + `location` under `deploy/docker/nginx/conf.d/default.conf`.
7. Re-run `./deploy/docker/smoke-test.sh`.

## Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Containers missing from Docker Desktop group | Compose `name` not `hath0r` | Fix compose; recreate |
| NGINX 502 on `/mcp/` | MCP not running | `make -C ../hath0r-mcp docker-up` |
| Redis connection refused | Wrong host or network | Use `hath0r-redis`; confirm `hath0r-net` |
| Port already allocated | Stale container / host process | `docker ps -a`; free `:38000` |

## See also

- `deploy/docker/README.md` — short ops card
- `docs/runbook.md` — tech runbook (CR-HATH0R-INIT-001)
- `docs/observe/README.md` — observation surfaces
- Sibling MCP: `../hath0r-mcp`
