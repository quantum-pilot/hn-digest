# AMD GPUs Go Brrr

- Score: 246 | [HN](https://news.ycombinator.com/item?id=45934416) | Link: https://hazyresearch.stanford.edu/blog/2025-11-09-amd-brr

TL;DR
HipKittens is a low-level toolkit that unlocks AMD CDNA GPUs by embracing their quirks: explicit register-tiling with pinned AGPR/VGPR usage, AMD-specific memory layouts/phases, and HBM-address swizzling; two intra-CU schedules (8‑wave ping‑pong, 4‑wave interleave) instead of wave specialization; and chiplet‑aware grid ordering to reuse L2/LLC. Results: MI355X BF16 GEMM hits ~1.6 PFLOPs, attention backward is 1.8–2.3× over AMD baselines, and bandwidth/TFLOPs rise with cache-smart block ordering. HN debates AMD’s software gaps, dev experience vs NVIDIA, and chiplet-driven scalability.

Comment pulse
- AMD must fix software stack → hardware lags without compiler/driver maturity; NVIDIA remains smoother for devs — counterpoint: Some report painless ROCm inference setups.
- Academia fills gaps productively → HipKittens/ThunderKittens show vendor-independent kernel progress; AMD is engaging (e.g., with tinycorp).
- Chiplets may scale better → more XCDs favor cache-aware scheduling; solving locality now could future-proof performance.

LLM perspective
- View: Adopt AMD-native pipelines; don’t force NVIDIA paradigms like wave specialization without register reallocation.
- Impact: Kernel authors, ROCm/HIPCC teams, and frameworks need register pinning, MFMA-aware layouts, and chiplet-aware launchers.
- Watch next: HIPCC AGPR input fixes, formal docs on memory phases, upstream PyTorch/Triton support for XCD-savvy scheduling.
