# Claude Skills

- Score: 446 | [HN](https://news.ycombinator.com/item?id=45607117) | Link: https://www.anthropic.com/news/skills

### TL;DR

Anthropic’s Skills package instructions, scripts, and resources into folders that Claude loads only when relevant. They are designed to compose, remain portable across Claude apps, Claude Code, and the API, and use executable code for deterministic work. Custom API skills require code execution, while Claude Code can install them through plugins or a local directory. Commenters saw a useful context-loading pattern but worried about concept proliferation, weak skill-selection blurbs, overlap with MCP and project instructions, and executable-code supply-chain risk.

### Comment pulse

- Skills are progressive context disclosure → concise descriptions advertise reference material that the agent reads only when needed.
- Terminology fatigue is real → agents, tools, MCP, commands, apps, and skills impose overlapping mental models.

### LLM perspective

- View: Skills formalize reusable operational knowledge more than they introduce a fundamentally new agent capability.
- Impact: Teams can version workflows once, but must govern descriptions, permissions, provenance, and cross-product compatibility.
- Watch next: Measure invocation accuracy, context savings, malicious-skill defenses, version rollout, and interoperability with MCP.
