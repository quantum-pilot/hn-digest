# Claude Code on the web

- Score: 322 | [HN](https://news.ycombinator.com/item?id=45647166) | Link: https://www.anthropic.com/news/claude-code-on-the-web

### TL;DR

Anthropic launched Claude Code on the web as a Pro and Max research preview for delegating repository tasks to isolated cloud sessions. Users connect GitHub, run multiple jobs in parallel, monitor and steer progress, and receive summaries and automatically created pull requests; an early iOS version extends access to mobile. Anthropic says sandboxes restrict filesystem and network access, use a proxy for authorized Git operations, and allow custom domain rules. Sessions share existing Claude Code rate limits, and the product targets repository questions, routine fixes, and backend work.

### Comment pulse

- Users debated Claude Code versus Codex on model quality, speed, permissions, planning, and long-running tasks.
- Some welcomed isolated unattended execution; others preferred tight local iteration over reviewing generated pull requests.
- Security discussion questioned whether broad allowed domains still permit code or data exfiltration.

### LLM perspective

- View: The product turns coding agents into asynchronous workers, making sandbox quality part of the developer experience.
- Impact: Parallel cloud sessions reduce terminal supervision but shift validation toward branches, summaries, and pull requests.
- Watch next: Sandbox audits, persistent environments, richer testing, smoother local handoff, and beta reliability.
