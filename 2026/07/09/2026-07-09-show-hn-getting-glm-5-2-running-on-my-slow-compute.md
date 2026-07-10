# Show HN: Getting GLM 5.2 running on my slow computer

- Score: 301 | [HN](https://news.ycombinator.com/item?id=48842459) | Link: https://github.com/JustVugg/colibri

- TL;DR  
  - An HN user demonstrates GLM 5.2 running locally on very modest hardware, trading speed for affordability by leaning on RAM limits and fast NVMe storage. Commenters share parallel experiments: mmap‑based loading in llama.cpp, Apple Silicon and Rust/Metal ports, multi‑token prediction, and aggressive quantization. Discussion revolves around what token/second rates remain useful, whether slow models suit “ticket queue” workflows better than chat, and how this compares to simply using free or cheap cloud-hosted GLM instances.  
  *Content unavailable; summarizing from title/comments.*

- Comment pulse  
  - Running frontier-scale models at home → people explore NVMe streaming, mmap, quantization, and partial residency to squeeze GLM 5.2–class models onto limited RAM.  
  - Usability hinges on throughput → ~1 tok/s seems acceptable for batch jobs; sub‑0.1 tok/s feels unusable—counterpoint: cloud GLM access is free and vastly faster.  
  - Interfaces may need rethinking → some propose ticket or job-queue UIs for slow local models, plus kernel-level optimizations and custom Metal/Rust runtimes on Apple Silicon.

- LLM perspective  
  - View: Local, disk-backed inference is converging across projects; community is collectively probing the limits of storage-bandwidth‑limited LLM serving.  
  - Impact: Enables offline, privacy-preserving use of very large models for patience-tolerant workloads, but won’t replace low-latency cloud chat anytime soon.  
  - Watch next: Shared benchmarks vs cloud APIs, standard APIs for out‑of‑core loaders, and comparisons of Medusa/MTP tricks on storage‑bound setups.
