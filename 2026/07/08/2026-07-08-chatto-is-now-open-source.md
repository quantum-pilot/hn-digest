# Chatto is now open source

- Score: 671 | [HN](https://news.ycombinator.com/item?id=48833116) | Link: https://www.hmans.dev/blog/chatto-is-open-source

### TL;DR
Chatto, a newly open‑sourced real‑time chat/communications server, is designed for very simple self‑hosting: a single binary plus NATS for messaging, optional S3 storage, and LiveKit for calls. HN commenters praise the clear deployment guidance and flexibility, and the solo creator’s use of “agentic coding” to build it. Questions center on client support (desktop/mobile), cheap hosting targets like Cloudflare/Vercel, and enterprise data retention vs. per‑user key deletion, plus naming/branding quirks and mobile push-notification hurdles.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Self‑hosting focus → Single compact binary, NATS, LiveKit, S3; strong docs make private deployments appealing—counterpoint: unclear desktop client availability and PaaS friendliness.
- Adoption concerns → Enterprises need soft‑delete and employer‑owned history, clashing with per‑user key shredding; mobile apps and push infra are must‑haves.
- Social/branding layer → Heavy praise for the author and agentic coding; some turned off by fanboy tone and “chato”/“chato” naming issues in major languages.

---

### LLM perspective
- View: Interesting reference architecture for self‑hosted, AI‑era comms built around small components and strong docs.
- Impact: Helps startups, privacy‑sensitive teams, and hobbyists run Slack‑style chat and calls entirely on their own infra.
- Watch next: Benchmarks under load, quality of official clients, hosted/SaaS option, and how governance and contributions evolve post–open sourcing.
