# Claude Code's new hidden feature: Swarms

- Score: 264 | [HN](https://news.ycombinator.com/item?id=46743908) | Link: https://twitter.com/NicerInPerson/status/2014989679796347375

### TL;DR

A post claims an unreleased Claude Code mode turns the main model into a lead that plans, delegates, and synthesizes instead of coding. After approval, specialists work in parallel from a dependency-aware task board and coordinate through messages. Commenters disputed whether this is fundamentally new or integrated subagents with better task state and mailboxes. One commenter reported his best code from a nine-agent team despite likely tenfold cost; others expected more code, weaker reviewability, and operational debt because current agents still miss simple judgment calls.

### Comment pulse

- Coordination can reduce human context switching → a manager agent tracks specialists, dependencies, and handoffs while isolated worktrees limit collisions.
- Role-heavy orchestration risks ceremony → a nine-agent, seven-stage Kanban can exceed the software task — counterpoint: its author reported better code and fun.
- Production confidence remains unproven → large generated changes make ownership and review harder than testing a demo’s surface behavior.

### LLM perspective

- View: Better orchestration scales both useful parallelism and model mistakes.
- Impact: Teams may exchange developer attention for inference cost, review load, and more complex failure diagnosis.
- Watch next: Official release details, task completion benchmarks, code volume, merge conflicts, review time, and three-month production outcomes.
