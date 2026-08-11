# Stop Burning Your Context Window – How We Cut MCP Output by 98% in Claude Code

- Score: 200 | [HN](https://news.ycombinator.com/item?id=47193064) | Link: https://mksg.lu/blog/context-mode

### TL;DR

Context Mode intercepts large MCP and command outputs, executes filtering inside isolated subprocesses, and admits only stdout into Claude Code's context. It can index full Markdown in SQLite FTS5 for BM25 retrieval, supports ten runtimes and authenticated CLIs, and claims 315 KB shrank to 5.4 KB across a session, extending useful work from roughly 30 minutes to three hours. Hacker News welcomed searchable output and proposed pruning failed attempts, while noting Claude already truncates responses and tool-definition bloat still requires curation or subagents.

### Comment pulse

- Searchable retention beats simple truncation → full results remain queryable instead of disappearing after a local summary.
- Context should be editable → resolved debugging attempts and stale logs could be pruned once their conclusions are retained.
- Curated tools and subagents attack root bloat — counterpoint: one snapshot can still overwhelm an otherwise focused session.

### LLM perspective

- **View:** Treat context as managed working memory rather than an append-only transcript.
- **Impact:** Longer sessions may reduce compaction errors, latency and repeated investigation.
- **Watch next:** Independent benchmarks, prompt-cache behavior, credential isolation and failure modes when filtering discards decisive evidence.
