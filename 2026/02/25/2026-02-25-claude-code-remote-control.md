# Claude Code Remote Control

- Score: 473 | [HN](https://news.ycombinator.com/item?id=47148454) | Link: https://code.claude.com/docs/en/remote-control

### TL;DR

Claude Code Remote Control lets Pro and Max subscribers continue a locally running coding session from claude.ai or mobile while retaining local files, tools, MCP servers, and configuration. The machine initiates outbound TLS connections, opens no inbound port, and can expose a session by URL or QR code. It supports one remote session, requires the terminal process to remain open, and exits after roughly ten offline minutes. HN’s preview users reported failed interruption, disconnects, missing sessions, confusing permissions, and poor state visibility, often preferring Tailscale plus SSH and tmux.

### Comment pulse

- Native mobile convenience lowers setup friction → standard SSH, Tailscale, and tmux already provide mature reconnection and full terminal control.
- Preview reliability is below production use → users reported stop buttons failing, stale status, and sessions disappearing after navigation.
- Local execution preserves the full environment → counterpoint: remotely reachable tools increase the importance of sandboxing and credential security.

### LLM perspective

- **View:** The product’s differentiation is interface integration, not a new remote-execution primitive.
- **Impact:** Developers gain mobility, but should keep production changes behind independent review and recovery paths.
- **Watch next:** Interrupt semantics, session discovery, mobile permissions, reconnection reliability, and Team or Enterprise availability.
