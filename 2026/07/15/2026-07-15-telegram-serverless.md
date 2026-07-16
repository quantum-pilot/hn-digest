# Telegram Serverless

- Score: 174 | [HN](https://news.ycombinator.com/item?id=48918534) | Link: https://core.telegram.org/bots/serverless

### TL;DR
Telegram Serverless is a new backend platform that runs your bot and Mini App logic directly on Telegram’s infrastructure. You write plain JavaScript (no npm deps) in a simple project layout, deploy via `tgcloud push`, and get fast V8 isolates plus a built‑in SQLite database and HTTP `fetch`. Schema changes use guided migrations; testing uses `tgcloud run`. Tooling is optimized for AI coding assistants. HN readers like the convenience but question quotas, pricing, security, and missing features like secrets management and cron.

---

### Comment pulse
- Convenience and power → Built‑in SQLite and serverless hosting are appealing, but people want clear limits on execution time, DB size, and quotas.  
- Business model worries → Closed beta, no pricing; some fear lock‑in to an unclear, possibly crypto‑subsidized business.  
- Security and ergonomics → Telegram bots aren’t E2E; some prefer Signal despite no bot API. Devs miss secrets storage, npm, cron, and TypeScript—counterpoint: simplicity keeps runtime small and safe.

---

### LLM perspective
- View: This is effectively “Cloudflare Workers, but only for Telegram,” tightly scoped and opinionated around bots.  
- Impact: Lowers the bar for hobby and SMB bots; larger teams will hesitate until limits, pricing, and reliability stories mature.  
- Watch next: Official quotas/pricing, secrets and scheduling features, file upload support, and whether Telegram opens this model beyond bots.
