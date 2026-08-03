# Run Kimi K3 using 29 GB of RAM at 0.50 tok/s

- Score: 132 | [HN](https://news.ycombinator.com/item?id=49123386) | Link: https://github.com/sqliteai/waste

### TL;DR

WASTE is a dependency-free C engine that runs the full 2.78-trillion-parameter Kimi K3 by keeping its shared trunk in RAM and streaming selected mixture-of-experts weights from NVMe. On a 64 GB M5 Pro MacBook, a 982 GB converted model decodes at 0.45–0.62 tokens/second; 29.06 GB is only the opening floor, while 64 GB is the practical minimum. Commenters found the experiment novel but questioned precision claims, LLM-authored documentation, and efficiency, estimating poor electricity economics versus GPU clusters.

### Comment pulse

- Documentation undermines confidence → readers found LLM-generated prose inscrutable and perceived contradictions around native precision, quantization, and the 29 GB claim.
- Human orchestration remains the defense → the author says experience plus agents produces better code faster — counterpoint: critics doubt meaningful review.
- Energy economics look unfavorable → commenters estimated about $5 per million tokens and 1,000–2,000 times GPU-cluster power use.

### LLM perspective

- View: Cache sizing must respect physical residency; higher hit rates caused page faults and an eightfold throughput collapse.
- Impact: Experimenters can inspect complete-model behavior without enough RAM to hold all published weights.
- Watch next: Test Metal and CUDA backends, measure energy per token, and validate performance on additional hardware.
