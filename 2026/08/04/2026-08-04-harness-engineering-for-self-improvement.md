# Harness engineering for self-improvement

- Score: 312 | [HN](https://news.ycombinator.com/item?id=49164896) | Link: https://lilianweng.github.io/posts/2026-07-04-harness/

### TL;DR

Weng frames harness engineering as the practical near-term route to recursive self-improvement: improve the runtime around a fixed model before expecting models to rewrite their own weights. Effective harnesses combine simple action loops, filesystem-backed state, inspectable subagents, context curation, evaluation, permissions, and regression testing. Surveyed systems increasingly optimize prompts, workflows, harness code, and even optimizer code through agentic or evolutionary search. Results are strongest where fitness is objective; fuzzy scientific value, memory decay, diversity collapse, reward hacking, and long-term maintainability still require external controls and human judgment.

### Comment pulse

- Project-specific evals are the missing fitness function → public benchmarks saturate, differ from real repositories, and cannot compare tasks of unequal difficulty.
- Session retros expose useful improvements → agents can identify confusing instructions, missing invariants, brittle tools, and latent follow-up work.
- Determinism and fail-closed coverage improve credit assignment → a passing but incomplete check suite can make harmful harness edits look decisively successful.

### LLM perspective

- **View:** Self-improvement is already a software optimization problem, but only within boundaries an independent evaluator can enforce.
- **Impact:** Teams should treat prompts, tools, memory, and permissions as versioned, testable production components.
- **Watch next:** Cross-repository transfer, held-out regressions, total compute cost, and robustness when tasks resist automatic scoring.
