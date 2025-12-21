# Go ahead, self-host Postgres

- Score: 394 | [HN](https://news.ycombinator.com/item?id=46336947) | Link: https://pierce.dev/notes/go-ahead-self-host-postgres#user-content-fn-1

### TL;DR
Author argues that fears around self-hosting Postgres are overstated: managed services mostly run standard Postgres with automation and a high markup. He migrated from AWS RDS to a dedicated server, saw equal or better performance, and now spends roughly an hour a month on backups, updates, and monitoring for millions of queries daily. He suggests self-hosting suits most non-regulated, non-hyperscale workloads, while HN commenters debate responsibility, the real value of “managed” features, and long‑term cost versus convenience.

---

### Comment pulse
- Using AWS shifts responsibility → for client projects, outages become “AWS is down”, easing politics — counterpoint: customers don't care whose logo is on downtime.  
- Self-hosting fits tight budgets and modest scale → saving hundreds monthly is worth 1–2 hours of DBA chores; cloud databases still consume similar attention.  
- Some define “managed DB” as DR, multi-region failover, PITR, insights → if cheap, that beats DIY — counterpoint: automation and self-hosting can approach this.  

---

### LLM perspective
- View: Self-hosted Postgres is viable for many, but only if teams treat it like core infra: monitoring, documentation, and runbooks are non-optional.  
- Impact: Cost-sensitive SaaS, internal tools, and data-heavy startups gain most; compliance-heavy or globally distributed consumer apps likely still prefer managed offerings.  
- Watch next: Track open-source automation stacks (autopg, vitabaks/autobase, Kubernetes operators) and cloud serverless Postgres pricing; the crossover point will decide many future architectures.
