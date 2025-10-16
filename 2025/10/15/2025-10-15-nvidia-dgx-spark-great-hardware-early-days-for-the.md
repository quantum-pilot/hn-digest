# Nvidia DGX Spark: great hardware, early days for the ecosystem

- Score: 171 | [HN](https://news.ycombinator.com/item?id=45586776) | Link: https://simonwillison.net/2025/Oct/14/nvidia-dgx-spark/

- TL;DR
  - Nvidia’s $4k DGX Spark is a compact ARM64 desktop with a Blackwell GB10 GPU and 128GB unified memory. Hardware impresses, but CUDA-on-ARM is still rough: PyTorch wheels and CUDA 12/13 mismatches tripped setup until Docker, new Nvidia docs, and emerging support (Ollama, vLLM container, llama.cpp, LM Studio) smoothed things out. Early benchmarks suggest strong prefill but decode lags 4090-class cards; unified memory helps larger models and fine-tuning. HN debates value vs Macs/AMD APUs, longevity risk, and availability.

- Comment pulse
  - Ecosystem clicked post-embargo → official NGC containers make vLLM/Ollama trivial; e.g., one docker run starts vLLM, default Qwen3-0.6B loads fast.
  - Throughput doubts → decode often trails 4090; ~4x lower bandwidth and few MXFP4 models; unified memory is the perk — counterpoint: prefill can be competitive.
  - ARM friction is real → many ML stacks assume x86; Spack can build toolchains and Python wheels across architectures to reduce pain.

- LLM perspective
  - View: Strong dev box for CUDA with big unified RAM; for pure throughput, 4090/5090 or M-series often win.
  - Impact: Best for private fine‑tuning, multi‑modal, or long‑context experiments; less ideal when tokens/sec throughput is the priority.
  - Watch next: ARM64 PyTorch/vLLM maturity, CUDA 13 vs 12 parity, MXFP4 model availability, and long‑term driver/container support commitments.
