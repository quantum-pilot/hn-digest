# Over-editing refers to a model modifying code beyond what is necessary

- Score: 271 | [HN](https://news.ycombinator.com/item?id=47866913) | Link: https://nrehiew.github.io/blog/minimal_editing/

## TL;DR
The post defines “over-editing” as LLMs rewriting far more code than necessary to fix a bug, which bloats diffs and silently harms maintainability despite passing tests. The author builds a synthetic benchmark where the true minimal fix is known, and measures both edit size (token-level Levenshtein) and added cognitive complexity. Frontier models systematically over-edit; Claude Opus is unusually restrained, GPT‑5.4 is not. Explicitly asking for minimal changes helps a lot, especially for reasoning models. Reinforcement learning (with or without LoRA) can train models to make minimal edits that generalize to new bug types without degrading general coding ability.

---

## Comment pulse
- AI as coding coworker → Some engineers report Claude/Cursor now write most of their code; careful feedback and “skill files” make over-editing rare and productivity huge.  
- Minimal diff vs refactor → Others often want larger refactors; the optimal change size depends on codebase age, review culture, and which files are “sacred.”  
- Hidden risk and learned helplessness → Agents may hide failures, over-automate ops, touch infra, and atrophy developer skills—counterpoint: keeping humans in approval loop mitigates this.

---

## LLM perspective
- View: Over-editing is a controllable style issue; models can already do minimal edits but default incentives push toward maximal “improvements.”  
- Impact: IDE vendors and in-house tooling should expose explicit “minimal edit” modes and train on minimality-aware rewards, not just test-pass metrics.  
- Watch next: Benchmarks on real PRs, repo-scale evaluations, and policies tying model rewards to reviewability and blast radius of changes.
