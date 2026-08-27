# Migrating from AWS to Hetzner

- Score: 1006 | [HN](https://news.ycombinator.com/item?id=45614922) | Link: https://digitalsociety.coop/posts/migrating-to-hetzner-cloud/

### TL;DR

Digital Society says migrating workloads from AWS and DigitalOcean to Hetzner cut its peak monthly cloud bill 76%, from $559.36 to $132.96, while workload capacity rose from 12 to 44 vCPUs and 24 to 88 GiB RAM. Its replacement stack uses Kubernetes on Talos Linux, CloudNativePG, ingress-nginx, ExternalDNS, cert-manager, Terraform, and Helm. Tradeoffs included self-management, cross-location latency, database operations, and underestimated deployment automation. Commenters stressed that savings depend heavily on requirements and operational expertise.

### Comment pulse

- Hetzner cloud delivers strong price-performance → managed security, backups, failover, and support remain real labor costs.
- Dedicated servers may save even more → slower scaling and greater operational ownership suit only some workloads.
- Infrastructure advice needs context → a small SaaS and a global enterprise optimize for different risks.

### LLM perspective

- View: The migration exchanges provider services for internal operational competence, not merely one invoice for another.
- Impact: Experienced small teams can buy substantial capacity while accepting narrower resilience and service guarantees.
- Watch next: Measure staff time, recovery tests, security patching, and single-location failures alongside monthly bills.
