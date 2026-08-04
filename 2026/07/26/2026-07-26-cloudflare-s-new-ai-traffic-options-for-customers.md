# Cloudflare's new AI traffic options for customers

- Score: 187 | [HN](https://news.ycombinator.com/item?id=49052564) | Link: https://blog.cloudflare.com/content-independence-day-ai-options/

### TL;DR

Cloudflare now lets every customer independently allow or block crawlers used for Search, user-directed Agents, and model Training. From September 15, new domains will block Training and Agent traffic by default on ad-supported pages while allowing Search; multipurpose crawlers such as Googlebot, Applebot, and BingBot inherit their most restrictive classification. Enterprise BotBase adds behavior visibility, planned content-use controls, and immediate/reference/full preferences, while verification becomes category-specific. Hacker News welcomed separating search from training but worried Cloudflare is centralizing web access, impairing personal agents, and positioning itself as a toll collector.

### Comment pulse

- Google’s combined crawler creates a coercive choice → publishers accepting search discovery also accept Gemini training unless infrastructure separates those purposes.
- Middle-path governance divides opinion → supporters see permission and compensation tools — counterpoint: critics see Cloudflare deciding access across more than 20% of domains.
- Proof-of-work is no clean alternative → headless browsers bypass challenges, while old hardware and low-end phones can wait minutes.

### LLM perspective

- **View:** Purpose-based controls are more durable than an AI label because one crawler can search, act, train, transact, or monitor.
- **Impact:** Bot operators gain incentives to split identities and honor declared uses, or lose verified reach across Cloudflare’s network.
- **Watch next:** Measure false blocks, referral losses, crawler separation, agent task failures, and adoption of the proposed Forwarded identity header.
