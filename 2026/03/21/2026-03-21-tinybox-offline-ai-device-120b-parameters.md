# Tinybox- offline AI device 120B parameters

- Score: 247 | [HN](https://news.ycombinator.com/item?id=47470773) | Link: https://tinygrad.org/#tinybox

## TL;DR
tinygrad, George Hotz’s minimalist deep learning framework, now ships tinybox: prebuilt multi-GPU machines aimed at cheap petaflop-scale, fully offline LLM training and inference. Red v2 (4× 9070XT, 64GB VRAM) and Green v2 (4× RTX 6000 Blackwell, 384GB VRAM) target local 70–120B-parameter models via aggressive quantization and RAM offload, with a 1-exaflop “exabox” planned. HN likes the human-written, opinionated site and local-control ethos but questions specs, 120B claims on red v2, and exabox’s competitiveness with Nvidia clusters—and watches tinygrad’s 2×-PyTorch performance promise.

## Comment pulse
- Local-control appeal → Human-written page and “AI for everyone” pitch resonate; buyers accept quirks like wiring and wire-transfer-only purchasing.  
- 120B on red v2 disputed → 64GB VRAM implies quantization and RAM offload; — counterpoint: some report 120B by splitting weights across RAM and GPU.  
- Exabox and tinygrad roadmap → Exaflop box seen as niche versus Nvidia DGX/Vera Rubin; others curious whether tinygrad can truly outpace PyTorch on real workloads.  

## LLM perspective
- View: This targets researchers and serious hobbyists who want turnkey local LLM rigs without wrestling with PCIe layouts and firmware.  
- Impact: If pricing holds, could normalize petaflop homelabs and reduce dependence on cloud GPU rentals for mid-sized teams.  
- Watch next: Independent benchmarks for 120B-class models, thermal/noise reports in homes, and whether exabox’s fabric competes with NVLink or Infiniband.
