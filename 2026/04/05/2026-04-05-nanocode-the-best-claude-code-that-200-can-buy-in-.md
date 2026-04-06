# Nanocode: The best Claude Code that $200 can buy in pure JAX on TPUs

- Score: 147 | [HN](https://news.ycombinator.com/item?id=47649742) | Link: https://github.com/salmanmohammadi/nanocode/discussions/1

### TL;DR
Nanocode is a small JAX codebase that walks you through training a Claude-Code-style coding agent from scratch on TPUs for roughly $200. Starting with a GPT‑2-scale pretrain (FineWeb‑EDU + The Stack v2), it specializes for “agentic coding” via custom tool-calling tokens (Read/Edit/Grep/Bash), synthetic datasets, and a Claude-like “SOUL” document. Post-training uses Constitutional-AI-style supervised data plus Direct Preference Optimization for personality and tool use. The goal is education and hackability, not beating frontier models.

---

### Comment pulse
- Example bug in a “remove falsey values” snippet → highlights that many seed datasets are LLM-generated and subtly wrong — counterpoint: prompt itself is contradictory.
- Why pay $200 vs using free models? → this is a learning lab for JAX, TPUs, CAI-style post-training, not a production competitor.
- Does this mirror Anthropic? → similar structure (tools, CAI, preference learning) but massively scaled down; real systems use far more data and online RL.

---

### LLM perspective
- View: This is a rare, end-to-end, readable blueprint for modern post-training and tool-use in a single, hackable repo.
- Impact: Best for researchers, tinkerers, and infra/ML engineers wanting hands-on experience with agentic coding stacks.
- Watch next: Benchmarks on real coding tasks, more robust evals of tool use, and ports to other frameworks/hardware.
