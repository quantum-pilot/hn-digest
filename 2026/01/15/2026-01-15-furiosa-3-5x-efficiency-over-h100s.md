# Furiosa: 3.5x efficiency over H100s

- Score: 206 | [HN](https://news.ycombinator.com/item?id=46626410) | Link: https://furiosa.ai/blog/introducing-rngd-server-efficient-ai-inference-at-data-center-scale

### TL;DR
FuriosaAI’s NXT RNGD Server is a 3 kW, air‑cooled, turnkey inference box built around up to 8 RNGD ASICs (4 PFLOPS FP8, 384 GB HBM3). It ships with Furiosa’s SDK and a vLLM‑compatible LLM runtime (OpenAI‑API style), targeting drop‑in deployment in existing 8 kW‑per‑rack data centers without liquid cooling. Furiosa claims up to 3.5× better efficiency than H100s and shows production results (e.g., LG’s EXAONE 32B), prompting HN debate over Nvidia’s “power wall,” economics, and ASIC viability.

---

### Comment pulse
- Nvidia’s at a power/cooling wall → specialized inference chips in air‑cooled racks could fix broken AI economics—counterpoint: Nvidia performance and financials still look strong, TPUs exist.
- Most “Nvidia killers” fail → software ecosystem, changing workloads, and memory bandwidth remain dominant bottlenecks; clever general‑purpose designs keep winning except in niche, ultra‑tuned domains.
- Benchmark skepticism → comparing to 3× H100 PCIe feels contrived; demands head‑to‑head vs 8× H100 and proof on larger or evolving models.

---

### LLM perspective
- View: Purpose‑built inference ASICs plus vLLM‑compatible software is a credible wedge into power‑constrained, on‑prem enterprise AI.
- Impact: Helps organizations stuck with air‑cooled racks, tight power budgets, and regulatory pressure to keep models and data local.
- Watch next: Independent MLPerf‑style benchmarks, pricing vs H100/TPU, cloud or managed offerings, and breadth of model/tooling support beyond marquee demos.
