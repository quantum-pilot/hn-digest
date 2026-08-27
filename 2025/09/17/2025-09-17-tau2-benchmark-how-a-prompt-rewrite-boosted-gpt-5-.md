# Tau² benchmark: How a prompt rewrite boosted GPT-5-mini by 22%

- Score: 179 | [HN](https://news.ycombinator.com/item?id=45275354) | Link: https://quesma.com/blog/tau2-benchmark-improving-results-smaller-models/

### TL;DR

Quesma reports that restructuring Tau² telecom policies into decision trees, explicit tool calls, prerequisites, error handling, and verification steps raised GPT-5-mini success from 55% to 67.5% across 40 simulations on 20 scenarios. Two-trial reliability rose from 40% to 50%, while always-failing tasks fell from six to three. HN readers wanted the exact prompt and policy diff, questioned result stability, and noted that Telecom’s outcome-based grading may be less brittle than the benchmark’s Airline and Retail domains.

### Comment pulse

- Clearer instructions resemble programming → explicit branches and invariants reduce ambiguity, but may require revision for every model generation.
- Benchmark interpretation matters → outcome-state grading permits valid alternative solutions, while zero partial credit can obscure near-successes.

### LLM perspective

- View: The experiment shows prompt structure can shift measured capability, but its small sample cannot establish broad generality.
- Impact: Teams may extract more reliability from cheaper models before paying for flagship inference.
- Watch next: Replication across seeds, full task sets, domains, models, and unchanged evaluation conditions.
