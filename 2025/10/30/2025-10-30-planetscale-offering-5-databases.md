# PlanetScale Offering $5 Databases

- Score: 117 | [HN](https://news.ycombinator.com/item?id=45761027) | Link: https://planetscale.com/blog/5-dollar-planetscale

TL;DR
- PlanetScale introduced a $5/month single‑node, non‑HA Postgres tier (PS‑5), with vertical scaling and a path to its multi‑AZ HA tiers (from $30). It targets dev/test and small workloads while keeping an upgrade path within the same platform.
- HN discussion centers on latency from not colocating compute and DB, the difficulty of PS’s high‑performance storage approach versus EBS/NVMe claims from rivals, and comparisons to budget dev tiers like Neon; Azure users lament weak managed PG options.

Comment pulse
- Co‑locate compute and DB → big latency gains; cross‑region RTT dominates; in‑region can match typical AWS latencies.
- Dedicated NVMe + sync replication beats EBS → operationally hard; vendors avoid it — counterpoint: NVMe‑over‑fabrics can match, but PlanetScale disputes.
- $5 tier suits dev/test pipelines on tight budgets; Neon cited as working alternative; Azure PG users frustrated by HA/maintenance limitations.

LLM perspective
- View: Entry pricing is a funnel: win early projects, upsell to HA; trade durability for affordability.
- Impact: Helps startups, CI environments, hobby apps; pressures Neon, Supabase, RDS on low-end pricing.
- Watch next: Seamless upgrades from single-node to HA, region coverage, concrete durability guarantees, and independent benchmarks vs EBS/NVMe competitors.
