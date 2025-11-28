# TPUs vs. GPUs and why Google is positioned to win AI race in the long term

- Score: 236 | [HN](https://news.ycombinator.com/item?id=46069048) | Link: https://www.uncoveralpha.com/p/the-chip-made-for-the-ai-inference

- TL;DR  
Google’s TPUs are custom AI accelerators built around systolic arrays and a tightly integrated software stack, delivering higher performance-per-watt and lower cost-per-query than Nvidia GPUs for well-matched workloads, especially large-scale inference. TPUv7 reportedly rivals Blackwell while being deeply optimized for Google services and GCP, letting Google escape Nvidia’s gross margins and potentially restore 50%+ cloud margins. Adoption, however, is constrained by CUDA/PyTorch inertia, single-cloud lock-in fears, and the difficulty of effectively exploiting highly specialized hardware.

- Comment pulse  
  - Claim → Google’s strength is TPU mega-clusters plus vertical stack, enabling cheap full-stack AI—counterpoint: Nvidia’s NVLink wins for MoE all‑to‑all traffic and MLPerf.  
  - Claim → Silicon isn’t decisive; data, research tricks, evals, and tooling matter more, and TPU-specific optimization is hard compared with today’s ubiquitous CUDA ecosystem.  
  - Claim → CUDA’s value is highest in training; inference favors simpler ASICs, pressuring Nvidia’s margins as hyperscalers copy TPUs and Meta explores buying Google chips.

- LLM perspective  
  - View → TPU economics matter for hyperscalers; most smaller firms will consume AI via managed APIs, abstracted from hardware choice.  
  - Impact → If TPU inference becomes default inside Google products, profit shifts from ads+Nvidia spend toward higher-margin AI subscriptions.  
  - Watch next → Whether Google offers TPUs via neocloud partners or on-prem, testing enterprise worries about lock‑in and long-term support.
