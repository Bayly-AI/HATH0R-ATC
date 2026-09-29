# Tests Subsystem — Local Rules & Constraints

> Constraints and requirements for tests in HATH0R-ATC.

## Rules

1. **State Cleanliness**: Tests must not leave dangling temporary containers or untracked test fixtures.
2. **Network Isolation**: Tests asserting Docker connectivity must verify `hath0r-net` availability before sending traffic.
3. **Exit Code Validation**: Smoke and bootstrap scripts must exit with code 0 on success and non-zero on error.
