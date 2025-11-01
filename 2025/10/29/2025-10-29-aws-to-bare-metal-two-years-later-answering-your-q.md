# AWS to bare metal two years later: Answering your questions about leaving AWS

- Score: 700 | [HN](https://news.ycombinator.com/item?id=45745281) | Link: https://oneuptime.com/blog/post/2025-10-29-aws-to-bare-metal-two-years-later/view

TL;DR
Two years post-move, OneUptime says leaving AWS for colocation cut costs ~76% (now ~$1.2M/yr saved), improved latency 19%, and delivered 99.993% availability across multi‑DC racks. Savings Plans couldn’t tame egress, EKS, or NAT fees, and their steady 24/7 load favored owned hardware. Migration overhead and ongoing toil were modest via GitOps and PXE imaging; compliance stayed SOC2/ISO. They still use cloud for Glacier, edge, and bursts. HN debates center on baseload vs elasticity, cloud sprawl/lock‑in, and on‑prem skill scarcity.

Comment pulse
- Bare metal wins for steady baseload → Egress, control-plane, NAT, and reservations keep AWS costly; local NVMe reduces jitter — counterpoint: bursts favor autoscaling.
- Cloud complexity and lock-in bloat teams → certification-led architectures and managed add-ons hide toil in sprawl — counterpoint: on‑prem expertise is scarce; hiring risk rises.
- Reliability feasible off-cloud → multi-DC, Cloudflare DDoS, Anycast BGP; quarterly failovers; avoided a recent AWS outage — counterpoint: single‑rack phases gamble on luck and turnover.

LLM perspective
- View: Open-source parity between their SaaS and self-hosted stack reduces drift; with steady baseload, TCO favors owned hardware.
- Impact: Teams with 24/7 loads, rising egress, and portability needs redirect cloud spend into hardware, AI acceleration, and reliability drills.
- Watch next: Talos migration outcomes, capex forecasting tooling, Anycast failover timings, egress price shifts, and LLM-ops ROI from AI servers.
