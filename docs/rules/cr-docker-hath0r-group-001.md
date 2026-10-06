---
id: cr-docker-hath0r-group-001
title: Canonical hath0r Docker group for all OpenSource workspace repos
version: 1.0.0
severity: CRITICAL
status: canonical
applies_to: "/Users/raybayly/Development/OpenSource/**"
effective_date: 2026-09-23
suite: hath0r-opensource
---

# CR-DOCKER-HATH0R-GROUP-001 — hath0r Docker group (CANONICAL)

## Rule statement

**Every repository, service, and container defined under the `OpenSource` workspace folder is a member of the Docker Compose project / Docker Desktop group `hath0r` for local suite runtime.**

This is **canonical** and not optional for local OpenSource suite runtime.

## Workspace root

```text
/Users/raybayly/Development/OpenSource
```

Includes (now and future):

- Control tower (`hath0r-atc/`)
- Standalone MCP (`hath0r-mcp/`)
- Operator CLI (`hathor-cli/`)
- Framework (`hath0r/`)
- Any additional clone under this directory

## Canonical artifacts

| Artifact | Value |
|----------|--------|
| Compose project name (`name:`) | `hath0r` |
| Docker Desktop group | `hath0r` |
| Network | `hath0r-net` (external, shared) |
| Shared communication | container `hath0r-nginx` |
| Shared state | container `hath0r-redis` |
| Image naming | `hath0r/{component}:tag` |
| Project label | `com.hath0r.project=hath0r-opensource` |
| Org label | `com.hath0r.org=bayly-ai` |

## Required compose skeleton

```yaml
name: hath0r

services:
  example:
    image: hath0r/example:local
    container_name: hath0r-example
    networks:
      hath0r-net:
        aliases: [hath0r-example, h0-example]
    labels:
      com.hath0r.org: bayly-ai
      com.hath0r.project: hath0r-opensource
      com.hath0r.component: example
      com.hath0r.container: hath0r-example

networks:
  hath0r-net:
    name: hath0r-net
    external: true
```

## Shared stack ownership

Workspace-owned shared services live in ATC:

`hath0r-atc/deploy/docker/docker-compose.yml`

| Container | Role |
|-----------|------|
| `hath0r-nginx` | Suite edge / reverse proxy |
| `hath0r-redis` | Shared state / cache / coordination |
| `hath0r-postgres` | Canonical DB (profile `db`) |

Member repos **consume** these. MCP is **standalone**: it joins `hath0r-net` and uses compose project `hath0r`, but its process lifecycle is owned by `hath0r-mcp`.

## Non-compliance

Using a different compose project name for suite peers, a private-only network for suite peers, or omitting group labels for Hath0r containers is a **CRITICAL** violation of this rule.

## Verification

```sh
docker ps -a --filter label=com.docker.compose.project=hath0r \
  --format 'table {{.Names}}\t{{.Status}}\t{{.Label "com.docker.compose.project"}}'
docker network inspect hath0r-net
```

Every Hath0r suite container MUST appear with project `hath0r`.

## Related

- `AGENTS.md`
- `docs/deployment-local-docker.md`
- `deploy/docker/README.md`
- Peer rule: 1-Nation `cr-docker-1n-group-001`
