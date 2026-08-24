# Show HN: NanoClaw – “Clawdbot” in 500 lines of TS with Apple container isolation

- Score: 85 | [HN](https://news.ycombinator.com/item?id=46850205) | Link: https://github.com/gavrielc/nanoclaw

### TL;DR

NanoClaw is a personal Claude assistant that routes WhatsApp messages through SQLite to agents running in per-group Apple containers. It supports isolated memories and mounted files, scheduled tasks, web access and optional integrations. Its deliberately small, single-process design replaces broad configuration with code changes generated through skills, targeting one owner rather than a general framework. The repository claims OS isolation and auditability improve safety, but HN commenters questioned unrestricted external actions, AI-generated documentation and whether the advertised 500-line scale matches roughly 2,500 TypeScript lines.

### Comment pulse

- Apple Container isolation appealed to readers, but they asked how an agent safely performs consequential actions outside mounted filesystems.
- Some welcomed a smaller OpenClaw alternative; others distrusted AI-polished documentation and alleged unchecked README hallucinations.
- The project’s scope drew line-count skepticism, while native containers’ lightweight virtual machines attracted technical interest.

### LLM perspective

- View: Small, fork-specific code improves comprehensibility, yet generated customization steadily erodes the common audited baseline.
- Impact: Solo users gain a controllable assistant; security depends on mounts, host IPC, credentials and every locally generated change.
- Watch next: Independent code audit, accurate line-count claims, Linux conversion, MCP behavior and tests of cross-group isolation.
