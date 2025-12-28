# OrangePi 6 Plus Review

- Score: 121 | [HN](https://news.ycombinator.com/item?id=46401499) | Link: https://boilingsteam.com/orange-pi-6-plus-review/

### TL;DR
OrangePi 6 Plus is a high-end ARM64 SBC: 12-core Armv9 (A720/A520), Immortalis-G720 GPU, 16–64GB LPDDR5, PCIe 4.0 x8 with dual NVMe, dual 5GbE, 8K output. It feels like an x86 desktop, benchmarks near an i5-10500 (single core) and Ryzen 7 4800H (multi-core), runs 1080p gaming and OBS after some manual builds, and can do small LLMs on CPU. But it’s stuck on Debian Bookworm + 6.6 kernel, with fragile non-mainline drivers, awkward NPU tooling, and a high 15W idle. HN praises the hardware but questions long-term software support versus Pi-class boards or cheap x86 mini-PCs.

---

### Comment pulse
- OrangePi/Radxa boards → fast but flaky: old kernels, DIY images, PRC-hosted or ad‑hoc repos; Raspberry Pis feel boring but reliable.  
- Why not an N150/N300 mini‑PC → similar price, lower idle power, better OS support—counterpoint: this SoC’s 12 cores significantly outgun low-end Intel for multicore work.  
- Many want mainline-first SBCs → no upstream Linux, no sale; NPUs are often decorative without drivers, and SBC “horsepower race” ignores small, cheap IoT/edge use cases.

---

### LLM perspective
- View: As a dev box, it’s great; as an appliance, non-mainline Linux and vendor SDKs make it fragile.  
- Impact: Best suited to hobbyists and ARM developers comfortable compiling kernels, GPUs, and ML stacks themselves.  
- Watch next: Mainlining of CIX SoC, stable Panfrost + newer kernels, and any open NPU backends for llama.cpp/ggml.
