# Migrating from DigitalOcean to Hetzner

- Score: 661 | [HN](https://news.ycombinator.com/item?id=47815774) | Link: https://isayeter.com/posts/digitalocean-to-hetzner-migration/

### TL;DR

A Turkish software company moved a steady-state production stack from a $1,432-per-month DigitalOcean VM to a $233 Hetzner dedicated server, gaining CPU and RAM while saving $14,388 annually. Its 24-hour, zero-downtime migration covered 248 GB across 30 MySQL databases, 34 Nginx sites, GitLab, Neo4j, workers, and live apps. Parallel dump/load plus replication kept data current; lowered DNS TTLs and an old-server reverse proxy bridged cutover. The move also upgraded CentOS 7 and MySQL 5.7, exposing schema, duplicate-row, privilege, and webhook issues. Hacker News admired the economics but questioned single-server resilience.

### Comment pulse

- The old deployment was already a single VM — counterpoint: a single bare-metal host trades cloud recovery options for one physical failure domain.
- Commenters argued many services can tolerate occasional downtime, and that simple, overprovisioned systems may outlive elaborate high-availability stacks.
- AI-assisted migration may erode provider lock-in by reducing legacy glue work, though readers disliked the article’s apparent machine-written repetition.

### LLM perspective

- **View:** The real optimization was matching steady-state workload needs to dedicated hardware, not proving one provider universally superior.
- **Impact:** Replication and proxying converted a risky big-bang move into reversible stages while delivering an 84% monthly cost reduction.
- **Watch next:** Backups, disaster recovery, hardware replacement, replica strategy, monitoring, provider egress policy, and whether operational labor erodes savings.
