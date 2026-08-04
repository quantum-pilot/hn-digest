# Running local models is good now

- Score: 954 | [HN](https://news.ycombinator.com/item?id=48555993) | Link: https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/

### TL;DR

On a 2022 M2 Mac with 64 GB RAM, the author says Gemma 4 and GPT-OSS have moved local models from novelty to useful development assistants. Gemma 4 agent loops feel 75% as capable and fast as frontier services for refactors, tests, proofreading, and repository bootstrapping. Her Pi-plus-LM Studio setup runs inside a restricted Docker container, but remains experimental: inference is slower, context consumes memory, and templates can break. HN experiences varied sharply by hardware, quantization, task, and expectations; some daily-drive Qwen, while others still prefer cheap frontier subscriptions.

### Comment pulse

- Hardware dominates experience → dense models are smart but slow; MoE models are faster but error-prone, while insufficient memory bandwidth makes both frustrating.
- Quantization is not free → 4-bit weights can weaken tool use; experienced users recommend roughly 5-bit dense and 6-bit MoE configurations.
- Ownership has nonfinancial value → local users gain privacy, stable behavior, no quotas, and inspectability — counterpoint: cloud subscriptions remain cheaper and stronger.

### LLM perspective

- **View:** Local inference has crossed a usefulness threshold, not a frontier-parity threshold; narrowly scoped automation is its strongest fit.
- **Impact:** Teams can route private, repetitive work locally while reserving expensive APIs for ambiguous reasoning and large changes.
- **Watch next:** Benchmark quality per watt, quantization-induced tool errors, long-context degradation, diffusion-model throughput, and total ownership cost.
