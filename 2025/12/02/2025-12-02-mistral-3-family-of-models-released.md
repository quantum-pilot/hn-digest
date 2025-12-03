# Mistral 3 family of models released

- Score: 633 | [HN](https://news.ycombinator.com/item?id=46121889) | Link: https://mistral.ai/news/mistral-3

- TL;DR  
Mistral 3 is a fully Apache‑2.0 family: a new sparse MoE flagship (Mistral Large 3, 41B active / 675B total params) plus three “Ministral” edge models (3B, 8B, 14B). All are multilingual, multimodal (text+images), and optimized with NVIDIA/vLLM for efficient inference from data center to Jetson‑class devices. HN discussion praises Mistral’s reliability and formatting vs GPT‑5, notes the Large 3 architecture reuses DeepSeek V2, and debates its competitiveness vs top closed models.

- Comment pulse  
  - Mistral models for structured tasks → very fast, cheap, and precise formatting; outperform some GPT‑5 deployments in reliability despite lower benchmark hype.  
  - Architecture reuse → Large 3 uses DeepSeek V2 code; some see missing attribution as bad form — counterpoint: open licenses explicitly allow such reuse.  
  - Capability gap concern → LMArena shows Large 3 behind leading proprietary models; absence of direct comparisons in the release interpreted as quiet admission.

- LLM perspective  
  - View: Strong open, commercially permissive stack from browser‑scale 3B vision to frontier‑ish MoE is a real alternative for many workloads.  
  - Impact: Startups, EU companies, and on‑device devs gain viable GPT‑4‑class-ish options without vendor lock‑in or restrictive licenses.  
  - Watch next: Reasoning variants’ benchmarks, real‑world latency/throughput on vLLM/TensorRT‑LLM, and whether others adopt DeepSeek‑style MoE as a de facto standard.
