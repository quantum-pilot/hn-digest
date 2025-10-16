# Apple M5 chip

- Score: 932 | [HN](https://news.ycombinator.com/item?id=45591799) | Link: https://www.apple.com/newsroom/2025/10/apple-unleashes-m5-the-next-big-leap-in-ai-performance-for-apple-silicon/

- TL;DR
  - Apple’s M5 brings a third‑gen 3nm SoC with per‑core GPU Neural Accelerators (Apple claims 4× AI GPU vs M4), 10‑core CPU (~15% multithread), faster 16‑core Neural Engine, and 153 GB/s unified memory, powering new 14‑inch MacBook Pro, iPad Pro, and Vision Pro. HN cheers on-device AI and graphics gains but questions cherry‑picked marketing (e.g., “86× vs Intel”) and notes small early CPU uplifts. Threads debate Tahoe sluggishness, Linux/ARM openness and gaming limits, and Apple’s vague Neural Engine details and memory constraints.

- Comment pulse
  - Marketing is cherry-picked → Apple touts “86× vs Intel”; early Geekbench shows ~8% single-core gain, 9‑core multi-core sample.
  - Software slowdown concerns → Users report Tahoe makes M1/M2 sluggish; glitches like cursor stutter; suspected intentional slowdowns — counterpoint: UI changes and bugs, not malice.
  - Openness/Linux debate → Some refuse Macs without native Linux; Asahi supports M1/M2; others suggest virtualization/containers; ARM gaming/tooling remains limiting.

- LLM perspective
  - View: Per-core GPU accelerators shift ML toward GPU-centric compute; ANE becomes specialized; developers should target Metal Tensor APIs and Core ML.
  - Impact: On-device diffusion and small-to-mid LLMs benefit; memory bandwidth helps context-heavy VLMs; 32GB cap still constrains larger models.
  - Watch next: Independent MLX/Metal benchmarks vs M4 and RTX; details on ANE/GPU tensor mapping; Asahi support and developer docs for GPU Accelerators.
