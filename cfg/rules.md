# Configuration Subsystem — Local Rules & Constraints

> Constraints and schema requirements for HATH0R-ATC configurations.

## Rules

1. **Schema Validation**: All YAML files must parse cleanly and match their respective schema definitions.
2. **Hidden Root Pointer**: Suite configurations must reference `.hath0r/` only (`cr-hath0r-root-001`).
3. **No Secret Storage**: Secrets must be stored outside git in `/Users/raybayly/Development/.credentials/`.
4. **Member Immutability**: Changes to `cfg/suite.yaml` or `cfg/products.yaml` require approval by CODEOWNERS.
