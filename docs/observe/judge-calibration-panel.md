# Judge calibration panel (Bayly-AI/HATH0R-ATC#88, epic Bayly-AI/HATH0R-CLI#610)

Gage R&R treats the eval gauge as one instrument with the same behaviour at every complexity level.
LLM judges do not behave like that: a judge can be fair on small changes and lenient on large ones.
HATH0R-CLI therefore calibrates every judge with a many-facet Rasch model (Study B) and certifies or
removes it per complexity level. ATC shows the result. It only observes; the numbers come from
`judge-calibration-bot` in HATH0R-CLI. Configuration:
[`cfg/observability/judge-calibration-panel.json`](../../cfg/observability/judge-calibration-panel.json).

## Read the panel

```sh
make observe-judges                      # hath0r evals judges report + status
hath0r -o json evals judges report       # latest study (contract hath0r-judge-calibration-v1)
hath0r evals judges status claude-opus --level L4   # may this judge be used at L4?
hath0r spc chart -m judge_severity@claude-opus:L4   # the judge's bias at L4 across studies
hath0r spc chart -m r_task --level L4               # R_task of L4 changes only
```

From an MCP client, call `evals_judge_calibration_report` on `hath0r-mcp`.

## What the colours mean

| Colour | Status | Meaning |
|---|---|---|
| Green | `certified` | Bias at this level is under 0.20 logits or not significant, fit is fine, and the estimate is precise (SE at most 0.10). Use the judge here. |
| Amber | `not_certified` | Not enough information to decide (SE above 0.10, too few items, every rating in one category, or no anchor). Do not rely on the judge here yet. |
| Red | `removed_bias` / `removed_noise` | A significant bias of at least 0.20 logits (Benjamini-Hochberg q 0.05), or misfit above 1.5 mean-square. Do not use the judge at this level. |

Cut-offs were approved by Ray on 2026-11-16. There is no score adjustment: a judge is used only where
it is certified, and scorecards refuse an uncertified LLM judge (`judge_calibration.enforce`).

## Levels

Code changes use L1 (trivial) to L5 (system), from `cfg/evals/complexity-levels.yaml` in HATH0R-CLI.
JEV tool-guard decisions use risk levels R1 to R5. Reasoning judges use Commons' Model of Hierarchical
Complexity orders 6 to 12.
