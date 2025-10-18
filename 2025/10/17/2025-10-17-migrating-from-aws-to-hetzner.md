# Migrating from AWS to Hetzner

- Score: 1006 | [HN](https://news.ycombinator.com/item?id=45614922) | Link: https://digitalsociety.coop/posts/migrating-to-hetzner-cloud/

- TL;DR
  - Digital Society moved workloads from AWS and DigitalOcean to Hetzner Cloud, rebuilding on Kubernetes with Talos Linux and CloudNativePG. Result: 76% lower monthly costs ($559→$133) while tripling available CPU/RAM. Tradeoffs: Hetzner’s “locations” had high cross-site latency, so they consolidated in one location with placement groups; migrating ECS configs to K8s took unexpected effort, solved with Kustomize and repo-based config. HN debates emphasize dedicated Hetzner bare metal for even better price/perf, caution about ops/security overhead, and the need to rebuild managed-DB capabilities.

- Comment pulse
  - Dedicated servers: ~2x perf, ~10x cheaper from low latency and NVMe; autoscalers less needed; stable bills — counterpoint: ops cost; this post used cloud VMs.
  - Leaving AWS means rebuilding Postgres ops: backups, failover, monitoring. Options: CloudNativePG, Elephant-Shed, or managed services on Hetzner; some prefer Big Cloud for security/compliance comfort.
  - Context matters: needs and skills vary; vendor influence can bias toward pricey serverless; dedicated setups scale slower but simplify architecture and reduce costs.

- LLM perspective
  - View: Self-managed K8s on Hetzner Cloud plus Talos/CloudNativePG is viable if you accept single-location design and operational responsibility.
  - Impact: Best for bootstrapped EU SaaS with spiky compute/data; fewer AWS features, but big savings fund product work instead of infra.
  - Watch next: Measure cross-location latency and failover; evaluate managed Postgres-on-Hetzner benchmarks; monitor Hetzner object storage SLAs, egress/I/O pricing, and ARM VM stability.
