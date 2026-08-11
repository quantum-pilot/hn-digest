# How I use Claude Code: Separation of planning and execution

- Score: 867 | [HN](https://news.ycombinator.com/item?id=47106686) | Link: https://boristane.com/blog/how-i-use-claude-code/

### TL;DR

The author’s Claude Code workflow separates research, planning, and implementation: first create a persistent codebase report, then iteratively annotate a detailed plan until assumptions and scope are approved, add a task checklist, and only then let one long session execute while type-checking. HN valued plans as review surfaces for hidden architectural assumptions. Debate focused on the author’s prompt intensifiers and “implement it all” approach; critics preferred staged commits, durable project guidance, explicit tests, and evidence that words such as “deeply” reliably improve model behavior.

### Comment pulse

- Written plans expose assumptions before code hardens them → inline annotations inject product constraints and preserve decisions through context compaction.
- Big-bang execution risks opaque changes → phase-by-phase implementation and comprehensive tests improve reviewability — counterpoint: an approved checklist can sustain momentum.
- Prompt incantations remain unproven → users report benefits from emphasis, but commenters requested reproducible comparisons rather than intuition.

### LLM perspective

- **View:** The durable artifact matters more than the exact adjectives used to request it.
- **Impact:** Experienced developers spend less time unwinding wrong assumptions but remain responsible for architecture and verification.
- **Watch next:** Controlled workflow comparisons measuring defects, tokens, review time, and test coverage.
