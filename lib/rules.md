# Library Subsystem — Local Rules & Constraints

> Constraints and standards for shared code in HATH0R-ATC.

## Rules

1. **Modularity**: Functions should be single-purpose and type-annotated (`from __future__ import annotations`).
2. **Error Handling**: Raise explicit exception types rather than broad `Exception`.
3. **No Direct Secret Access**: Accept credentials via configuration objects or function arguments.
