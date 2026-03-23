# Flash-MoE: Running a 397B Parameter Model on a Laptop

- Score: 290 | [HN](https://news.ycombinator.com/item?id=47476422) | Link: https://github.com/danveloper/flash-moe

## TL;DR

Flash‑MoE is a pure C/Metal inference engine that streams a 397B‑parameter Qwen3.5 MoE model from SSD on an M3‑Max MacBook, reaching ~4.4 tok/s with 4‑bit experts. It uses on‑demand SSD expert loading, hand‑tuned FMA dequant kernels, Metal shaders, BLAS for linear attention, and macOS’s page cache instead of custom caching, with a GPU→SSD→GPU serial pipeline dictated by unified memory. HN discussion praises the engineering but stresses that aggressive 2‑bit quantization and expert reduction make the “397B” setup more proof‑of‑concept than practically useful.

---

## Comment pulse

- Alternative path → 2.5 bpw Qwen 397B quants run on 128 GB Macs at ~20 tok/s with strong eval scores—counterpoint: still big hardware, not “small laptop.”

- Quality concern → 2‑bit quant + cutting experts from 10→4 “lobotomizes” the model; JSON/tool calls break, outputs wander, so it’s more demo than tool.

- Systems angle → Questions about mmap, huge pages, and prefetching; several note a well‑tuned 30B @4‑bit often beats a massive model at 2‑bit.

---

## LLM perspective

- View: Real value is in the meticulous systems work and experiment log, not the “397B on a laptop” headline.

- Impact: Sets a reference design for MoE‑on‑SSD pipelines and highlights how unified memory constraints shape optimal scheduling.

- Watch next: Independent benchmarks of 4‑bit Flash‑MoE on real workflows versus smaller dense models, plus ports to non‑Apple GPUs/OSes.
