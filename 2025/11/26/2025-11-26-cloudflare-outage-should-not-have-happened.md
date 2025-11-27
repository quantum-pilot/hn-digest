# Cloudflare outage should not have happened

- Score: 124 | [HN](https://news.ycombinator.com/item?id=46059227) | Link: https://ebellani.github.io/blog/2025/cloudflare-outage-should-not-have-happened-and-they-seem-to-be-missing-the-point-on-how-to-avoid-it-in-the-future/

### TL;DR
The blog argues Cloudflare’s global outage stemmed from a logical single point of failure: a central ClickHouse query whose unconstrained result set, exposed by a security-related permissions change, produced oversized ML feature files that crashed core systems. The author claims Cloudflare fixates on physical redundancy and rollout mechanics instead of eliminating logical coupling via strict relational design (no NULLs, full normalization) and formally verified code. HN commenters largely push back, citing feasibility, cost, and simpler explanations like deployment strategy and query review.

---

### Comment pulse
- Formal rigor is ideal but impractical → Fully normalized schemas and formal verification radically slow teams and restrict hiring; better fit for narrow, ultra-critical components—counterpoint: at Cloudflare’s scale, “insulin-pump” rigor is warranted.  
- Root cause differs → Many see this as a bad query plus global, rapid rollout, not a ClickHouse vs PostgreSQL or normalization problem; gradual deployments defend better than “perfect” code.  
- Value of critique debated → Some dismiss the post as unhelpful Monday-morning quarterbacking; others find it educational and spin off concrete ideas like Rust features for panic-free critical paths.

---

### LLM perspective
- View: Treat ML-derived configs and analytics pipelines as code: versioned, rollbackable, with blast-radius limits, not just “data plumbing.”  
- Impact: Cloud and security infra vendors must separate “experiment fast” layers from a locked-down, verifiably safe control plane.  
- Watch next: Postmortems detailing staged rollouts for model features, config validation services, and language/runtime safeguards against catastrophic panics in core paths.
