# Push events into a running session with channels

- Score: 391 | [HN](https://news.ycombinator.com/item?id=47448524) | Link: https://code.claude.com/docs/en/channels

### TL;DR
Anthropic’s new Claude Code “channels” let an MCP server push events (chat messages, webhooks, CI alerts) into an already-running local Claude session, and optionally receive replies back through the same channel. Initial plugins ship for Telegram, Discord, and a local “fakechat” demo, with strict allowlists, enterprise toggles, and a research-preview allowlist for plugins. HN discussion praises Telegram’s bot API, notes similarities to unofficial *claws setups, and raises concerns about Anthropic’s pace, polish, and walled-garden trajectory.

---

### Comment pulse
- Telegram-first choice → Devs love its simple, robust bot API and use it mainly as a bot platform, not messaging—counterpoint: some expected Slack/Teams given Anthropic’s enterprise focus.  
- Ecosystem comparison → Pi.dev already has many “channel-like” plugins and easy extension via prompting, making Anthropic look slow and more locked down.  
- Channels’ role → Seen as an official, ToS-compliant *claws-style bridge using MCP and local sessions; fits enterprise security, but some distrust Anthropic and see features as hype-driven.

---

### LLM perspective
- View: Channels normalize “AI agent as a local hub” that reacts to real-time events instead of isolated cloud jobs.  
- Impact: Benefits power users, ops/dev teams, and bot builders who want Claude near their code and infra without new cloud wiring.  
- Watch next: Broader plugin whitelisting, richer non-chat channels (CI, monitoring), and tighter mobile/desktop UX to avoid feeling like a brittle preview.
