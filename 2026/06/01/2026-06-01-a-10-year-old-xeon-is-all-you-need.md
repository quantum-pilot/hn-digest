# A 10 year old Xeon is all you need

- Score: 667 | [HN](https://news.ycombinator.com/item?id=48353348) | Link: https://point.free/blog/gemma-4-on-a-2016-xeon/

## TL;DR
The author shows how to run Google’s new Gemma 4 26B Mixture‑of‑Experts model at “reading speed” on a 2016 Xeon E5‑2620 v4 with DDR3 RAM and no GPU, using a highly tuned fork of llama.cpp (ik_llama.cpp). By aggressively exploiting speculative decoding, CPU‑optimized MoE routing, runtime tensor repacking, mlocked RAM, Flash Attention and MLA on CPU, they push past the memory‑bandwidth bottleneck that normally kills performance. The broader point: open‑weight models are usable on cheap recycled hardware if you control the inference stack instead of relying on black‑box tools.

---

## Comment pulse
- Old Xeons are viable LLM hosts → multiple readers report similar setups (2012–2014 Xeons, 128–192GB RAM, modest GPUs) achieving usable t/s locally—counterpoint: some confusion about DDR3 support and SMT benefits.
- Local “good enough” AI may undercut cloud APIs → devs cancel Copilot, move to local coding models, planning to hit APIs only when stuck; others expect open‑model hosting at commodity cloud prices to erode hyperscaler moats.
- Economics and noise debated → one warns old servers are power‑hungry versus $0.1–0.3/M token APIs; others correct: ~85W under load, quiet with larger cases and slower fans.

---

## LLM perspective
- View: This work proves that software‑level memory and cache optimization can substitute for expensive GPUs for many personal and homelab workloads.
- Impact: Homelabbers, small teams, and privacy‑sensitive users gain credible local alternatives to proprietary APIs, especially for coding and automation.
- Watch next: Better-documented CPU kernels and autotuning in mainstream runtimes; standardized “expert presets” for old hardware; more CPU‑friendly open MoE models.
