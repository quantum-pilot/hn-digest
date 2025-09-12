# Why is Japan still investing in custom floating point accelerators?

- Score: 236 | [HN](https://news.ycombinator.com/item?id=45141907) | Link: https://www.nextplatform.com/2025/09/04/why-is-japan-still-investing-in-custom-floating-point-accelerators/

- TL;DR
  - Japan is backing Pezy’s SC4s math accelerators as a sovereign, energy‑efficient alternative to GPUs for FP64‑heavy HPC and some AI. SC4s packs 2,048 SPMD cores, 96 GB HBM3, and RISC‑V control, delivering FP64 flops/watt near Nvidia H200 and strong genomics results, while running PyTorch. GPUs increasingly favor low‑precision AI, shrinking FP64 options; Pezy hedges supply risks ahead of FugakuNext. HN notes national‑security motives, immersion‑cooled cluster‑only sales, and questions around TSMC dependence and FP64 power on Nvidia parts.

- Comment pulse
  - Strategic autonomy → Japan wants domestic HPC capacity for defense/nuclear simulation; local accelerators hedge export shocks — counterpoint: Pezy still fabs at TSMC, not in‑country.
  - GPU drift to AI → Nvidia deprioritizes FP64; Pezy targets HPC gaps. Question raised: do FP64‑limited GPUs actually draw nameplate TDP under FP64 workloads?
  - System design and sales → Immersion‑cooled, cluster‑scale offerings; limited retail access. Software moat: Nvidia’s ecosystem remains the main adoption barrier.

- LLM perspective
  - View: Pezy is a focused FP64/HPC play and geopolitical hedge; viability depends on mature PyTorch ops, compilers, and cluster software.
  - Impact: Success could pressure Nvidia to sustain FP64 SKUs and bolster Japan’s leverage; near‑term winners: genomics, CFD, climate, nuclear simulations.
  - Watch next: Independent benchmarks beyond GATK; PyTorch op coverage; fab plans (Rapidus vs TSMC); SC5s chiplets with FP8; large‑scale immersion deployments.
