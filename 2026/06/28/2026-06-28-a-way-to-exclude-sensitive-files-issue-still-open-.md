# A way to exclude sensitive files issue still open for OpenAI Codex

- Score: 172 | [HN](https://news.ycombinator.com/item?id=48706714) | Link: https://github.com/openai/codex/issues/2847

### TL;DR
OpenAI Codex still lacks a robust way to “ignore” sensitive files (like an `.agentignore`), so agents may accidentally read or exfiltrate secrets via tools (`rg`, `make`, Docker, etc.). Commenters argue the real fix is at the OS/sandbox level: run agents in containers or separate users with least-privilege access, not global blocklists. Others propose harness-level redaction and better secret handling (avoiding `.env`, using proxies, local-first data) but emphasize that ignore files alone give a dangerous illusion of safety.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Security should live in the OS: separate users, containers, Firecracker VMs; blocklists are brittle. — counterpoint: many users reasonably expect a simple `.agentignore`-style UX.

- Better UX: agent sessions run in fresh sandboxes seeded with a low-risk project folder and scoped tokens, making file access opt-in instead of opt-out.

- Secrets strategy must change: stop storing real creds in `.env`, use agents/proxies and local-only dev data so accidental exfiltration has limited blast radius.

---

### LLM perspective
- View: Treat the coding agent as an untrusted program; design its filesystem, network, and credentials like production infrastructure, not like a friendly editor.

- Impact: Developers, DevOps, and security teams must own agent environments, not rely on per-tool config knobs or pattern-based ignore lists.

- Watch next: Standardized “dev agent sandbox” templates, IDE integrations for least-privilege containers, and benchmarks measuring real-world secret exfiltration rates under different setups.
