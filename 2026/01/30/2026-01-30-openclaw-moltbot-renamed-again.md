# OpenClaw – Moltbot Renamed Again

- Score: 593 | [HN](https://news.ycombinator.com/item?id=46820783) | Link: https://openclaw.ai/blog/introducing-openclaw

### TL;DR
OpenClaw is the rebranded Clawdbot/Moltbot, an open‑source agent platform that hooks LLMs into WhatsApp, Slack, email, and other chat apps while running on your own hardware. The new release adds more channels, models, web image support, and a heavy emphasis on security via hardening work, formal models, and guidance. HN reactions mix excitement with concern over prompt‑injection, opt‑in sandboxing, npm supply‑chain risk, and expensive cloud token usage, with many urging local models and safer defaults.

### Comment pulse
- Security feels precarious → prompt injection plus opt‑in sandboxing make it seem like LLM‑controlled RCE—counterpoint: some praise strong docs and early formal security models.  
- Cloud usage can be shockingly expensive → casual experimentation burned $5–$560 in Claude tokens; users suggest local models, cheaper APIs, or Clawdbot token‑optimization.  
- People admire the creator’s track record → but some struggle to see what OpenClaw adds over Claude Code or Pi beyond heartbeat and chat‑app glue.  

### LLM perspective
- View: This is an orchestration layer turning chat apps into a unified personal agent surface; differentiation hinges on reliability and safety.  
- Impact: If security and governance mature, always‑on agents managing inboxes and calendars could become normal for power users and small teams.  
- Watch next: Watch adoption of default‑on sandboxing, third‑party audits, token‑cost controls, and high‑quality local models as leading indicators of sustainable success.
