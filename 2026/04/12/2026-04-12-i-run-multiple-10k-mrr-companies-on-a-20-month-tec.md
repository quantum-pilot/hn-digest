# I run multiple $10K MRR companies on a $20/month tech stack

- Score: 812 | [HN](https://news.ycombinator.com/item?id=47736555) | Link: https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack

### TL;DR
The author runs several ~$10k MRR SaaS products on ~\$20/month by aggressively simplifying: a single cheap VPS, Go binaries, SQLite with WAL, local GPUs for heavy batch AI, and OpenRouter + Copilot for interactive AI and coding. This keeps infra trivial, costs tiny, and runway long, avoiding premature “enterprise” complexity and VC pressure. HN discussion largely agrees on starting lean, but debates SQLite vs Postgres, VPS vs bigger/dedicated hardware, and how far 1GB RAM frugality should go.

---

### Comment pulse
- SQLite as primary DB → amazing single-box performance; WAL, app-managed write queue, Litestream-style replication—counterpoint: Postgres on localhost gives easier reporting, HA, scaling paths.  
- “Just use a VPS” → overclouded apps waste money and complexity; simple monoliths suffice early—counterpoint: backups and ops discipline remain non-optional.  
- Hardware strategy → mix of tiny VPS, cheap Hetzner/OVH dedicated boxes, Proxmox, containers; debate whether 1GB RAM is smart constraint or pointless self‑punishment.

---

### LLM perspective
- View: This playbook fits solo bootstrappers optimizing for simplicity and margin, not VC-scale, compliance-heavy, or multi-team systems.  
- Impact: Normalizes questioning cloud defaults; may shift some indie devs back to monoliths, SQLite, and owned GPUs for AI workloads.  
- Watch next: Real-world perf/cost case studies comparing lean VPS+SQLite+local-AI vs managed cloud at different traffic and team sizes.
