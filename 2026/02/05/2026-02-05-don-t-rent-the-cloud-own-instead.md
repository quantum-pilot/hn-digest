# Don't rent the cloud, own instead

- Score: 1193 | [HN](https://news.ycombinator.com/item?id=46896146) | Link: https://blog.comma.ai/datacenter/

### TL;DR
Comma.ai describes how it runs all ML training and data in a self-built, in-office $5M data center instead of public cloud. Motivations: avoid lock‑in, keep architectural control, force efficiency (optimize code instead of buying more compute), and slash costs—they estimate cloud would have cost $25M+. The setup: 600 GPUs in in‑house boxes, ~4PB SSD storage, Slurm + PyTorch FSDP, a custom key‑value storage layer, lightweight task scheduler, and monorepo-based workflows. HN extends this into a broader debate about cost, scale, staffing, and operational risk.

### Comment pulse
- Cloud vs own spectrum → options from hyperscale, managed private, rented bare metal, to owned/colo; savings often 50–90% vs AWS when workloads are steady.  
- Scale and people → If infra spend <1 FTE/year, cloud is fine; at multi‑FTE bills, staff+colo can win — counterpoint: hardware/ops overhead is real.  
- Reliability and cooling → Owning a DC means handling redundancy, humidity, dust; some urge indirect-air systems — counterpoint: comma says filtered air <45% RH works.  

### LLM perspective
- View: For predictable heavy GPU workloads, owning or colocating clusters increasingly beats hyperscale cloud on both cost and architectural flexibility.  
- Impact: Expect hybrids: cloud for bursty user apps, dedicated GPU fleets for training, and research HPC time for cash‑constrained startups.  
- Watch next: Turnkey managed-colo GPU offerings, open-source infra stacks like minikeyvalue/miniray, and clearer benchmarks comparing 3–5‑year TCO versus AWS/Azure.
