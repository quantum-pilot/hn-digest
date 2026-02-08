# Don't rent the cloud, own instead

- Score: 1196 | [HN](https://news.ycombinator.com/item?id=46896146) | Link: https://blog.comma.ai/datacenter/

## TL;DR

comma.ai details how it built and runs a ~$5M in‑office data center instead of using public cloud, arguing that owning compute avoids lock‑in, promotes performance‑conscious engineering, and sharply cuts long‑term ML training costs (they estimate more than fivefold savings). Their setup uses custom GPU boxes, multi‑petabyte SSD storage, high‑bandwidth networking, and a thin software layer (Slurm, PyTorch FSDP, custom storage, scheduler, and experiment tooling) run by a small team. HN discussion agrees this pays off at scale but emphasizes hybrid approaches, operational expertise, and colocation or managed bare metal.

## Comment pulse

- Infra spans cloud, managed private, rented bare metal, own/colo → cloud often expensive due to managed services; bare metal/colo shine once spend and skills grow.  
- Hybrid strategies → keep latency‑sensitive GPU/HPC on owned or colocated gear, use cloud for user‑facing and disaster recovery; some say running dual sites is manageable.  
- Outside‑air cooling worries practitioners → humidity and dust shorten hardware life; others cite crypto mines as proof it works — counterpoint: many prefer cloud.

## LLM perspective

- View: For ML-heavy orgs with predictable workloads, investing in dedicated compute can become a strategic moat, not savings alone.  
- Impact: Encourages infra talent, simpler architectures, and OSS‑centric stacks; reduces dependence on hyperscaler pricing and product roadmaps.  
- Watch next: credible TCO benchmarks across models, and expansion of provider‑operated dedicated GPU clusters that abstract facilities while exposing costs.
