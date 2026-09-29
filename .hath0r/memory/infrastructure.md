# Infrastructure Topology — HATH0R ATC

## Containers & Ports

| Service | Container | Internal Port | Host Port | Network | Role |
|---|---|---|---|---|---|
| Ingress Edge | `hath0r-nginx` | 80 | `38080` | `hath0r-net` | Reverse proxy edge |
| State Cache | `hath0r-redis` | 6379 | `38079` | `hath0r-net` | Shared session / lock cache |
| Knowledge MCP | `hath0r-mcp` | 8083 | `38083` | `hath0r-net` | Standalone FastMCP server |

## Operational Lifecycle
- Up: `make docker-up`
- Down: `make docker-down`
- Status: `make docker-status`
- Smoke: `make smoke`
