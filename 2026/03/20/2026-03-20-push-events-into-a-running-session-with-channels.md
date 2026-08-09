# Push events into a running session with channels

- Score: 391 | [HN](https://news.ycombinator.com/item?id=47448524) | Link: https://code.claude.com/docs/en/channels

### TL;DR

Claude Code channels let an MCP server push alerts, messages, or webhooks into an already-running local session, where the agent retains files and context and can reply through the same route. The research preview supports Telegram, Discord, and localhost fakechat; it requires Claude Code 2.1.80+, Bun, claude.ai authentication, and allowlisted plugins. Events arrive only while the session runs, pairing restricts senders, and permission prompts can still halt unattended work. HN readers welcomed the practical local automation loop but some called the tooling rushed.

### Comment pulse

- Developers favored Telegram because its bot API is simple, free, and lightweight compared with enterprise chat platforms.
- Compared with custom “claws,” channels invert control: Claude Code starts the MCP transport and owns the process lifecycle.
- Local hosting appealed to security-minded readers — counterpoint: others feared sessions would eventually move into Anthropic’s walled garden.

### LLM perspective

- **View:** Push turns an invoked tool into a context-holding event consumer.
- **Impact:** CI, monitoring, and chat can converge on one live workspace without polling.
- **Watch next:** Protocol stability, custom-channel access, auditability, and safer unattended permission handling.
