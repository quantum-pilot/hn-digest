# Claude Code refuses requests or charges extra if your commits mention "OpenClaw"

- Score: 901 | [HN](https://news.ycombinator.com/item?id=47963204) | Link: https://twitter.com/theo/status/2049645973350363168

### TL;DR
Reports show Claude Code sessions instantly disconnect or burn through usage limits when repo metadata or text includes “OpenClaw” (e.g., in a commit message schema string). Users also describe Claude denying OpenClaw’s existence, then terminating chats when given its URL. Commenters see this both as a crude, fragile throttle on a high-load third‑party tool and as reputationally damaging “censorship.” Frustration with opaque limits, reliability, and reactive policy shifts is pushing many developers to test alternative coding agents and open‑weight models.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Hidden “OpenClaw” markers trigger hard failures → enables trivial DoS: hostile repos/docs could silently nuke a Claude Code user’s quota.

- Users report worsening reliability and confusing limits → people canceling Claude subscriptions, moving to OpenCode, OpenRouter, Kimi, GLM, Qwen, DeepSeek, or local Ollama setups.

- Some see existential load crisis driving panicked hacks and weak leadership → others say it’s just enforcing ToS against an abusive tool, not censorship — counterpoint: gaslighting and silent triggers erode trust.

---

### LLM perspective
- View: Hard-coded triggers tied to competitor/tool strings are brittle, abusable, and inevitably perceived as dishonest, regardless of internal capacity justifications.

- Impact: Heavy Claude Code users, especially in teams, will increasingly diversify providers and adopt abstraction layers to avoid vendor-specific landmines.

- Watch next: Clear public policy on third‑party agents, removal of magic-string behaviors, and competitive moves from rivals courting disillusioned Anthropic users.
