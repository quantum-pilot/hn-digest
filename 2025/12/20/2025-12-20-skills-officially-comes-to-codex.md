# Skills Officially Comes to Codex

- Score: 231 | [HN](https://news.ycombinator.com/item?id=46334424) | Link: https://developers.openai.com/codex/skills/

### TL;DR

Codex Agent Skills package reusable workflows as a required `SKILL.md` plus optional scripts, references, and assets. At startup, Codex loads each skill’s name and description, then reads full instructions only when the user explicitly invokes it or the task matches implicitly. Skills work in the CLI and IDE, follow an open specification, and can be scoped at repository, user, admin, or system levels with defined precedence. They are designed to make task-specific expertise shareable, composable, versionable, and more context-efficient than permanently loading every instruction.

### Comment pulse

- Supporters prefer skills’ simple files, progressive disclosure, scripts, composability, and ability to document effective use of existing tools or MCP servers.
- Critics warn every front-matter description consumes context and influences selection, making discoverability, prompt injection, and skill sprawl practical concerns.

### LLM perspective

- View: Skills standardize operational knowledge effectively, but their value depends more on precise descriptions than elaborate bodies.
- Impact: Teams can review and version agent workflows alongside code without building a bespoke integration service.
- Watch next: Searchable registries, provenance controls, signature verification, conflict handling, and measurements of selection accuracy.
