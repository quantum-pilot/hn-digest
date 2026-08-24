# Don't rent the cloud, own instead

- Score: 1196 | [HN](https://news.ycombinator.com/item?id=46896146) | Link: https://blog.comma.ai/datacenter/

### TL;DR

Comma.ai says its $5 million office data center would have cost more than $25 million in cloud services. Its predictable ML workload uses 600 GPUs across 75 TinyBox Pros, about 4 PB of SSD storage, simple networking, outside-air cooling, Slurm, PyTorch, and lightweight custom storage and scheduling tools, maintained by a few people. Much data and several service masters deliberately lack redundancy. Commenters treated ownership as one option on a spectrum spanning cloud, managed private cloud, rented bare metal, colocation, and hybrid deployments, with scale and staffing determining the winner.

### Comment pulse

- Economics favor steady utilization → owned hardware can reward optimization and avoid metered premiums when compute and storage remain consistently busy.
- Infrastructure is a spectrum → rented bare metal, managed private cloud, colocation, and cloud bursting can reduce capital, staffing, or reliability tradeoffs.
- Operational simplicity has limits → outside-air cooling worked for comma — counterpoint: contaminants, humidity, compliance, failures, and multiple sites require specialized judgment.

### LLM perspective

- View: This case supports ownership for predictable, infrastructure-core ML workloads, not a universal rejection of public cloud.
- Impact: Teams can cut recurring spend and control hardware, while assuming procurement, capacity, power, cooling, repair, and availability risk.
- Watch next: Utilization, hardware failures, power generation, cooling durability, staffing cost, refresh cycles, downtime, and continued hybrid-cloud use.
