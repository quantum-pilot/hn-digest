# MiMo-v2.5-Pro-UltraSpeed: 1T model with 1000 tokens per second

- Score: 474 | [HN](https://news.ycombinator.com/item?id=48446639) | Link: https://mimo.xiaomi.com/blog/mimo-tilert-1000tps

- TL;DR  
  - Xiaomi’s MiMo‑V2.5‑Pro‑UltraSpeed hits ~1000+ tokens/s on a 1‑trillion‑parameter MoE model using only an 8‑GPU commodity node, via FP4‑only‑on‑experts quantization, DFlash speculative decoding, and TileRT’s persistent‑kernel runtime. It’s ~3× the price of standard MiMo‑V2.5‑Pro but ~10× faster, offered as a limited, application‑gated API trial plus free chat. Xiaomi also open‑sources an FP4‑DFlash checkpoint. HN discussion centers on how ultra‑fast LLMs reshape workflows, worker productivity, and China–US cost competition.

- Comment pulse  
  - Ultra‑fast LLMs change UX → near‑instant responses enable single‑task, interactive workflows, but also let models go “off‑road” faster than humans can intervene.  
  - Productivity for workers is ambiguous → tasks shrink from days to hours, yet review/debug still dominate; some feel more rushed, not freer — counterpoint: better tools enable deeper problem‑solving.  
  - Chinese models seen as “good‑enough and cheap” → combined with rising US prices and closed weights, many foresee migration to Chinese or open‑weight ecosystems.

- LLM perspective  
  - View: Speed is becoming a core capability, enabling multi‑path reasoning, real‑time loops, and new agent designs rather than just nicer UX.  
  - Impact: Beneficial first to power users and infra‑savvy orgs; over time, it commoditizes mid‑tier “AI coding” work.  
  - Watch next: Independent benchmarks of MiMo FP4‑DFlash, price moves by US labs, and whether open UltraSpeed‑like runtimes land in mainstream OSS stacks.
