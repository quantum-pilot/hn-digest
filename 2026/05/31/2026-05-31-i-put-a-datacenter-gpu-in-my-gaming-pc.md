# I put a datacenter GPU in my gaming PC

- Score: 271 | [HN](https://news.ycombinator.com/item?id=48345694) | Link: https://blog.tymscar.com/posts/v100localllm/

### TL;DR
A home gamer added a used Tesla V100 SXM2 datacenter GPU to a desktop via an unofficial SXM2‑to‑PCIe adapter, creating a dual‑GPU, 32 GB VRAM rig for local LLMs at roughly 10% the cost of a new 32 GB gaming card. After taming an 82 dB server fan with a simple PWM wiring hack, they used NixOS, legacy NVIDIA drivers, and a custom llama.cpp build to run Qwen3.6‑27B‑MTP (with vision) at interactive speeds, rivaling mid‑tier cloud models. Hacker News adds real‑world notes on airflow, aging features, and prefill bottlenecks.

---

### Comment pulse
- Used datacenter GPUs (V100, MI50/MI100) → great $/VRAM, but lack modern formats like bf16 and demand elaborate cooling, fan shrouds, or water loops.  
- Prefill dominates large‑context workflows → 100k tokens can mean multi‑minute waits; discussions revolve around prompt caching and how well frameworks reuse cached prefixes.  
- V100s shine beyond LLMs → strong FP64 makes them attractive for scientific compute; many run them in noisy basement servers rather than desktops.

---

### LLM perspective
- View: Cheap ex‑datacenter GPUs plus strong open models are pushing serious local AI from “hobby” into everyday tooling.  
- Impact: Independent devs and labs can prototype powerful agents privately instead of paying recurring API costs.  
- Watch next: More robust multi‑GPU support, mature MTP implementations, and better software support for legacy accelerators in mainstream inference stacks.
