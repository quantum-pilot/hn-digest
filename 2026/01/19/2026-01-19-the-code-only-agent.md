# The Code-Only Agent

- Score: 147 | [HN](https://news.ycombinator.com/item?id=46674416) | Link: https://rijnard.com/blog/the-code-only-agent

### TL;DR

The author proposes an agent with one enforced tool: execute code. Every action becomes an executable witness whose runtime semantics, repeatability, and composability are meant to improve exhaustive work over ad hoc tool-call traces. Practical choices include runtime, result-size handling, persistence, output streams, and blocking other tools; future agents might combine natural-language orchestration with code-only inner loops. HN liked persistent self-built CLIs and code-mediated data pipelines, but argued wrappers add tokens and failure modes, context loading remains a bottleneck, and modern models with several flexible tools often outperform single-tool agents.

### Comment pulse

- Reusable tooling → agents can create persistent CLIs that users share — counterpoint: cross-session discovery and duplicate reinvention remain unreliable.
- Semantic skepticism → wrapping mature commands adds code, cost, and bugs without strengthening guarantees; source control already preserves the important artifact.
- Performance evidence → smolagents users report fewer than ten flexible tools outperform code-only designs, except when pipelines avoid large context transfers.

### LLM perspective

- View: Code-only execution is strongest as a compositional interface, not proof that generated behavior is trustworthy.
- Impact: Harness designers trade smaller tool schemas for sandboxing, context routing, artifact discovery, and wrapper maintenance.
- Watch next: Benchmark success, tokens, latency, reproducibility, security escapes, and reuse against direct tools on identical workloads.
