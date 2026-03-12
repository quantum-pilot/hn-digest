# BitNet: 100B Param 1-Bit model for local CPUs

- Score: 288 | [HN](https://news.ycombinator.com/item?id=47334694) | Link: https://github.com/microsoft/BitNet

### TL;DR
BitNet is a Microsoft research line using ~1.6‑bit (ternary) weights so that huge models could, in principle, run on commodity CPUs by trading precision for more parameters. The current public models are only 1B–2B parameters and nearly a year old; there is no trained 100B model, just an inference framework that claims it could handle one. HN discussion centers on misleading hype, modest eval performance so far, and genuine interest in the memory‑bandwidth and hardware implications.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- This isn’t new → public BitNet weights are 1B/2B and ~11 months old; title suggests a fresh 100B model that doesn’t exist.  
- BitNet needs 4–5× more parameters than fp16 → but ternary weights turn matmuls into additions, potentially boosting CPU throughput—counterpoint: eval performance still trails better small models like Qwen 3.5 2B.  
- Memory bandwidth is the bottleneck for local 70B+ models → BitNet’s tiny weights could inspire custom low‑bit inference chips using cheap adders and wide vectors.

---

### LLM perspective
- View: BitNet is more a compute/architecture experiment than a practical competitor to today’s best small models… for now.  
- Impact: If proven at scale, it could democratize “100B‑class” local inference on CPUs and reshape inference‑only hardware design.  
- Watch next: A well‑trained ≥30B BitNet model with public evals, plus real‑world CPU benchmarks vs 4‑bit/8‑bit quantized baselines.
