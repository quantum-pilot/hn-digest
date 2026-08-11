# Fix your tools

- Score: 175 | [HN](https://news.ycombinator.com/item?id=47112174) | Link: https://ochagavia.nl/blog/fix-your-tools/

### TL;DR

A maintainer initially worked around a debugger that ignored breakpoints by adding diagnostic logging, then realized the broken tool was obstructing the actual investigation. A one-line configuration fix restored debugging visibility and enabled the underlying library bug to be solved. HN endorsed maintaining leverage-producing tools but stressed the stopping rule: repair or replace tooling when it clearly blocks progress, yet avoid turning a small task into open-ended yak shaving, speculative automation, or a cleaner side project that postpones the real objective.

### Comment pulse

- Sharpening tools compounds → repeated friction deserves automation or repair, especially when failures are silent or diagnostics are weak.
- Tool work can become procrastination → urgency sometimes favors hardcoded, disposable progress — counterpoint: neglected debt is eventually paid.
- Replacement may be the fix → simple, purpose-built scripts can outperform opaque all-in-one workflow platforms when debugging matters.

### LLM perspective

- **View:** Time-box tool repair against the expected cost of continuing blind.
- **Impact:** Teams benefit from explicit maintenance budgets and transparent fallbacks.
- **Watch next:** Whether the repaired debugger prevents recurrence and reduces future diagnosis time.
