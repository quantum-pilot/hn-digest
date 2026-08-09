# Cook: A simple CLI for orchestrating Claude Code

- Score: 284 | [HN](https://news.ycombinator.com/item?id=47434024) | Link: https://rjcorwin.github.io/cook/

### TL;DR

Cook provides a compact left-to-right command grammar for coordinating Claude Code, Codex, and OpenCode. Sequential operators repeat work, add review-and-gate iterations, or advance through task lists; composition operators race identical runs or compare different approaches in isolated worktrees, then pick, merge, or document results. Configuration selects agents, models, sandboxes, and rate-limit waiting. HN saw value in reusable multi-agent workflows but questioned whether Bash or a small Python subprocess loop would suffice. The distinction is packaged composability and repeatability rather than a new agent capability.

### Comment pulse

- Repeated orchestration patterns justify a wrapper → named operators reduce prompt repetition and inconsistent one-off scripts.
- Simple subprocess loops cover specialized experiments → commenters questioned dependency value — counterpoint: Cook packages branching, review gates, resolution, and recovery.
- Naming collision amused another Cook author → the two projects respectively orchestrate agents and serve as an agent.

### LLM perspective

- **View:** A tiny workflow language is useful when teams can inspect its semantics and predict how operators nest.
- **Impact:** Agent users trade bespoke scripts for standardized loops, parallel trials, model routing, and logs.
- **Watch next:** Conflict handling, integration validation, task receipts, rate-limit continuation behavior, and measured gains over simple scripts.
