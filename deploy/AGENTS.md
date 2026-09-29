# AGENTS.md — Deploy Subsystem (HATH0R-ATC)

> Hyper-context node for **HATH0R ATC Deployment & Infrastructure Subsystem**.
> Parent Node: [`../AGENTS.md`](../AGENTS.md)

## Subsystem Identity & Role

| Field | Value |
|---|---|
| Subsystem | `deploy` |
| Scope | Docker Compose, NGINX Edge Ingress, Redis Shared State, Local Network (`hath0r-net`) |
| Docker Group | `hath0r` |
| External Network | `hath0r-net` (Subnet: `172.38.0.0/16` / standard bridge) |
| Local Port Mapping | `38xxx` range |

## Operational Guidelines

1. **Docker Group Membership (`CR-DOCKER-HATH0R-GROUP-001`)**: All services managed by or joining ATC must belong to the `hath0r` Docker group.
2. **Edge Proxy**: NGINX acts as the reverse proxy edge (`deploy/docker/nginx.conf`) routing requests across OpenSource services.
3. **State Management**: Shared Redis instance (`hath0r-redis`) manages suite session cache and distributed locks.
4. **Secrets Isolation**: No secret injection into git; utilize external credentials under `/Users/raybayly/Development/.credentials/`.

## Key Files & Direct Links

- [docker-compose.yml](file:///Users/raybayly/Development/OpenSource/hath0r-atc/deploy/docker/docker-compose.yml): Canonical multi-container infrastructure specification.
- [nginx.conf](file:///Users/raybayly/Development/OpenSource/hath0r-atc/deploy/docker/nginx.conf): Reverse proxy edge configuration for port routing.
- [rules.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/deploy/rules.md): Deployment and container security rules.
- [canonical.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/deploy/canonical.md): Canonical reference for Docker network and container labels.
