# Claude Code as a Daily Driver: Claude.md, Skills, Subagents, Plugins, and MCPs

- Score: 348 | [HN](https://news.ycombinator.com/item?id=48289950) | Link: https://arps18.github.io/posts/claude-code-mastery/

**TL;DR**  
The post is a deep “how to actually live in Claude Code” guide: treat it as a configurable engineer, not autocomplete. Core ideas: keep `CLAUDE.md` tiny but ruthlessly tuned from past mistakes; use `CLAUDE.local.md` to encode personal PR feedback; factor repeated workflows into Skills and Subagents; rely on `/goal`, planning mode, and tests/commands so Claude verifies its own work; and wire Plugins/MCPs plus Obsidian or notes for project memory. HN likes the power, but criticizes complexity, ceremony, and an AI-written feel.

---

### Comment pulse

- Abstraction sprawl complaint → commands, skills, agents, plugins all feel like “canned prompts”; Boris: consolidating on built-in `/code-review` with effort levels and `--fix`/`ultra`.  
- Skills skepticism → they became a junk drawer; commenters want clearer separation between agents (persona), prompts (tasks), and tools—counterpoint: subagents truly add value via clean, separate context.  
- Real-world use → Claude speeds work on 100k+ LOC, but devs still manually review and iterate; advice: encode repeated tweaks into config instead of endless back-and-forth.

---

### LLM perspective

- View: The real innovation isn’t features, it’s treating configuration files as an evolving “house style” for how your AI collaborator works.  
- Impact: Teams with large, stable codebases gain most; solo/greenfield work may not justify heavy skills/agents/plugin scaffolding.  
- Watch next: Whether ecosystems converge on fewer, clearer abstractions—perhaps portable “agent profiles” and task prompts that work across vendors and open-source models.
