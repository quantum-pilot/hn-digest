# Pro Max 5x quota exhausted in 1.5 hours despite moderate usage

- Score: 511 | [HN](https://news.ycombinator.com/item?id=47739260) | Link: https://github.com/anthropics/claude-code/issues/45756

### TL;DR

Claude Code users report exhausting a Pro Max 5× quota in roughly 90 minutes. A team representative attributes many cases to costly cache misses in million-token sessions, especially after idle periods, plus plugins that load many skills or launch agents and background jobs. Anthropic is testing a 400,000-token default, better visibility, and smarter pruning. Users remain unconvinced, citing a recent cache-lifetime change, long exploratory loops, opaque accounting, and context-reset nudges that merely force expensive rebuilding. Many are testing Codex, Cursor, Kiro, or local models.

### Comment pulse

- Clearing or compacting can reduce future context cost. — counterpoint: rebuilding productive context still consumes quota and interrupts unattended workflows.
- Users disagree whether maximal thinking saves tokens, illustrating how opaque metering turns optimization into anecdote and ritual.
- Some expect subsidized coding-agent plans to tighten across vendors as demand outruns compute capacity.

### LLM perspective

- **View:** The core failure is unpredictability: subscribers cannot connect actions, context size, and cache state to quota burn.
- **Impact:** Professionals cannot budget focused work when hidden agents, skills, or cache misses can consume hours of allowance.
- **Watch next:** Configurable context limits, cache telemetry, per-task usage breakdowns, quota refunds, and a reproducible explanation for March’s shift.
