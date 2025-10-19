# AMD's Chiplet APU: An Overview of Strix Halo

- Score: 165 | [HN](https://news.ycombinator.com/item?id=45624888) | Link: https://chipsandcheese.com/p/amds-chiplet-apu-an-overview-of-strix

- TL;DR
    - AMD’s Strix Halo is a 55–120W chiplet APU: up to 16 Zen 5 cores (full 512-bit FPUs) plus a 40‑CU RDNA 3.5 iGPU, fed by 256‑bit LPDDR5X‑8000 (256 GB/s). CPU performance approaches desktop Zen 5; the iGPU rivals an RTX 5070 Mobile in some workloads/settings, helped by 32MB Infinity Cache, though external GDDR still wins at higher bandwidth. ROCm 7.0.2 only just arrived, so ML results lag. HN discusses scarce EU availability/pricing, ROCm maturity vs Nvidia, and this emerging “local‑AI APU” niche vs dGPUs and DGX Spark.

- Comment pulse
    - EU availability/pricing pain → few Halo laptops/mini‑PCs; 128GB configs scarce, warranties spotty—counterpoint: HP ZBook Ultra offers 128GB and fair EU pricing.
    - ROCm progress → usable on Linux, but hiccups remain; for AI today, Nvidia (or Apple) still safer; some recommend cheap dual‑RTX 3090 desktops for perf/$.
    - Positioning vs dGPUs/DGX Spark → integrated wins on power/integration and memory capacity; dGPUs win on bandwidth; future “Medusa Halo” may add 384‑bit LPDDR6.

- LLM perspective
    - View: Integrated 128GB shared memory plus decent GPU makes local inference attractive for mid‑size models without VRAM constraints.
    - Impact: Laptop dGPU attach rates may fall; mini‑PC and workstation buyers gain compact, lower‑power AI boxes.
    - Watch next: Stable ROCm 7.x, ML benchmarks vs 4070/5070M, OEMs shipping 128–192GB configs, and LPDDR6‑384‑bit “Medusa Halo” timelines.
