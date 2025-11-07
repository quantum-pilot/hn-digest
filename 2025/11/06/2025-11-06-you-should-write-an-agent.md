# You should write an agent

- Score: 175 | [HN](https://news.ycombinator.com/item?id=45840088) | Link: https://fly.io/blog/everyone-write-an-agent/

- TL;DR
  - Ptacek argues you won’t really grok LLM agents until you build one: a tiny Python loop plus OpenAI’s Responses API yields ChatGPT-like chat, then “tools” (e.g., ping) enable autonomous multi-step actions without extra code. MCP isn’t required; instead, design contexts, segregate tools, and use sub‑agents to manage token budgets, security, and cost. He frames agent design as balancing determinism and emergent behavior. HN backs the DIY ethos: small scripts treating LLMs like Unix filters, model/latency trade-offs, memory/voice add-ons, and debate over small vs mid-grain tool design.

- Comment pulse
  - LLMs as Unix text tools → compose loops and branches; tiny scripts already useful before tool-calling, returning structured output via conventions.
  - Roll-your-own coding agent → swap models; speed matters for multi-turn tools (e.g., Cerebras GLM 4.6); add memory and voice for faster, stickier workflows.
  - Prefer small, deterministic tools for security → agents interpret ping/dig/traceroute well; sweet spot likely mid-grain to curb context bloat — counterpoint: more tools increase overhead.

- LLM perspective
  - View: Leverage lies in state: memory stores, tool scoping, and inter-agent protocols beat prompt wordsmithing.
  - Impact: Dev workflows shift from plugins to bespoke agents; better isolation and tailored security policies.
  - Watch next: Benchmarks on tool orchestration accuracy, context budget strategies, and model latency vs capability trade-offs.
