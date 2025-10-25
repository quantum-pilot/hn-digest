# Asahi Linux Still Working on Apple M3 Support, M1n1 Bootloader Going Rust

- Score: 258 | [HN](https://news.ycombinator.com/item?id=45694767) | Link: https://www.phoronix.com/news/Asahi-Linux-M3-m1n1-Update

- TL;DR
  - Asahi Linux reports steady Apple Silicon progress: patches upstreaming into 6.17/6.18, M2 Pro/Max/Ultra device trees, and m1n1 bootloader moving to Rust for safety/maintainability. Gaming advances continue; Wine now runs outside muvm as the GPU stack matures. M3 bring-up exists but only “boots to a blinking cursor,” useful for reverse-engineering with fuller support planned. HN debates sticking with capable M1/M2 hardware, bare‑metal Linux needs vs macOS virtualization, and whether Apple’s yearly cadence risks perpetual catch‑up.

- Comment pulse
  - Stick with M1/M2 → still fast, great battery; cheap used options run Asahi well — counterpoint: some need bare‑metal Linux beyond macOS VMs/containers.
  - Yearly Apple chips hinder support → feels Sisyphean; Asahi dev says most SoC interfaces evolve, hardest churn is GPU/NPU and power management.
  - Alternatives and tools → Lenovo P1/X1 praised for upgradability; OrbStack improves Docker-on-Mac; many buy refurbished M2s.

- LLM perspective
  - View: Rust m1n1 hardens the boot chain and clarifies logic; easier audits and contributions.
  - Impact: Mainlining M2 device trees signals longevity for M1/M2 owners; M3 users wait for display, USB, suspend.
  - Watch next: m1n1-rs boot on real hardware; first M3 desktop, Wi‑Fi, GPU bring‑up; kernel 6.18 driver merges.
