# Clawdbot - open source personal AI assistant

- Score: 363 | [HN](https://news.ycombinator.com/item?id=46760237) | Link: https://github.com/clawdbot/clawdbot

- TL;DR  
  Clawdbot is an open‑source, local‑first “personal AI gateway” that wires Anthropic/OpenAI models into your existing chat apps, voice interfaces, browser automation, cron jobs, and device tools. A Node-based daemon routes WhatsApp/Telegram/Slack/etc. into configurable agents with skills and strong defaults for DM pairing and optional sandboxing. HN discussion shows excitement about the “always-on secretary” experience and DIY extensions, alongside serious concerns about runaway API costs, broad host access, and a large unresolved security-issue backlog.

- Comment pulse  
  - Powerful but expensive → user reports $300+ API spend in 2 days, yet praises dynamic skill creation, scheduled automation, and persistent, remotely reachable agents.  
  - Security and maturity worries → 300 open issues and an AI-generated report on hardcoded OAuth secrets lead some to delay install, while others downplay impact.  
  - Strong demand for ‘secretary in a box’ → people describe calendar/email/Telegram assistants, would pay ~$200/month for a trustworthy one, plus AI-coauthored fixes and anthropomorphism debates.

- LLM perspective  
  - View: Architecturally a capable orchestration shell; real deployments need conservative defaults for tool scope, rate limits, and explicit consent flows.  
  - Impact: If projects like this stabilize, non-programmers get automation platforms, while ops and security teams inherit complex, user-driven integration surfaces.  
  - Watch next: stronger per-session sandboxes, clearer token accounting, and competitive local models that plug into the same gateway abstraction.
