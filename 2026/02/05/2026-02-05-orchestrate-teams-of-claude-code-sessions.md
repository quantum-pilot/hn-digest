# Orchestrate teams of Claude Code sessions

- Score: 387 | [HN](https://news.ycombinator.com/item?id=46902368) | Link: https://code.claude.com/docs/en/agent-teams

### TL;DR

Claude Code’s experimental Agent Teams feature coordinates a lead session and independent teammates through shared tasks, dependencies, mailboxes, and direct messaging. Unlike subagents, teammates can communicate and self-coordinate, each with its own context. Teams suit parallel research, review, competing debugging hypotheses, or file-disjoint modules, while sequential and tightly coupled work should stay single-session. Plan approval, delegate mode, hooks, and explicit ownership add control. The docs warn of much higher token use, no nested teams, fragile resumption, lagging tasks, slow shutdown, and file conflicts. Commenters questioned novelty and affordability.

### Comment pulse

- Multi-agent orchestration looked like convergent evolution from actors, scripts, and Gas Town, not a new systems concept; improved models now make it practical.
- One reported four-agent run cut 18–20 sequential minutes to six at roughly fourfold tokens, with file-disjoint tasks preventing conflicts.
- Costs split opinion—counterpoint: some exhausted paid quotas quickly, while others said short bursts or $200 Max plans remained economical.

### LLM perspective

- View: Parallel agents buy latency reduction and independent search, not free throughput; decomposition and verification remain the scarce human skills.
- Impact: Teams can accelerate review and modular changes, while token bills, duplicated work, and coordination failures rise with concurrency.
- Watch next: Conflicts, escaped defects, token-adjusted speed, UI stability, resumption, task accuracy, permission isolation, and comparisons with simpler scripts.
