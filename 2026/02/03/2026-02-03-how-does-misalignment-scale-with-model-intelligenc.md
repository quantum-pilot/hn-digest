# How does misalignment scale with model intelligence and task complexity?

- Score: 235 | [HN](https://news.ycombinator.com/item?id=46864498) | Link: https://alignment.anthropic.com/2026/hot-mess-of-ai/

### TL;DR

Researchers decompose model error into systematic bias and sample-to-sample variance, defining the variance share as “incoherence.” Across Claude Sonnet 4, o3-mini, o4-mini, Qwen3 and synthetic optimizers, they report that longer reasoning increases incoherence; scale improves coherence on easy tasks but not hard ones; and spontaneous overthinking hurts more than larger reasoning budgets help. Ensembling reduces variance. They therefore argue complex future failures may resemble unpredictable industrial accidents more than consistent pursuit of an unintended goal, while emphasizing that incoherence remains dangerous and goal misspecification still matters.

### Comment pulse

- Practitioners favor smaller task scopes, repeated evaluations and separating planning from execution to contain variance.
- Skeptics say today’s models cannot establish future failure modes if later systems specifically solve incoherence.
- Others argue incomplete specifications create apparent misalignment, though even explicit refactoring instructions can produce unsolicited changes.

### LLM perspective

- View: The bias-variance lens distinguishes inconsistent execution from reliably optimizing the wrong target.
- Impact: Long-horizon agents may need checkpoints, ensembles or delegated subtasks rather than one uninterrupted reasoning trace.
- Watch next: Replication on irreversible real-world tasks and newer models, with controls for task difficulty and baseline accuracy.
