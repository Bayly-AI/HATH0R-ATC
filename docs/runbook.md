# Runbook: HATH0R ATC (Control Tower)

> Canonical operations runbook for **HATH0R ATC**.  
> Satisfies Hath0r initialization gate **CR-HATH0R-INIT-001**.  
> Tech family: Docker Compose control tower / suite infrastructure (peer: 1-Nation ATC).

---

## 1. Overview

HATH0R ATC is the **infrastructure**, **observation**, and **central group controller** for the OpenSource Project (`hath0r-opensource`).

| Responsibility | Owned here |
|----------------|------------|
| Docker group `hath0r` + network `hath0r-net` | Yes |
| Shared edge `hath0r-nginx` + state `hath0r-redis` | Yes |
| Optional `hath0r-postgres` | Yes (profile `db`) |
| MCP service process | **No** — standalone `../hath0r-mcp` |
| Operator CLI binary `hath0r` | **No** — `../hathor-cli` |
| Framework application code | **No** — `../hath0r` (supported by this tower) |

---

## 2. Prerequisites

- Docker Desktop (or Engine + Compose v2)
- `make`, `curl`, `bash`
- Optional: `hath0r` CLI on PATH for doctor/bootstrap
- No conflicting listeners on `:38000` / `:35432`

---

## 3. Install / bootstrap

```bash
cd /Users/raybayly/Development/OpenSource/hath0r-atc
cp .env.example .env   # optional overrides
./bin/hath0r-bootstrap.sh
```

---

## 4. Local Docker operations

```bash
make docker-up        # redis + nginx
make docker-up-db     # + postgres
make docker-status
make smoke
make docker-logs      # follow
make docker-down      # stop ATC stack; keep volumes
```

Manual equivalents:

```bash
docker network inspect hath0r-net >/dev/null 2>&1 || docker network create hath0r-net
docker compose -f deploy/docker/docker-compose.yml up -d redis nginx
./deploy/docker/smoke-test.sh
```

---

## 5. Standalone MCP (sibling)

```bash
# Shared infra first
make docker-up
# MCP owns its own compose lifecycle
make -C ../hath0r-mcp docker-up
make -C ../hath0r-mcp smoke
curl -fsS http://127.0.0.1:38000/mcp/health
```

Never `docker compose down --remove-orphans` against the shared `hath0r` project from a member repo in a way that removes ATC shared services unless you intend a full suite teardown from ATC.

---

## 6. Quality / verification

| Check | Command |
|-------|---------|
| Layout bootstrap | `make bootstrap` |
| Edge health | `curl -fsS http://127.0.0.1:38000/healthz` |
| Group smoke | `make smoke` |
| Network | `docker network inspect hath0r-net` |
| Group listing | `docker ps -a --filter label=com.docker.compose.project=hath0r` |

---

## 7. Deploy / rollback (local)

- **Deploy**: `make docker-up` (and optional `docker-up-db` / MCP up).
- **Rollback**: `make docker-down` then re-up previous known-good images/tags.
- **Data**: Redis volume `hath0r_redis_data` and external Postgres volume `hath0r_postgres_data` are retained on `down`. Destroy only with explicit `docker volume rm`.

Production cloud hosting is out of scope for this local tower runbook.

---

## 8. Promotion path (CR-BAI-001 / CR-BRANCH-GOV-001)

```text
local → development → testing → staging → master (Production)
```

- Issue first; branch from `development`.
- Feature PRs target `development` only.
- CI: `.github/workflows/enforce-promotion-path.yml`

---

## 9. Troubleshooting

| Symptom | Action |
|---------|--------|
| healthz fail | `make docker-status`; ensure nginx healthy |
| DNS alias missing | confirm container on `hath0r-net` |
| MCP 502 via edge | start `../hath0r-mcp`; check `docker inspect hath0r-mcp` |
| Port in use | `docker ps --filter publish=38000` |

---

## 10. Related

| Doc | Role |
|-----|------|
| [`deployment-local-docker.md`](deployment-local-docker.md) | Full deploy record |
| [`rules/cr-docker-hath0r-group-001.md`](rules/cr-docker-hath0r-group-001.md) | Docker membership rule |
| [`observe/README.md`](observe/README.md) | Observation surfaces |
| Setup playbook | `../hathor-cli/docs/hathor-playbook-001-repo-init-setup-20260919.md` |
| Peer ATC | `/Users/raybayly/Development/1-Nation/ATC` |
