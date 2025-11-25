# Claude Advanced Tool Use

- Score: 275 | [HN](https://news.ycombinator.com/item?id=46038047) | Link: https://www.anthropic.com/engineering/advanced-tool-use

- TL;DR
  - Anthropic adds three beta features for Claude agents: Tool Search (defer + discover tools on demand), Programmatic Tool Calling (code orchestrates tools, not prompts), and Tool Use Examples (sample calls). Internal results: ~85% tool-definition token savings and accuracy gains (Opus 4: 49→74%; Opus 4.5: 79.5→88.1), plus 37% average token reduction and lower latency with code orchestration; parameter accuracy 72→90% with examples. HN debates GraphQL-as-one-tool simplicity, potential “Tool Engine Optimization” gaming, complexity pendulum, and security of third‑party example code.

- Comment pulse
  - GraphQL-as-single-tool beats MCP → typed schema, exact data, fewer tokens; LLMs write queries. — counterpoint: introspection can bloat tokens; claims need measurements.
  - Tool search risks TEO: spammy ranking, ads, gaming. — counterpoint: discovery could rely on GitHub/known repos already embedded in models.
  - Agents oscillate complexity: scaffolding inflates context; code-first SDKs or compact signatures (.d.ts-like, functions API) may simplify; avoid pseudo-RPC overhead.

- LLM perspective
  - View: Dynamic discovery plus code orchestration mirrors software modularity; let models reason over results, not raw intermediate data.
  - Impact: Enterprise agents scale to many systems with lower cost/latency; infra shifts to search quality, schemas, and sandbox security.
  - Watch next: Standard tool signatures (.d.ts/MCP Output Schema), anti-TEO ranking signals, and benchmarks comparing GraphQL-only vs MCP/PTC stacks.
