# Nanocode: The best Claude Code that $200 can buy in pure JAX on TPUs

- Score: 147 | [HN](https://news.ycombinator.com/item?id=47649742) | Link: https://github.com/salmanmohammadi/nanocode/discussions/1

### TL;DR

Nanocode is a 5,500-line JAX project for learning how to pretrain and post-train a small coding agent on TPUs. Its 1.3B-parameter model costs about $200 and nine hours on a v6e-8; a 477M variant takes roughly 1.5 hours for $34. Building on nanochat, it mixes FineWeb-Edu with Stack V2 code, doubles context to 4,096 tokens, teaches Read/Edit/Grep/Bash calls through synthetic rollouts, then applies Constitution-guided SFT and DPO for a lowercase personality. The author warns it is under-tuned, weak on complex fixes, and lacks rigorous agentic evaluations.

### Comment pulse

- Readers caught a synthetic example that returns a new list despite claiming in-place mutation; the prompt itself also contradicts that requirement.
- Spending $200 makes little sense for deployment — counterpoint: the author positions training as education in JAX, distributed systems, and preference optimization.
- Practitioners called the Claude analogy simplified: production agents use vastly more data, compute, and online reinforcement learning, while Claude Code is technically a harness.

### LLM perspective

- **View:** Its achievement is pedagogical compression: one reproducible pipeline exposes tokenization, pretraining, tool formatting, synthetic alignment, and inference.
- **Impact:** Researchers can cheaply test agent interfaces and post-training ideas without mistaking the resulting model for a competitive assistant.
- **Watch next:** Task benchmarks, ablations, contradictory data, tool-call reliability, GPU portability, online reinforcement learning, and larger-scale replication.
