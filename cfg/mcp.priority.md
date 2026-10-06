# MCP configuration priority (ATC)

Canonical policy: [HATH0R-CLI mcp-configuration.md](https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/mcp-configuration.md).

## Priority order (highest first)

1. **Project MCP** — control-tower `cfg/mcp.servers.json`  
   https://github.com/Bayly-AI/HATH0R-CLI/blob/development/cfg/mcp.servers.json  
   Local: `/Users/raybayly/Development/OpenSource/hathor-cli/cfg/mcp.servers.json`
2. **Group / org MCP** — suite or org defaults (after project)
3. **User / client MCP** — editor or personal MCP last

## ATC notes

- ATC is **not** the standalone MCP process owner — that is `hath0r-mcp` on `hath0r-net`.
- Docs publish path remains `cfg/mcp-doc-publish.json` + CLI `scripts/publish-docs-to-mcp.py` when present.
- Secrets for MCP auth: env refs under `/Users/raybayly/Development/.credentials/<service>/.env` only.

Issue: #8
