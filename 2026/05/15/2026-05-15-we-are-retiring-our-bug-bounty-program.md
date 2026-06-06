# We are retiring our bug bounty program

- Score: 344 | [HN](https://news.ycombinator.com/item?id=48148391) | Link: https://turso.tech/blog/the-wonders-of-ai

### TL;DR
Turso, which is rewriting SQLite, is shutting down its $1,000 data‑corruption bug bounty. Initially it worked well: five high-caliber contributors found rare issues, sometimes using LLMs and formal methods, even uncovering SQLite bugs. After widespread AI “slop,” the bounty became a magnet for junk PRs: fabricated exploits, intentional self-corruption, and endless LLM-generated arguing. The cost asymmetry (minutes to generate, hours to review) made it untenable. Turso will keep contributions open but remove cash incentives, and calls for new OSS governance patterns.

---

### Comment pulse
- Core scarcity is attention, not code → reading, understanding, and reviewing dominate; AI makes high-volume “tactical tornado” behavior cheaper — counterpoint: strong tests can justify rare, big refactors.
- Bot honeypots now exist to attract/measure bounty-seeking agents; unclear why some spam repos with no payouts, suggesting misconfigured or cheaply run agents.
- Proposal: refundable submission fees to deter spam; pushback: reputational risk, payment overhead, and even stronger incentives to litigate “you misclassified my bug.”

---

### LLM perspective
- View: Un-gated cash bounties plus cheap LLMs create a denial-of-service on maintainer time; economic incentives dominate good-faith norms.
- Impact: Security and reliability work may shift toward trusted circles, vendors, or platforms instead of open bounties for anyone.
- Watch next: Platform-level anti-spam, staking/escrow models for bug bounties, and contribution systems that require minimal proof-of-work before review.
