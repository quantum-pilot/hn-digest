# OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI

- Score: 536 | [HN](https://news.ycombinator.com/item?id=46250332) | Link: https://simonwillison.net/2025/Dec/12/openai-skills/

### TL;DR
OpenAI has quietly adopted a Claude-style “skills” system: small folders containing a markdown spec plus optional scripts and resources that models can discover and load on demand. In ChatGPT’s Code Interpreter, built‑in skills handle spreadsheets, DOCX, and PDFs by converting them to images for vision models, enabling iterative, layout‑aware PDF generation. Codex CLI now supports user-defined skills living in `~/.codex/skills`, demonstrated by automatically generating a Datasette plugin. HN sees skills as simple dynamic prompt/context management—conceptually old, but very practical when paired with cloud code execution and lazy loading.

---

### Comment pulse
- Skills are dynamic prompt/context extensions in folders with markdown and scripts; conceptually similar to AGENT.md or *.instruction.md—counterpoint: packaging + discovery make them more reusable.
- Lazy-loaded skills avoid bloated prompts and MCP overhead: index only, load full instructions/scripts when needed, so you pay tokens only for invoked capabilities.
- Implementations scan SKILL.md metadata into an index, then fetch deeper docs/scripts on demand; people build evolving skill libraries for debugging, CI, and project-specific workflows.

---

### LLM perspective
- View: Skills formalize a “modular knowledge + scripts” layer that LLMs can selectively load, making agents more maintainable than giant, monolithic system prompts.
- Impact: Biggest short-term wins are in dev tooling, data work, and team repos where repeatable workflows can be encoded once and reused safely.
- Watch next: Cross-vendor skill specs, permission models for executing arbitrary scripts, and benchmarks of skills vs MCP/agent frameworks on reliability and cost.
