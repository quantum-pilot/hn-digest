# How Complex is my Code?

- Score: 170 | [HN](https://news.ycombinator.com/item?id=47673171) | Link: https://philodev.one/posts/2026-04-code-complexity/

### TL;DR

Sofia Fischer surveys code complexity as resource costs: runtime and memory, execution paths, token vocabulary, and human understanding. Cyclomatic and Halstead measures can expose risky functions, yet miss domain knowledge, semantics, and surprising constraints. She maps psycholinguistic ideas—familiarity, dependency distance, working-memory load, coherence, and entropy—to variable lifetimes, call graphs, and recognizable patterns, concluding complexity ultimately depends on the reader. Metrics become useful when combined with churn and coupling to prioritize refactoring, visualize debt, and support discussion, not when imposed as optimization targets. Commenters emphasized accidental and cross-feature complexity.

### Comment pulse

- Experienced engineers described resisting accidental complexity as constant work, punctuated by rare abstractions that eliminate whole problem classes.
- Function-level scores miss feature-wide cause-and-effect chains; commenters favored tracing data and organizing related policy near the feature.
- Measuring agent-generated complexity could prompt simplification — counterpoint: optimizing a score invites Goodhart effects such as duplicated code.

### LLM perspective

- **View:** No scalar captures maintainability; complexity is a relationship among code, domain, architecture, task, and reader experience.
- **Impact:** Churn-and-coupling overlays turn imperfect measures into practical triage signals for human and AI-generated code.
- **Watch next:** Feature-level metrics, reader studies, longitudinal defect data, agent-change deltas, and whether visualizations improve refactoring decisions.
