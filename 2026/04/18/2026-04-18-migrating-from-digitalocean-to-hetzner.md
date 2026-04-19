# Migrating from DigitalOcean to Hetzner

- Score: 661 | [HN](https://news.ycombinator.com/item?id=47815774) | Link: https://isayeter.com/posts/digitalocean-to-hetzner-migration/

### TL;DR
A Turkish software company cut monthly infrastructure spend from $1,432 on a single large DigitalOcean droplet to $233 on a more powerful Hetzner dedicated box. They migrated 248 GB of MySQL, 34 Nginx sites, GitLab, Neo4j and workers with zero downtime using MySQL replication, rsync, DNS TTL tuning, and scripted Nginx reverse-proxy cutover, plus a MySQL 5.7→8.0 upgrade. HN discussions focus on cloud lock‑in and egress fees, Hetzner’s value, AI‑assisted migrations, and tradeoffs around redundancy vs simplicity.

---

### Comment pulse
- Cloud lock‑in is costly → AWS prices and egress fees push people to Hetzner; EU rules now force some free egress—counterpoint: waivers may be limited.  
- Hetzner value praised → Users report huge savings and good support; some used Claude to rewrite legacy stacks—counterpoint: others resent AI marketing and storytelling creep.  
- Reliability tradeoffs debated → Critics dislike single big server without HA; defenders prefer simpler, cheaper setups; others advocate multi-node bare metal with Kubernetes.

---

### LLM perspective
- View: For steady, monolithic workloads, scripted replication plus reverse-proxy cutover makes cloud-to-bare-metal moves both safe and economical.  
- Impact: Small companies in weak-currency regions gain most; they can reclaim tens of thousands yearly without sacrificing performance.  
- Watch next: More turnkey migration scripts, LLM-assisted refactors, and legal pressure on cloud egress pricing will further reduce provider lock-in.
