# Real-SWE: Benchmarking AI models on private, real-world, enterprise codebases

- Score: 246 | [HN](https://news.ycombinator.com/item?id=49676820) | Link: https://withspecific.com/benchmarks/real-swe

### TL;DR

Real-SWE evaluates model-and-harness combinations on licensed private production codebases, using business tasks spanning billing, migrations, infrastructure, and company-specific conventions. Its creators report Fable 5.1 leading at 38.8% resolution, followed by GPT-6 Astra at 33.8%, with no model solving every task. Six of ten sampled tasks scored below 15%; missed requirements, unchecked assumptions, and integration errors dominated failures. Commenters value benchmarks grounded in their own repositories but question privacy, contamination, one-shot grading, and whether leaderboard rankings match daily experience.

### Comment pulse

- Private tasks improve realism → proprietary conventions and cross-service business rules test capabilities absent from isolated coding puzzles.
- Benchmark privacy remains uncertain → commenters question whether sending licensed code to model providers keeps it meaningfully private.
- Personal evaluations may be more actionable → teams can replay historical tickets against accepted changes and calibrate models to their workflows.

### LLM perspective

- View: The benchmark measures autonomous first-pass reliability, not the productivity of an expert steering agents through clarification and review.
- Impact: Enterprises gain evidence that current agents still need verification, especially around requirements, assumptions, and integration boundaries.
- Watch next: Publish task-selection bias, contamination checks, harness sensitivity, human-in-loop baselines, and confidence intervals for model comparisons.
