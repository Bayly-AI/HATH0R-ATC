# Contracts Subsystem — Local Rules & Constraints

> Constraints and schema governance for HATH0R-ATC.

## Rules

1. **Envelope Conformance**: Output responses must validate against `hath0r-cli-response-v1.schema.json`.
2. **Schema Mutability**: Do NOT edit schema definitions directly in member repos without syncing from `Bayly-AI/HATH0R-Agentic-Framework/lib/schemas`.
3. **Exit Code Validation**: Tools must return exit codes specified in `contracts/exit-codes.yaml`.
4. **No Undocumented Extensions**: Unknown payload properties must be declared or rejected per strict JSONSchema standards.
