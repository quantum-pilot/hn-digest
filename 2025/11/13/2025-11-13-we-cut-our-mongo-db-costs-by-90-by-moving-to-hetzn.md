# We cut our Mongo DB costs by 90% by moving to Hetzner

- Score: 211 | [HN](https://news.ycombinator.com/item?id=45915884) | Link: https://prosopo.io/blog/we-cut-our-mongodb-costs-by-90-percent/

TL;DR
Prosopo cut MongoDB costs ~90% by moving a 500 GB Atlas M40 deployment on AWS (~$3k+/mo; backups and ~$1k internet egress dominated) to a single Hetzner dedicated server (~$160/mo; 8 cores, 256 GB RAM, NVMe). Their ML/offline workload tolerates some downtime; self-managing (Proxmox/Docker, VPN/firewall, Ansible, OpenObserve, mongodump backups) improved performance via large RAM. HN debates the trade: big savings vs lower multi-AZ resilience, encryption-at-rest gaps, and hidden ops salaries; some argue AWS bandwidth pricing often drives bills more than compute.

Comment pulse
- Single server lacks Atlas-style HA → multi-AZ clusters are more resilient; DIY adds on-call/patching — counterpoint: Hetzner bandwidth ~$1.20/TB vs AWS far higher.
- Savings may be illusory → $2–3k/mo can be cheaper than a FTE to operate, monitor, secure, and upgrade databases.
- Beware data-at-rest gaps → Hetzner bare metal lacks default disk encryption; use LUKS or equivalent to reduce decommission/leak risks.

LLM perspective
- View: Cost win hinges on egress-heavy, downtime-tolerant workloads; big RAM boxes beat mid-tier managed nodes for performance.
- Impact: Teams with cross-cloud stacks, EU data residency, or ML preprocessing can benefit; pure SaaS backends may not.
- Watch next: Add Hetzner multi-DC replication, test restores/DR, publish uptime and bandwidth stats; compare Atlas PrivateLink/peering to curb egress.
