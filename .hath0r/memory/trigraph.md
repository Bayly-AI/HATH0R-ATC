# Tri-Graph Substrate — HATH0R ATC

The Tri-Graph architecture for HATH0R-ATC bridges static infrastructure definitions with dynamic agent execution state:

1. **KnowledgeGraph (AST & Lineage)**:
   - Indexes Docker compose models, NGINX routing maps, YAML schemas, and diagnostic playbooks.
   - Pinned schema definitions in `contracts/`.
2. **ContextGraph (Subsystem Topology)**:
   - Localized context boundaries across 7 subsystems: `deploy/`, `contracts/`, `cfg/`, `docs/`, `tests/`, `lib/`, `site/`.
   - Hierarchical traversal rooted at `AGENTS.md`.
3. **MemoryGraph (Working Memory Space)**:
   - Persisted under `.hath0r/memory/` (`architecture.md`, `core_rules.md`, `trigraph.md`, `infrastructure.md`).
   - Accessible via `hath0r memory read <topic>`.
