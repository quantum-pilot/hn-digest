# Open source Kanban desktop app that runs parallel agents on every card

- Score: 148 | [HN](https://news.ycombinator.com/item?id=48239413) | Link: https://www.kanbots.dev/

### TL;DR

KanBots is an MIT-licensed desktop Kanban for dispatching Claude Code or Codex from cards, isolating each run in a Git worktree and storing state locally in SQLite without accounts or telemetry. Its autopilot cycles up to four persona-driven agents, splits tasks, pauses for decisions, tracks costs, and stops at budgets; a paid cloud tier adds collaboration while execution remains local. HN readers liked the local-first model but questioned whether parallel overnight work creates unreviewable diffs, merge pain, and lost product intent despite the human-in-the-loop controls.

### Comment pulse

- Review-first users preferred one or two concurrent chats; even 30 minutes of autonomous coding can hide misunderstandings that become expensive later.
- Smaller, well-structured changes felt tractable: respondents staged approved files and asked agents to prioritize review order — counterpoint: managers increasingly treat review as bottleneck.
- Comparisons to Vibe Kanban and Windsurf emphasized remote access and editor integration; others saw dedicated orchestration UIs as replaceable by existing task-system APIs.

### LLM perspective

- View: The board’s value is observability and containment; agent throughput matters only when review capacity scales with it.
- Impact: Solo developers gain structured delegation, but concurrency can shift the bottleneck from implementation to specification, review, and integration.
- Watch next: Measure defect escape rates, review time, merge conflicts, and cost per accepted change across supervised and autopilot modes.
