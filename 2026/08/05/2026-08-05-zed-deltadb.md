# Zed DeltaDB

- Score: 520 | [HN](https://news.ycombinator.com/item?id=49187256) | Link: https://zed.dev/deltadb

### TL;DR

DeltaDB is Zed’s early-access version-control layer for work between commits. It records every edit as a stable operation, links code changes to the agent conversations that produced them, permits branching from any intermediate point, and virtualizes worktrees so agent branches are cheap. Teams can join work before a commit, annotate it, and converse with the responsible agent; sharing the thread becomes an alternative to waiting for a pull request. The pitch focuses on traceability and collaboration around AI-generated changes rather than explicitly replacing Git.

### Comment pulse

- Many users wanted Zed to fix editor basics—file refresh, Linux clipboard, freezes, resource use, and UI issues—before expanding scope.
- Defenders said DeltaDB complements Git by exposing agent edits and rationale between commits.
- Critics associated the project and its copy with AI-driven scope expansion — counterpoint: experimental tooling can produce valuable infrastructure.

### LLM perspective

- View: Commit-level history is too coarse for supervising long, agent-driven edit streams.
- Impact: Conversation-linked operations could improve review, rollback, and parallel exploration.
- Watch next: Git interoperability, storage overhead, conflict semantics, and whether core-editor reliability receives equal attention.
