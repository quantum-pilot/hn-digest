# Openrouter Fusion API

- Score: 196 | [HN](https://news.ycombinator.com/item?id=48537641) | Link: https://openrouter.ai/openrouter/fusion

### TL;DR

OpenRouter’s Fusion runs a prompt through several models in parallel with web search and fetch enabled, then asks a judge model to map consensus, contradictions, gaps, and unique insights before producing one answer. Users can choose Quality or Budget presets or replace both panel and judge; billing sums every completion. HN discussion questioned whether judges select truth or merely familiar answers, arguing gains may come mostly from extra test-time sampling. Reported tradeoffs included stronger benchmark results, but roughly 7× latency and 4× cost in one informal evaluation.

### Comment pulse

- Verifiability determines value → résumé scoring benefited from comparison against source documents, while ambiguous trading reviews added caution and latency.
- Diversity may be secondary → repeated samples from one model also improved results — counterpoint: mixing models yielded a smaller additional benchmark gain.
- Evaluation prompts need two axes → separating truth from usefulness reduces nitpicks and helps distinguish valid criticism from changes worth making.

### LLM perspective

- **View:** Fusion is best understood as configurable test-time compute with structured adjudication, not guaranteed independent expert wisdom.
- **Impact:** High-stakes research gains broader coverage; routine prompts incur unnecessary expense, delay, and another model’s biases.
- **Watch next:** Demand task-specific evaluations comparing self-consistency, heterogeneous panels, longer reasoning, iterative agents, and distillation at equal cost and latency.
