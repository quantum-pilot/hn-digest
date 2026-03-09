# Cloud VM benchmarks 2026

- Score: 325 | [HN](https://news.ycombinator.com/item?id=47293119) | Link: https://devblog.ecuadors.net/cloud-vm-benchmarks-2026-performance-price-1i1m.html

### TL;DR
Independent benchmarks of 44 VM types across AWS, GCP, Azure, OCI, Hetzner, Linode and DigitalOcean show AMD’s EPYC Turin dominating single‑ and multi‑threaded CPU performance, often justifying higher prices. New ARM chips (Google Axion, Azure Cobalt 100, AmpereOne M) now rival or beat x86 on perf/price, while Intel Granite Rapids mainly fixes Emerald Rapids’ inconsistency. Hetzner and Oracle deliver standout value; AWS generally lags on cost. HN discussion centers on self‑hosted vs cloud economics and Oracle’s trade‑offs.

### Comment pulse
- Self-racked servers beat cloud Turin VMs in absolute and per-core speed, but others note colo, hardware, and payback math often erase supposed “months” savings.  
- Hetzner praised for astonishing perf/price and solid dedicated offerings; DigitalOcean criticized for ancient CPUs despite marketing newer chips—counterpoint: they allegedly have some Emerald Rapids nodes.  
- Oracle Cloud’s ARM and Turin VMs look fantastic on paper; commenters still warn about UX nightmares, aggressive sales, and avoiding proprietary services to stay portable.  

### LLM perspective
- Cloud CPU race now: Turin dominant, ARM “house” chips competitive, Intel recovering; choosing newest generation matters more than provider brand.  
- Cost-sensitive teams can mix: OCI or Hetzner for raw compute, big-three only where managed services, regions, or compliance demand it.  
- Watch for Graviton5, broader Turin/Granite deployments, AMD/Nvidia AI alternatives; re-benchmark when providers refresh fleets or tweak spot pricing.
