# Anthropic tries to hide Claude's AI actions. Devs hate it

- Score: 346 | [HN](https://news.ycombinator.com/item?id=47033622) | Link: https://www.theregister.com/2026/02/16/anthropic_claude_ai_edits/

### TL;DR

Claude Code 2.1.20 replaced visible file-level activity with generic counts, leaving paths behind an expansion shortcut. Anthropic framed the change as reducing terminal noise as agents run longer, while developers said paths are essential for spotting wrong context, unauthorized edits, security issues, and wasted tokens. After backlash, Anthropic repurposed verbose mode to restore read and search paths without every internal detail, but retained the condensed default—simultaneously reducing the older verbose view and satisfying neither visibility preference cleanly.

### Comment pulse

- Continuous file visibility enables early steering → agents can spend minutes in the wrong project before final diffs reveal the mistake.
- Autonomous agent teams motivate quieter interfaces → counterpoint: long unattended runs increase, rather than remove, the need for trustworthy audit trails.
- Developers can switch harnesses while keeping models → poor UX risks eroding Claude Code’s strongest niche.

### LLM perspective

- **View:** Observability is part of control, not terminal decoration.
- **Impact:** Developers need selectable detail levels that preserve paths, permissions, and chronological auditability.
- **Watch next:** Track whether defaults change and whether full verbose output returns under a distinct mode.
