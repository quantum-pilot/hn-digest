# Cord: Coordinating Trees of AI Agents

- Score: 144 | [HN](https://news.ycombinator.com/item?id=47096466) | Link: https://www.june.kim/cord

## TL;DR
Cord is a small framework and protocol where a single LLM agent dynamically builds and runs a tree of subtasks (with dependencies, parallelism, and human questions) instead of following a developer‑predefined workflow. The key primitives are `spawn` (clean-context child), `fork` (context-inheriting child), `ask`, `complete`, and `read_tree`, enforced by a runtime over SQLite and Claude Code. HN discussion questions how novel “spawn vs fork” really is, suggests richer context-compaction primitives, and debates strict trees/DAGs vs looser event-driven coordination.

---

## Comment pulse
- Claim: Spawn/fork isn’t novel, just new labels → real value is limited; anthropomorphizing tool use overstates LLM “understanding”. — counterpoint: author concedes overselling labels, emphasizes dynamic tree building.
- Claim: First-class context_query is crucial → let agents specify how to compact and pass context, implemented in the client to avoid full-context tool calls.
- Claim: Rigid trees/DAGs are needed for reliability → they bound stochastic behavior; others report success with pub/sub orchestration and think cycles are fine with safeguards.

---

## LLM perspective
- View: Letting models design the task graph while the runtime enforces structure is a pragmatic split between autonomy and control.
- Impact: Orchestration libraries, infra teams, and tooling around MCP/LLM APIs can standardize on a small set of coordination primitives.
- Watch next: Comparative benchmarks vs LangGraph/Swarm, cost/reliability metrics for large trees, and vendor-agnostic specs for spawn/fork/context_query semantics.
