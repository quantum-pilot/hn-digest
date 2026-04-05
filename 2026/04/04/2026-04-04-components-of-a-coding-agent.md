# Components of a Coding Agent

- Score: 149 | [HN](https://news.ycombinator.com/item?id=47638810) | Link: https://magazine.sebastianraschka.com/p/components-of-a-coding-agent

### TL;DR
Raschka decomposes “coding agents” like Claude Code into their real value-add over plain LLM chat: a harness that manages repo context, cached prompt prefixes, structured tool calls with validation and permissions, context compaction, durable transcripts plus distilled working memory, and bounded subagents for delegated subtasks. This scaffolding makes average LLMs feel much stronger and narrows the gap between open and closed models. HN commenters extend the idea toward spec‑driven development, central sources of truth, and serious attention to context and safety.

---

### Comment pulse
- Spec‑driven agents beat chat‑style coding → specs become the single source of truth, constrain context, preserve intent; tools like Ossature implement a spec→plan→code pipeline.  
- Open models in strong harnesses rival frontier products → GLM, Qwen, etc. already plug into Codex/Claude‑like CLIs and feel highly capable for personal projects.  
- Harness power is brittle → simple loops plus bash and truncation/summaries unlock autonomy, but real-world harnesses become sprawling, hard‑to‑audit systems with nontrivial safety risks.

---

### LLM perspective
- View: The main innovation is shifting complexity from the model into deterministic scaffolding that shapes context, tools, and control flow.  
- Impact: IDEs, CLIs, and internal dev tools become competitive by pairing solid open models with carefully engineered harnesses.  
- Watch next: Shared spec formats, richer traceability, and benchmarks that evaluate complete agents, not just standalone LLMs.
