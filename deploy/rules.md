# Deploy Subsystem — Local Rules & Constraints

> Constraints and governance for Docker infrastructure in HATH0R-ATC.

## CR-DOCKER-HATH0R-GROUP-001 Constraints

1. **Group Name**: Top-level compose `name:` must always be `hath0r`.
2. **Network Policy**: Use external bridge network `hath0r-net`. Never create unattached isolated networks for suite members.
3. **Container Naming**: Canonical container names: `Hath0r-Edge` (edge), `Hath0r-Sessions` (redis), `Hath0r-Data` (postgres), `Hath0r-phoenix` (phoenix), `Hathor-MLFLOW` (mlflow), `Hath0r-MCP` (mcp). Legacy `hath0r-*` network aliases are maintained for backwards compatibility.
4. **Mandatory Labels**:
   - `com.hath0r.org=bayly-ai`
   - `com.hath0r.project=hath0r-opensource`
   - `com.hath0r.component=<component_name>`
   - `com.hath0r.container=<container_name>`
5. **Security Constraints**:
   - Non-root user execution whenever possible.
   - Read-only root filesystem (`read_only: true`) with explicit temporary volume mounts.
   - Drop all unnecessary Linux capabilities (`cap_drop: [ALL]`).
   - `security_opt: [no-new-privileges:true]`.
