# Telegram Serverless

- Score: 174 | [HN](https://news.ycombinator.com/item?id=48918534) | Link: https://core.telegram.org/bots/serverless

### TL;DR

Telegram Serverless is a managed backend for bots and Mini Apps: JavaScript handlers run on demand in isolated V8 environments beside the Bot API, with persistent SQLite-backed storage and outbound HTTP built in. Its CLI supports local diffs, test runs, atomic code pushes, explicit schema migrations, and conflict detection; BotFather exposes the same project controls on mobile. The constrained runtime has no npm packages or filesystem. HN readers welcomed the integrated database but treated the closed beta as operationally underspecified and debated whether Telegram’s convenience justified its privacy tradeoffs.

### Comment pulse

- Bot ecosystems split opinion → some want Signal’s developer ergonomics — counterpoint: others value its lack of bots and distrust Telegram bot privacy.
- Missing platform basics concern developers → secure secrets, scheduled tasks, TypeScript, and external packages are absent or undocumented.
- Business constraints remain opaque → commenters found no published execution quotas, database caps, pricing, or durable commercial model.

### LLM perspective

- **View:** This is less generic serverless than a vertically integrated Telegram runtime; simplicity comes from tight capability boundaries.
- **Impact:** Small bots can eliminate hosting operations, while complex integrations may outgrow the SDK before infrastructure would have become burdensome.
- **Watch next:** Benchmark handler latency, concurrent database writes, deployment conflict handling, and migration recovery before production use.
