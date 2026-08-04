# Model Training as Code

- Score: 178 | [HN](https://news.ycombinator.com/item?id=48673450) | Link: https://aleph-alpha.com/en/blog/model-training-as-code/

### TL;DR

Aleph Alpha’s Savanna turns pretraining, supervised fine-tuning, reinforcement-learning, and evaluation pipelines into version-controlled imperative code. Typed stages compose into one-click hermetic runs; immutable datasets, tokenizers, checkpoints, configs, logs, and metrics preserve lineage, while input hashing and caching avoid duplicate sweep work. Pull requests run a sub-five-minute end-to-end test, nightly jobs catch capability regressions, and Flyte on Kubernetes handles execution. HN welcomed reproducibility but questioned its novelty beyond existing workflow systems.

### Comment pulse

- Organization is the bottleneck → pipelines reduce handoff errors and forgotten experiments, but commenters said culture must align tooling, training, and product around repeatable improvement.
- Savanna is not another executor → its domain-specific composability and lineage layer delegates durable scheduling, retries, caching, and visualization to Flyte.
- Strict identity enables reuse → hashing code, images, environments, configs, and inputs lets identical stages recover cached outputs, resembling Nix semantics.

### LLM perspective

- **View:** The important artifact is no longer a checkpoint alone, but the executable process that can regenerate and explain it.
- **Impact:** Specialists can own capabilities end to end instead of optimizing isolated stages that fail after infrequent handoffs.
- **Watch next:** Measure cache correctness, reuse, GPU idle time, rollback speed, cross-team contributions, and whether nightly gains survive full-scale training.
