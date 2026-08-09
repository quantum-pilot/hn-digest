# Lambda Calculus Benchmark for AI

- Score: 128 | [HN](https://news.ycombinator.com/item?id=47900506) | Link: https://victortaelin.github.io/lambench/

### TL;DR

λ-bench tests models on 120 pure lambda-calculus programming tasks in Lamb: each receives encodings, a specification, and tests, then must return one `@main` program that passes every case. GPT-5.4 leads the posted table at 110/120, narrowly ahead of Opus 4.6 at 108 and GPT-5.3 Codex at 107; many cheaper or local models trail sharply. HN liked the unfamiliar, encoding-heavy domain but warned that single-attempt scores, unclear serving configurations, and duplicate model labels make broad intelligence or cost-quality conclusions unreliable.

### Comment pulse

- Repeated samples estimate within-task variability, but more distinct tasks are necessary to predict performance on future problems.
- Top models cluster closely — counterpoint: average coding may hide differences that emerge only on rare, difficult work.
- Pure encodings make algorithms like FFT structurally unlike mutable-array examples, testing derivation rather than surface translation.

### LLM perspective

- Publish prompts, model IDs, providers, quantization, sampling settings, token budgets, failures, and per-task outputs.
- Report pass@1 and pass@k with confidence intervals, latency, tokens, and cost.
- Maintain a hidden task set and rotate problems to reduce contamination from published solutions.
