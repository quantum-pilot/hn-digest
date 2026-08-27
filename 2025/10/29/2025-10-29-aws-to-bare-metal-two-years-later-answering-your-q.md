# AWS to bare metal two years later: Answering your questions about leaving AWS

- Score: 700 | [HN](https://news.ycombinator.com/item?id=45745281) | Link: https://oneuptime.com/blog/post/2025-10-29-aws-to-bare-metal-two-years-later/view

### TL;DR

Two years after moving steady workloads from AWS, OneUptime reports saving over $1.2 million annually, 99.993% availability across 730 days, and 19% lower latency. It now runs two provider-separated European racks with replicated storage, out-of-band access, quarterly failover drills, and about 14 engineer-hours monthly toil. The company still uses AWS for archives, edge delivery, and burst tests. Its conclusion is conditional: colocation suits stable baseload and capable platform teams; cloud remains preferable for elasticity and valuable managed services.

### Comment pulse

- Supporters emphasized cloud premiums, egress costs, and organizational lock-in for workloads that remain continuously provisioned.
- Skeptics warned self-hosting costs surface later through scarce expertise, undocumented systems, hardware failures, and staff turnover.

### LLM perspective

- View: The case supports workload-specific unbundling, not a general verdict that bare metal beats cloud.
- Impact: Mature teams with predictable demand can redirect infrastructure rent into capacity while assuming lifecycle responsibility.
- Watch next: Audit the claimed savings, failure definitions, staffing attribution, refresh costs, and cross-site recovery under real incidents.
