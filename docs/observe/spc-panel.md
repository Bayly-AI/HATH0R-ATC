# SPC status panel (Bayly-AI/HATH0R-CLI#594)

ATC is the place operators check suite health, so it carries the statistical process control (SPC) panel.
ATC only observes. The charts and capability come from `spc-monitor-bot` in HATH0R-CLI, and the panel
reads them through the CLI or the read-only HATH0R-MCP tool. Configuration:
[`cfg/observability/spc-panel.json`](../../cfg/observability/spc-panel.json).

## Read the panel

```sh
make observe-spc                       # hath0r spc status for the current workspace
hath0r -o json spc status              # same, as JSON (contract hath0r-spc-chart-v1)
hath0r spc chart -m r_task             # one chart: I-MR limits, Western Electric rules, EWMA, CUSUM
hath0r andon status                    # any stop that is holding workflows
```

From an MCP client, call `quality_spc_status` (optionally with `metric`) on `hath0r-mcp`, and
`andon_status`, `evals_msa_report`, `fmea_query` for the related views.

## What the colours mean

| Colour | Condition | What to do |
|---|---|---|
| Green | Every metric in control and R_task Cpk at least 1.33 | Nothing |
| Amber | Provisional limits (fewer than 20 points), a rule signal, or Cpk below 1.33 | A warning (validated 2026-11-11). Find the assignable cause; see the CLI SPC playbook |
| Red | Out of control with `capability.mode: block`, or an active Andon stop | Workflows are held. `hath0r andon status`, fix, then `hath0r andon ack` and `clear` |

Capability is R_task against the eval threshold (LSL 0.80, one-sided). The goal is R_task as close to
1.0 as possible; anything under the threshold is a failed eval.

## Metrics

R_task, the four tier scores, eval duration, total tokens, cost and latency. Limits are frozen per
metric with `hath0r spc baseline -m <metric> [--recent]` in the CLI workspace.
