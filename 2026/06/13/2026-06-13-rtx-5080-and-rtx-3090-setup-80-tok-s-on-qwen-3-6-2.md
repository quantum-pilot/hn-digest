# RTX 5080 and RTX 3090 Setup: 80 Tok/s on Qwen 3.6 27B Q8

- Score: 287 | [HN](https://news.ycombinator.com/item?id=48515454) | Link: https://imil.net/blog/posts/2026/rtx-5080-+-rtx-3090-setup-80+-tok-s-on-qwen-3.6-27b-q8/

## TL;DR
Home enthusiast pairs an RTX 5080 (16 GB) with a refurbished RTX 3090 (24 GB) on an Asus X570-Pro, uses UEFI-only boot, 4G decoding, ReBAR, custom CUDA builds, and llama.cpp multi‑GPU tensor splitting to run Qwen 3.6 27B Q8 with a 230k context at 80–90 tokens/s locally. HN commenters report similar setups, debate optimal sampling/MTP settings and quant choices, compare against cloud/frontier models, and weigh electricity, hardware diversity, and maintainability of AI‑generated code.

---

## Comment pulse
- Local mid‑size Qwen models rival cloud assistants for many day‑to‑day tasks → simpler failures, less “clever” but more maintainable code, big-context workflows feel transformative.  
- Author’s hyperparameters and quant/model pick seen as suboptimal → others recommend different temps, MTP/ngram settings, and a better 27B quant for higher quality.  
- Performance vs cost tension → some report much lower tps on other GPUs/ASICs and note electricity makes heavy local inference non‑competitive with cloud — counterpoint: ownership, privacy, and latency still justify it.

---

## LLM perspective
- View: Commodity multi‑GPU rigs plus aggressive quantization/speculative decoding make serious local assistants practical for power users, not just labs.  
- Impact: Independent devs, tinkerers, and small orgs gain private, always‑on “personal models” tightly integrated with custom tools and data.  
- Watch next: Better multi‑GPU schedulers, standardized MTP/ngram presets, and clear perf‑per‑watt benchmarks across Nvidia, Apple Silicon, and emerging accelerators.
