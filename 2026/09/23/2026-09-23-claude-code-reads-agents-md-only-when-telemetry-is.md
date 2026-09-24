# Claude Code reads AGENTS.md only when telemetry is on [fixed]

- Score: 463 | [HN](https://news.ycombinator.com/item?id=49814947) | Link: https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/

### TL;DR

Claude Code 2.1.277 initially placed `AGENTS.md` loading behind a remote feature flag whose fallback was off. Disabling telemetry or nonessential traffic prevented the flag from resolving, so local project instructions were silently skipped; a one-line `CLAUDE.md` import worked around it. An Anthropic staff member clarified that this was a rollout kill-switch mistake, not intended telemetry coupling, and said version 2.1.281 fixed it the same day. HN appreciated the response while debating feature flags, silent failure, and AI-generated-code speculation.

### Comment pulse

- The defect was a rollout artifact → Anthropic’s implementer accepted responsibility and shipped a fix in version 2.1.281.
- Silent instruction loss was the real hazard → users could blame model behavior without knowing the file never entered context.
- AI-generated patches were blamed prematurely → the staff account called it a human design error — counterpoint: layered systems still invite subtle regressions.

### LLM perspective

- View: Local documented behavior should fail visibly and remain independent of optional remote configuration.
- Impact: Teams with restricted traffic can now use project instructions, but should verify loader behavior after upgrades.
- Watch next: Test global instructions, mixed `CLAUDE.md` modes, gateways, and future Mods without telemetry.
