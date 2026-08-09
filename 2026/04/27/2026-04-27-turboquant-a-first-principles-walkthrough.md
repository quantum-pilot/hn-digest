# TurboQuant: A first-principles walkthrough

- Score: 282 | [HN](https://news.ycombinator.com/item?id=47916890) | Link: https://arkaung.github.io/interactive-turboquant/

### TL;DR

TurboQuant compresses vectors to 2–4 bits per coordinate by randomly rotating them, spreading outliers into a near-Gaussian distribution, then applying a Lloyd–Max codebook without per-block scales. Its MSE variant matches Shannon’s \(4^{-b}\) distortion rate within a constant factor; its product variant uses one QJL residual bit to remove inner-product bias. The paper reports full-quality 4× KV-cache compression and faster indexing. Hacker News questioned precedence and reproducibility: DRIVE and EDEN introduced the construction earlier, optimized scaling reportedly beats TurboQuant, RaBitQ authors dispute its comparisons, and one llama.cpp implementation runs 5–10× slower.

### Comment pulse

- DRIVE and EDEN authors say TurboQuant fixes their scale suboptimally and needs an extra residual bit; their note reports EDEN winning every setup.
- RaBitQ researchers allege runtime and recall numbers do not reproduce — counterpoint: these remain public allegations under review.
- KV-cache compression primarily raises concurrent inference capacity, not model size; local benefits depend on model quality and implementation speed.

### LLM perspective

- **View:** The rotation-and-codebook insight is valuable, but novelty and implementation claims must be separated.
- **Impact:** Efficient kernels could extend contexts and batch sizes while reducing memory requirements.
- **Watch next:** Independent reproductions, corrected baselines, EDEN comparisons, kernel optimization, end-to-end latency, energy, and quality regressions.
