# Big GPUs don't need big PCs

- Score: 119 | [HN](https://news.ycombinator.com/item?id=46338016) | Link: https://www.jeffgeerling.com/blog/2025/big-gpus-dont-need-big-pcs

## TL;DR
Jeff Geerling shows that a Raspberry Pi 5 with only a single PCIe Gen3 x1 lane can drive high‑end GPUs surprisingly well for GPU‑bound work. For video transcoding benchmarks that are I/O‑heavy, a modern Intel desktop crushes the Pi, but for real Jellyfin usage the Pi handles multiple 4K/1080p streams fine. In GPU rendering and LLM inference, a Pi + big Nvidia GPU often delivers within 2–5% of PC performance, while using much less power and far cheaper host hardware.

---

## Comment pulse
- Multi‑GPU LLMs often split models by layers → serialization and PCIe latency limit speedups; better tensor‑parallel backends and GPU‑P2P interconnects are key — counterpoint: parallel “agent” workflows can still saturate multiple GPUs.
- Many readers want the *cheapest* box that can “just feed the GPU” → Pi‑style hosts are attractive, but RAM capacity and PCIe lane count still matter for serious local AI.
- Discussion veers to future architectures → GPUs as near‑network devices with their own storage/CPUs and high‑bandwidth links, potentially even flash‑centric AI accelerators.

---

## LLM perspective
- View: For inference, host compute is often overbuilt; a tiny, efficient controller plus big GPU is enough.
- Impact: Hobbyists, small labs, and homelabbers can cut AI hardware cost and idle power while keeping strong performance.
- Watch next: Better Arm drivers, CUDA/Vulkan parity benchmarks, and commodity PCIe switches or network‑attached GPU boxes targeting Pi‑class hosts.
