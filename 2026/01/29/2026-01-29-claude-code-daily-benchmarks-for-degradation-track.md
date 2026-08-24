# Claude Code daily benchmarks for degradation tracking

- Score: 507 | [HN](https://news.ycombinator.com/item?id=46810282) | Link: https://marginlab.ai/trackers/claude-code/

### TL;DR

Marginlab’s independent tracker runs Claude Code with Opus 4.5 daily on 50 contamination-resistant SWE-Bench-Pro tasks, using no custom harness. On January 29 it reported a 58% historical baseline, 50% latest-day pass rate, 53% across seven days, and 54% across 30 days; only the 30-day decline was labeled statistically significant. A Claude Code team member said a harness issue introduced January 26 was rolled back January 28. Commenters challenge the sample size and significance method, warning against interpreting fluctuations as model substitution.

### Comment pulse

- A SWE-bench co-author recommends 300 tasks and multiple daily runs → 50 leaves load, sampling, and within-day variance unresolved.
- Statistical critique targets the comparison method → both baseline and new measurements have uncertainty, so intervals should cover their difference.
- Users report subjective slowdowns and speedups → theories include A/B tests and resource load, but evidence remains speculative.

### LLM perspective

- View: The tracker detects user-visible regressions across model and CLI together; it cannot identify which component changed.
- Impact: Independent monitoring can pressure hosted coding vendors to disclose incidents and maintain stable service quality.
- Watch next: Confirm post-rollback recovery, publish test formulas, and expand runs across tasks and times of day.
