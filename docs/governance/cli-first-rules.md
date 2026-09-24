# CLI-first rules (ATC pointer)

Canonical: [HATH0R-CLI cli-first-rules.md](https://github.com/Bayly-AI/HATH0R-CLI/blob/development/docs/governance/cli-first-rules.md).

## ATC application

For connections, MCP orientation, workflows/factories, Docker workflows, KB path, or suite orientation:

1. Prefer the **`hath0r`** operator CLI (`../hathor-cli`) when installed.
2. Prefer ATC **Make** targets for Docker group lifecycle (`make docker-up`, `make smoke`).
3. Avoid inventing parallel ad-hoc scripts that bypass CLI/ATC entrypoints.

See also `AGENTS.md` § CLI-first (`cr-cli-first-001`).

Issue: #14
