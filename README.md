# HATH0R-ATC

**Canonical control tower** for the OpenSource Project (`hath0r-opensource`) — infrastructure, observation, and Docker-group controller.

| Field | Value |
|-------|--------|
| GitHub | **[Bayly-AI/HATH0R-ATC](https://github.com/Bayly-AI/HATH0R-ATC)** |
| Local path | `/Users/raybayly/Development/OpenSource/hath0r-atc` |
| Default branch | `development` |
| Roles | **Infrastructure** · **Observation** · **Central group controller** |
| Docker group | `hath0r` on network `hath0r-net` |
| Config | [`cfg/control-tower.yaml`](cfg/control-tower.yaml), [`cfg/suite.yaml`](cfg/suite.yaml) |
| Agents | [`AGENTS.md`](AGENTS.md) |
| Runbook | [`docs/runbook.md`](docs/runbook.md) |
| Deploy record | [`docs/deployment-local-docker.md`](docs/deployment-local-docker.md) |

ATC and **MCP are standalone**. Together they support building the **HATHOR framework** (`../hath0r`). Operator CLI remains `hath0r` from `../hathor-cli`.

---

## OpenSource workspace layout

```text
/Users/raybayly/Development/OpenSource/
├── hath0r-atc/          # THIS REPO — control tower (git: Bayly-AI/HATH0R-ATC)
├── hath0r-mcp/          # Standalone MCP member
├── hathor-cli/          # Operator CLI (hath0r binary)
├── hath0r/              # Framework + docs corpus
└── hath0r-poc/          # Archived optional fixture
```

| Path | Role |
|------|------|
| `hath0r-atc/` | Infrastructure, observation, group controller |
| `hath0r-mcp/` | Standalone MCP on `hath0r-net` |
| `hathor-cli/` | `hath0r` operator CLI |
| `hath0r/` | Framework being built/supported |

**Do not** place suite `deploy/`, tower `cfg/`, or suite `docs/` at the OpenSource root. Those belong under `hath0r-atc/`.

### ATC repository layout

```text
hath0r-atc/
├── AGENTS.md
├── README.md
├── Makefile
├── bin/hath0r-bootstrap.sh
├── cfg/
│   ├── control-tower.yaml
│   ├── suite.yaml
│   ├── products.yaml
│   ├── product.yaml
│   └── knowledge-tower.yaml
├── deploy/docker/
│   ├── docker-compose.yml
│   ├── Makefile
│   ├── smoke-test.sh
│   ├── nginx/
│   └── README.md
├── docs/
│   ├── runbook.md
│   ├── deployment-local-docker.md
│   ├── observe/
│   ├── rules/
│   ├── reports/
│   └── archive/
└── site/                  # optional stubs only
```

---

## Roles

1. **Infrastructure** — owns `deploy/docker/` (`hath0r-nginx`, `hath0r-redis`, optional Postgres), `CR-DOCKER-HATH0R-GROUP-001`, suite network.
2. **Observation** — smoke/status baselines and archives (`docs/observe/`, `docs/archive/`, `docs/reports/`).
3. **Central group controller** — suite identity (`cfg/suite.yaml`), tower config (`cfg/control-tower.yaml`), membership policy for **all** repos under OpenSource.

Member remotes stay independent. **Docker group policy always resolves here.**

---

## Deployment procedures (local Docker)

```sh
cd /Users/raybayly/Development/OpenSource/hath0r-atc
```

### Profiles

| Make target | What starts |
|-------------|-------------|
| `make docker-up` | `hath0r-redis` + `hath0r-nginx` |
| `make docker-up-db` | shared + `hath0r-postgres` |
| `make docker-status` | network + group health + edge `/healthz` |
| `make smoke` | automated edge + Redis (+ MCP if up) |
| `make docker-down` | stop ATC stack; **named volumes retained** |

### Quick start

```sh
make docker-up
make docker-status
curl -fsS http://localhost:38000/healthz
docker exec hath0r-redis redis-cli ping
make smoke
```

### Standalone MCP

```sh
make docker-up
make -C ../hath0r-mcp docker-up
curl -fsS http://localhost:38000/mcp/health
```

### Host ports

| Container | Host | Notes |
|-----------|------|--------|
| `hath0r-nginx` | http://localhost:38000 | Suite edge |
| `hath0r-mcp` | http://localhost:38083 | Direct (MCP repo) |
| `hath0r-postgres` | localhost:35432 | Optional db profile |
| `hath0r-redis` | _(not published)_ | internal only |

Port range `38xxx` avoids collision with 1-Nation (`58xxx`).

### Canonical Docker rules

| Artifact | Value |
|----------|--------|
| Compose `name:` | `hath0r` |
| Network | external `hath0r-net` |
| Images | `hath0r/{component}:tag` |
| Labels | `com.hath0r.org`, `com.hath0r.project=hath0r-opensource`, component, container |

Policy: [`docs/rules/cr-docker-hath0r-group-001.md`](docs/rules/cr-docker-hath0r-group-001.md).

---

## Branch strategy

```text
feature/* → development → testing → staging → master (production)
```

See [`docs/rules/cr-branch-gov-001-canonical-branches.md`](docs/rules/cr-branch-gov-001-canonical-branches.md).

---

## Related docs

| Doc | Purpose |
|-----|---------|
| [`docs/runbook.md`](docs/runbook.md) | Ops runbook |
| [`docs/deployment-local-docker.md`](docs/deployment-local-docker.md) | Full local Docker record |
| [`docs/observe/README.md`](docs/observe/README.md) | Observation surfaces |
| [`AGENTS.md`](AGENTS.md) | Agent orientation |
| Peer reference | `/Users/raybayly/Development/1-Nation/ATC` |
