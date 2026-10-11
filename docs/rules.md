# Documentation Subsystem — Local Rules & Constraints

> Constraints and formatting standards for documentation in HATH0R-ATC.

## Rules

1. **Taxonomy Discipline**: Structure documentation according to canonical hierarchy: Playbook (troubleshooting/triage) → Procedure (step-by-step operation) → Runbook (lifecycle/service ops).
2. **Path Pointers**: Relative links must use markdown format and valid file targets.
3. **Redaction**: Never write plain text tokens, API keys, or private SSH keys into markdown files.
4. **Header Consistency**: Markdown documents must include front-matter or initial block summary with document ownership and status.
