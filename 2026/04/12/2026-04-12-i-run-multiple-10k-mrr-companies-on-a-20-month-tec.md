# I run multiple $10K MRR companies on a $20/month tech stack

- Score: 812 | [HN](https://news.ycombinator.com/item?id=47736555) | Link: https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack

### TL;DR

The author bootstraps several revenue-generating products with a single $5–10 VPS, statically compiled Go services, SQLite in WAL mode, and local GPU inference for batch AI, using OpenRouter only for frontier-model requests and GitHub Copilot for development. The thesis is that low burn creates venture-like runway while keeping deployment understandable and delaying scaling infrastructure until demand exists. Commenters broadly endorsed avoiding Kubernetes and cloud sprawl, while debating SQLite versus local Postgres, Go versus higher-memory runtimes, and whether extreme $5 constraints distract from the business. Backups and server hardening remain essential.

### Comment pulse

- SQLite minimizes latency and operations; local Postgres adds reporting, replicas, HA paths, and richer features with modest overhead.
- Cloud sales narratives normalize premature complexity. — counterpoint: self-hosting transfers security, backup, hardware, and availability responsibility to the founder.
- Some favor a larger shared server or $20 VPS, arguing marginal RAM cost matters less than customer value.

### LLM perspective

- **View:** Simplicity compounds when it shortens debugging, deployment, and financial runway simultaneously.
- **Impact:** Solo founders can validate demand before committing to managed infrastructure or fundraising.
- **Watch next:** Test restores, off-provider backups, resource saturation, concurrent-write latency, and a documented migration threshold.
