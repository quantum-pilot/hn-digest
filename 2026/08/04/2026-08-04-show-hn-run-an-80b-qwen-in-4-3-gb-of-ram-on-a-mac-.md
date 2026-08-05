# Show HN: Run an 80B Qwen in 4.3 GB of RAM on a Mac, and a 35B on an iPhone

- Score: 304 | [HN](https://news.ycombinator.com/item?id=49158333) | Link: https://github.com/leonickson1/Swiftlet

### TL;DR

Swiftlet is an Apache-licensed Swift and Metal runtime that runs sparse Qwen MoE models on Apple devices by retaining only dense components in memory and streaming selected experts from SSD. It reports Qwen3.6-35B-A3B in 2.6GB RAM at 7–11 tokens/s on an M5 Mac and about 1 token/s on an iPhone 17; an 80B model uses 4.3GB at 4.5–5 tokens/s. Fixed-stride storage, bounded expert caching, and mostly linear attention enable the footprint. HN applauded accessible experimentation but debated SSD wear, centralized economics, and practical quality.

### Comment pulse

- Consumer-device feasibility invites experimentation → motivated amateurs can improve software once a previously inaccessible model class becomes runnable.
- SSD streaming is genuine progress → counterpoint: critics doubt this path scales economically or technically to trillion-parameter models.
- Centralized inference remains efficient for parallel demand → local execution still matters for privacy, offline access, customization, and unusual workloads.

### LLM perspective

- **View:** Sparse activation turns storage bandwidth and dispatch overhead into optimization targets without pretending every parameter is active.
- **Impact:** Apple developers can embed larger local models in applications that lack enough RAM for conventional loading.
- **Watch next:** Kernel speedups, SSD endurance measurements, larger-cache scaling, iPhone thermals, and independent output-quality tests.
