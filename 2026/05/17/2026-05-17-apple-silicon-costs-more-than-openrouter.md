# Apple Silicon costs more than OpenRouter

- Score: 290 | [HN](https://news.ycombinator.com/item?id=48168198) | Link: https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html

### TL;DR

A cost model for running Gemma 4 31B on a $4,299 M5 Max MacBook estimates roughly $0.40–$4.79 per million tokens, driven mainly by hardware depreciation, versus $0.38–$0.50 through OpenRouter; hosted inference is also reported faster. HN disputed the assumptions: allocating an entire general-purpose laptop, using 10–40 tokens per second, and choosing Gemma may misstate incremental local cost. Commenters nevertheless accepted cloud’s utilization advantage, while emphasizing that privacy, offline operation, model permanence, predictable billing, and existing hardware can justify local inference.

### Comment pulse

- Depreciation should be incremental → compare the premium over the laptop someone would buy anyway, including resale — counterpoint: dedicated hardware warrants full allocation.

- Benchmark inputs may be cherry-picked → users reported 95–100 tokens per second on M5 Max and recommended newer, smaller Qwen models.

- Hybrid operation dominates absolutes → cloud offers efficient scale and frontier quality; local models preserve privacy, offline access, continuity, and cost ceilings.

### LLM perspective

- **View:** Self-hosting economics hinge on utilization and counterfactual hardware cost, while deployment choice also prices operational sovereignty.

- **Impact:** Individual developers usually save with hosted inference; regulated, disconnected, latency-sensitive, or service-continuity workloads may rationally pay a local premium.

- **Watch next:** Rebenchmark identical quantization, prompts, output lengths, batch sizes, power, utilization, resale, provider latency, and current local-model alternatives.
