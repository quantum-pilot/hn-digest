# Claude Code daily benchmarks for degradation tracking

- Score: 507 | [HN](https://news.ycombinator.com/item?id=46810282) | Link: https://marginlab.ai/trackers/claude-code/

### TL;DR
Marginlab’s new dashboard tracks Claude Code Opus 4.5 on a daily subset of SWE-Bench-Pro to flag statistically significant degradations. It reports a 58% historical pass-rate baseline and a current 30‑day rate of 54%, a roughly 4‑point regression deemed significant. Benchmarks are run through the public Claude Code CLI and modeled as Bernoulli trials with confidence intervals. HN discussion probes sampling size and statistical validity, Anthropic’s admitted harness bug, infrastructure/load effects, and whether oscillations reflect true downgrades, A/B tests, or randomness.

### Comment pulse
- Small N=50 daily subset makes results noisy; SWE-bench author urges 300 tasks, multiple runs; others note cost, suggest Anthropic funding independent monitoring.  
- Anthropic engineer blames briefly-broken Claude Code harness, rolled back; users demand token compensation, clearer postmortem, and assurances about internal regression and safety monitoring.  
- Some doubt model downgrades, citing oscillations, A/B tests, and load-based inference knobs; statisticians challenge confidence-interval method; many report big speed swings when traffic drops.

### LLM perspective
- View: Public, continuous third-party benchmarks help distinguish real regressions from random variance and rumors about silent model downgrades.  
- Impact: Robust trackers pressure providers to maintain quality, document changes, and quickly acknowledge or fix harness, deployment, or infrastructure issues.  
- Watch next: Standardize task sets and timing, publish statistical methods, and benchmark multiple models to isolate model vs tooling regressions.
