# Use One Big Server (2022)

- Score: 350 | [HN](https://news.ycombinator.com/item?id=45085029) | Link: https://specbranch.com/posts/one-big-server/

- TL;DR
  - Thesis: for most web apps, one modern “big” server plus a differently specced backup beats cloud-native sprawl on cost, latency, and complexity. Today’s boxes (100+ cores, ~TB RAM, NVMe) handle 10k+ QPS; clouds add a 5–30x premium (serverless worst). Prefer vertical scaling; use multi-DC redundancy to avoid correlated failures; keep clouds for bursty workloads, CDNs, and backups. HN largely agrees on cloud tax and bare‑metal predictability; dissenters cite IaC/PaaS speed and durable services as worth it for larger, well-funded efforts.

- Comment pulse
  - Cloud tax narrows design → bare metal gives 10–100x resources, lower latency; simpler systems suffice — counterpoint: IaC/PaaS often trivialize setup; cost seldom blocks winners.
  - Two-server pattern → one live, one backup in different DCs/hardware reduces correlated failures; HN follows this with high uptime.
  - Avoid premature cloud-native → teams burn months on k8s; PaaS or a VPS works until the bill hurts; hybrid colo+cloud yields best cost/perf at scale.

- LLM perspective
  - View: Start vertical: benchmark one hefty box; add a differently specced hot standby; treat microservices as optimization, not default.
  - Impact: fewer moving parts, lower latency, cost savings; but requires ops fluency and discipline around backups, monitoring, and failover testing.
  - Watch next: ARM price/perf vs x86, EPYC core trends, NVMe benchmarks; vertical-scaling case studies; serverless pricing changes and egress fees.
