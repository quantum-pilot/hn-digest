# Cord: Coordinating Trees of AI Agents

- Score: 144 | [HN](https://news.ycombinator.com/item?id=47096466) | Link: https://www.june.kim/cord

### TL;DR

Cord is a roughly 500-line Python proof of concept that lets a root Claude Code process create a runtime task tree rather than follow a developer-authored workflow. Agents can spawn clean-context tasks, fork children that inherit completed sibling results, ask humans questions, declare dependencies, and coordinate through MCP tools backed by SQLite. Fifteen behavioral tests reportedly passed. HN liked explicit dependency boundaries and suggested first-class context queries, but challenged the novelty: spawn versus fork mainly labels familiar context-selection tactics, and model-generated trees still need deterministic constraints and better evaluation.

### Comment pulse

- Runtime decomposition adapts task count and parallelism → static graphs remain easier to inspect and constrain when model variance compounds.
- Context should be queried, not merely copied → isolated compaction can pass role-specific summaries without bloating parent or child windows.
- The presentation oversold novelty → the author acknowledged that tree generation, not spawn/fork terminology, is the stronger contribution.

### LLM perspective

- **View:** A coordination protocol needs benchmarks beyond correct tool calls on 15 hand-designed tests.
- **Impact:** Dynamic trees may reduce orchestration code while shifting failure analysis into runtime traces.
- **Watch next:** Baselines, cost scaling, cycle handling, cancellation, retries, authority enforcement, and reproducibility across models.
