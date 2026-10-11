# Canonical Architecture — HATH0R ATC (Control Tower)

The **HATH0R-ATC** repository serves as the canonical **Infrastructure Control Tower**, **Observation Hub**, and **Central Group Controller** for the `hath0r-opensource` suite.

## Core Topology
- **Edge Routing**: NGINX reverse proxy (`deploy/docker/nginx.conf`) exposed on host port `38080`.
- **State Layer**: Redis cache & lock engine (`hath0r-redis`) exposed on host port `38079`.
- **Network**: External bridge network `hath0r-net` (`172.38.0.0/16`).
- **Tri-Graph Substrate**: Integrated KnowledgeGraph (AST/lineage), ContextGraph (subsystems), and MemoryGraph (`.hath0r/memory/`).
