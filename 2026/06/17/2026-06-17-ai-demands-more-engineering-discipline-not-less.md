# AI demands more engineering discipline. Not less

- Score: 329 | [HN](https://news.ycombinator.com/item?id=48570948) | Link: https://charitydotwtf.substack.com/p/ai-demands-more-engineering-discipline

### TL;DR

The essay argues that cheap AI generation should make implementations disposable, like immutable infrastructure, while moving durable knowledge into specifications, architecture artifacts, behavioral tests, capture-replay, observability, and production evaluations. Code becomes a materialized view of shared understanding, regenerated rather than endlessly mutated. Because agents are nondeterministic and output volume explodes, teams need shorter feedback loops and stronger validation, not relaxed review. HN agreed knowledge cannot remain only in code, but warned that plausible automated artifacts can overwhelm reviewers and that complete regenerative specifications may approach source code’s complexity.

### Comment pulse

- Artifact volume obscures competence → prolific agents produce polished code, reviews, and designs, making genuine system understanding harder to identify and increasing hidden debt.
- Human intent should survive generation → prompts, plans, decisions, and agent sessions are often discarded even though they explain and can recreate the implementation.
- Regeneration has an information ceiling → specifications reproducing every behavior may become source code — counterpoint: incomplete models can still be useful.

### LLM perspective

- **View:** AI relocates the bottleneck from production to verification; the scarce resource becomes trustworthy evidence that behavior matches intent.
- **Impact:** Senior engineers spend less time typing and more time designing constraints, decomposing changes, preserving rationale, and interpreting production evidence.
- **Watch next:** Measure review load, defect escape, rollback rates, comprehension retention, regeneration fidelity, and system complexity—not lines or PR counts.
