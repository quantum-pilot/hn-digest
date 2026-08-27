# PlanetScale Offering $5 Databases

- Score: 117 | [HN](https://news.ycombinator.com/item?id=45761027) | Link: https://planetscale.com/blog/5-dollar-planetscale

### TL;DR

PlanetScale plans to roll out single-node Postgres over the coming months, led by a $5 monthly PS-5 tier for development, testing, and other non-critical workloads. Unlike its existing three-node, multi-availability-zone starter configuration, the new mode is explicitly non-HA, although customers can scale vertically without adding replicas. Listed single-node options range from $5 to $13, while HA starts at $30. HN commenters welcome affordable test databases but emphasize region co-location, latency, provider availability, and competing low-cost services.

### Comment pulse

- The tier fits shoestring development → teams can provision realistic Postgres environments without paying for three-node availability.
- Geography remains decisive → application compute and PlanetScale should share a city or region to avoid damaging latency.
- Infrastructure differentiates providers → commenters debate PlanetScale’s local-NVMe replication versus alternatives built on networked storage.

### LLM perspective

- View: PlanetScale is separating premium availability from its operational tooling to lower the adoption floor.
- Impact: Small projects can start on the same platform, but must accept a single failure domain.
- Watch next: Verify launch timing, regions, storage limits, backup behavior, latency, and vertical-scaling downtime.
