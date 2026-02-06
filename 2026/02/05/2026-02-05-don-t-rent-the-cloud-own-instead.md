# Don't rent the cloud, own instead

- Score: 1062 | [HN](https://news.ycombinator.com/item?id=46896146) | Link: https://blog.comma.ai/datacenter/

### TL;DR
Comma.ai details how they built and run a roughly $5M in‑office data center with ~600 GPUs and 4+ PB of SSD storage, using simple power/cooling, Slurm, PyTorch FSDP, a custom key‑value store, and a lightweight job scheduler instead of public cloud. For their steady, GPU‑heavy ML workloads, they estimate on‑prem is about 5× cheaper and encourages tighter, more efficient engineering. HN discussion focuses on where the cloud/on‑prem break‑even lies, operational risk, and technical caveats like outdoor‑air cooling.

---

### Comment pulse
- Infra choices form a spectrum from public cloud to owned colo; break‑even often around $5–15k/month spend, with bare‑metal 50–90% cheaper.  
- Cloud’s real waste is complex managed services and microservices sprawl driving overuse—counterpoint: many teams lack skills or appetite to own full stack.  
- Comma’s direct outside‑air cooling worries data‑center veterans; humidity, dust and contaminants can drastically shorten hardware life without more sophisticated conditioning.  

---

### LLM perspective
- View: Owning makes sense when GPUs are core IP, utilization is high, and someone senior is accountable for physical reliability.  
- Impact: Expect more mid‑sized ML shops to mix colo plus some cloud, pushing hyperscalers to justify premiums with unique services.  
- Watch next: better ROI tools, open hardware templates, and benchmarks comparing TCO and throughput of clouds versus DIY GPU clusters.
