# Claude Skills are awesome, maybe a bigger deal than MCP

- Score: 388 | [HN](https://news.ycombinator.com/item?id=45619537) | Link: https://simonwillison.net/2025/Oct/16/claude-skills/

- TL;DR
  Anthropic’s Claude Skills are lightweight folders (Markdown + YAML, optional scripts) that models load only when relevant, keeping prompts token‑lean. Running inside Claude Code’s sandbox, they turn Claude into a general automation agent; Anthropic’s document tools and a Slack GIF validator show the pattern. Compared with MCP, Skills avoid protocol overhead and context bloat, leaning on existing CLIs and filesystems and working across models. HN highlights tool‑calling as the real innovation, with skills making documentation actionable; MCP still shines for auth and cross‑app integrations.

- Comment pulse
  - Docs become useful → fast feedback, AI-assisted authoring, and direct personal benefit turn tribal knowledge into task guides; previously blocked by slow loops and tech-debt.
  - Tool-calling is the win → MCP rode timing; Skills/CLIs minimize tokens and complexity — counterpoint: MCP adds OAuth, cross-app UIs, and works without sandboxes/small models.
  - Skills package instructions plus code → some are just tools with docs; environment handles dependencies; future: skills invoking MCP servers from the interpreter.

- LLM perspective
  - View: Skills are token-frugal, composable task packs; paired with code sandboxes, they unlock general-purpose automation beyond coding.
  - Impact: Dev productivity and SOPs become executable assets; lighter than MCP, portable across models, and fast to iterate and share.
  - Watch next: Sandbox hardening and dependency manifests; public skills registries/versioning; benchmarks versus MCP/CLIs on latency, cost, and task success.
