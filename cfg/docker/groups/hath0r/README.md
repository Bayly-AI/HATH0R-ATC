# Docker group `hath0r` — ATC ownership + template pointer

ATC is the **canonical runtime owner** of the OpenSource `hath0r` Docker group
(`CR-DOCKER-HATH0R-GROUP-001`).

## Runtime (this repo)

| Artifact | Path |
|----------|------|
| Compose + NGINX + Makefile | [`../../../deploy/docker/`](../../../deploy/docker/) |
| Operator README | [`../../../deploy/docker/README.md`](../../../deploy/docker/README.md) |
| Deploy record | [`../../../docs/deployment-local-docker.md`](../../../docs/deployment-local-docker.md) |
| Rule | [`../../../docs/rules/cr-docker-hath0r-group-001.md`](../../../docs/rules/cr-docker-hath0r-group-001.md) |

Canonical values: compose `name: hath0r`, network `hath0r-net`, edge `hath0r-nginx`, state `hath0r-redis`.

## Suite template (control tower)

Shared template / workflow definitions for member repos:

- Standard: https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/docker-group-standard.md
- Template tree: https://github.com/Bayly-AI/HATH0R-CLI/tree/development/cfg/docker/groups/hath0r
- Local CLI path: `/Users/raybayly/Development/OpenSource/hathor-cli/cfg/docker/groups/hath0r`

Member products should **not** invent alternate compose project names. Prefer joining
`hath0r-net` and using ATC shared edge/state; point docs here + CLI template.

## Operator entry

```bash
cd /Users/raybayly/Development/OpenSource/hath0r-atc
make docker-up
make docker-status
make smoke
```

Issues: #16 · #9
