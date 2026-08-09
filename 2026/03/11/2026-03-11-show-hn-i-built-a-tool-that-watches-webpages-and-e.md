# Show HN: I built a tool that watches webpages and exposes changes as RSS

- Score: 139 | [HN](https://news.ycombinator.com/item?id=47337607) | Link: https://sitespy.app

### TL;DR

Site Spy monitors webpages in a real browser, records text and optional screenshot snapshots, highlights additions and removals, and publishes changes through RSS, email, push, Telegram, webhooks, an API, or MCP. Users can select an element or describe a desired signal such as price drops; AI filters noise. The free tier covers two hourly watches, with paid plans adding faster checks, more history, browser steps, and team features. Commenters like the diff-first execution but note established self-hosted alternatives and ask about anti-bot defenses, login sessions, and audience-specific alert channels.

### Comment pulse

- Real-browser rendering handles JavaScript sites → aggressive bot protection and complicated authentication remain harder than dynamic HTML itself.
- RSS is an open integration layer → urgent events usually fit push or email, while feed readers suit changes that can wait.
- Convenience is the differentiation → counterpoint: changedetection.io and urlwatch already offer capable free, self-hosted monitoring.

### LLM perspective

- **View:** The product wins if setup and signal quality justify outsourcing a mature monitoring problem.
- **Impact:** Reporters, shoppers, job seekers, and agents gain structured change histories without writing scrapers.
- **Watch next:** Filter accuracy, false negatives, browser-step reliability, anti-bot failure messages, and AI-summary availability.
