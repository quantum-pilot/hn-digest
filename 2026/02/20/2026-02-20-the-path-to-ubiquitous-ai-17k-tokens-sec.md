# The path to ubiquitous AI (17k tokens/sec)

- Score: 651 | [HN](https://news.ycombinator.com/item?id=47086181) | Link: https://taalas.com/the-path-to-ubiquitous-ai/

### TL;DR

Taalas hard‑wires individual language models into custom chips, merging storage and compute on a huge 6nm die to crush latency and cost. Their first product, a heavily quantized Llama 3.1‑8B, reportedly reaches ~17k tokens/sec per user at ~10x speed, 20x cheaper build, and 10x lower energy versus GPU baselines, exposed via an API and instant‑feeling chat demo. HN sees big potential for real‑time agents, robotics, and bulk processing, while debating yield, model lock‑in, and the promised two‑month design‑to‑silicon cycle.

---

### Comment pulse

- Custom, per‑model chip looks technically sound and fast (≈15–17k tok/s, 6nm, 880mm², 3‑bit quant), ideal for ultra‑low‑latency, short‑context inference; 2‑month turnaround seems optimistic.  

- Market view: many workloads don’t need frontier IQ; cheap, fast 8B‑class models fit bulk data, web, robotics—counterpoint: rivals like Cerebras may already cover this niche.  

- Users report near‑instant demo responses enabling new coding/agent workflows, but note glitches and that quality is bounded by a two‑year‑old, heavily‑quantized 8B model.  

---

### LLM perspective

- View: This is effectively “AI ASICs as a service,” trading model flexibility for latency and cost—attractive wherever SLAs beat IQ.  

- Impact: If economics hold, GPU clouds may offload predictable workloads to such chips, reserving frontier GPUs for training and experimentation.  

- Watch next: independent benchmarks, transparent per‑token pricing, and evidence they can tape‑out new model silicon within months as architectures evolve.
