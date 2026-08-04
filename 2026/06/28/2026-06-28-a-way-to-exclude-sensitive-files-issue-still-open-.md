# A way to exclude sensitive files issue still open for OpenAI Codex

- Score: 172 | [HN](https://news.ycombinator.com/item?id=48706714) | Link: https://github.com/openai/codex/issues/2847

### TL;DR

A Codex request sought repository and global deny rules for sensitive paths such as `.env`, keys, and credentials, enforceable across direct reads and shell tools. OpenAI pointed to beta permission profiles and `/permissions`, then closed the issue as completed. However, a Windows report says identical user configuration is honored by CLI 0.145.0 but ignored by the Codex App, where parity remains unfinished. HN argued ignore files are insufficient security boundaries: agents need OS-enforced, least-privilege containers or users, restricted mounts, and scoped credentials.

### Comment pulse

- Put enforcement below the model → OS permissions, Landlock, containers, and bind mounts can block shell tools and alternate access paths that ignore harness-level rules.
- Least privilege should be opt-in → copy only task-needed code and scoped credentials into disposable sandboxes instead of exposing a whole workstation.
- Blocklists can still reduce accidents → harnesses may redact tool output and secret-like strings — counterpoint: clever agents can transform content, creating false assurance.

### LLM perspective

- **View:** An agent’s effective read authority equals every capability reachable through its tools, not merely its named file-reading API.
- **Impact:** Security teams need reproducible task sandboxes that preserve builds while withholding unrelated secrets, production data, and privileged sockets.
- **Watch next:** Verify CLI, app, IDE, subprocess, Docker, and remote-agent parity with adversarial tests before treating permissions as a control.
