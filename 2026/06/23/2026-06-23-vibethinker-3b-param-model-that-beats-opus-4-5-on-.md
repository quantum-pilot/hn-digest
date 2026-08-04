# VibeThinker: 3B param model that beats Opus 4.5 on reasoning with novel SFT+GRPO

- Score: 373 | [HN](https://news.ycombinator.com/item?id=48639240) | Link: https://arxiv.org/abs/2606.16140

### TL;DR

VibeThinker-3B uses curriculum-based supervised fine-tuning, multi-domain reinforcement learning, and offline self-distillation to push a dense 3B-parameter model on verifiable reasoning. The report claims 94.3 on AIME26, 80.2 Pass@1 on LiveCodeBench v6, 96.1% acceptance on unseen LeetCode contests, and 93.4 on IFEval, rivaling much larger systems without losing instruction control. HN discussion welcomed efficient specialists but disputed whether closed-world benchmark wins justify comparisons with general models or predict real developer workflows.

### Comment pulse

- Reasoning can be compressed while knowledge stays external → enthusiasts imagined tiny local models consulting documentation — counterpoint: skeptics argued reasoning emerges from broad training.

- Benchmark wins may not transfer to agentic work → commenters cited weak tool calling, one-to-two-message limits, Python-only results, and incoherent conversation.

- Single-chip deployment looks plausible → commenters linked 3B-scale reasoning to Taalas-class ASICs and imagined 16K-token-per-second operation.

### LLM perspective

- **View:** The headline comparison is narrower than general intelligence: specialized, checkable tasks reward optimized post-training and test-time scaling.

- **Impact:** Cheap reasoning cores could complement larger models, handling bounded subproblems locally while general systems supply context and orchestration.

- **Watch next:** Test non-Python coding, tool use, multi-turn stability, knowledge-intensive tasks, independent benchmark replication, and end-to-end agent workloads.
