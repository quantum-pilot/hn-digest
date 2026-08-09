# Show HN: How I Topped the HuggingFace Open LLM Leaderboard on Two Gaming GPUs

- Score: 260 | [HN](https://news.ycombinator.com/item?id=47322887) | Link: https://dnhkng.github.io/posts/rys/

### TL;DR

Using two RTX 4090s, the author swept 3,241 ways to repeat contiguous blocks in Qwen2-72B and found that rerunning seven middle layers improved math and emotional-reasoning probes without changing weights. Applied to a model, the 78B execution path ranked first on Hugging Face’s then-current leaderboard: five of six benchmarks improved, including MuSR by 17.72 percent, while IFEval fell 2.05 percent. He hypothesizes that middle layers form reusable multi-step circuits because repeating single layers fails. Readers find the heatmaps compelling, but code is forthcoming and the anatomical interpretation remains unreviewed.

### Comment pulse

- Out-of-sample validation strengthens the result → leaderboard tasks were not used during the math-and-emotion block search.
- Architecture surgery is not free → shared layer pointers save weight memory, but repeated depth increases inference compute and KV-cache demand.
- Functional “organs” remain a hypothesis — counterpoint: coherent block effects suggest structure, but benchmark gains alone do not identify mechanisms.

### LLM perspective

- **View:** The optimization looks reproducible; the neuroscience analogy needs ablations, independent replication, and mechanistic evidence.
- **Impact:** Local-model builders may trade latency for capability without training or storing additional weights.
- **Watch next:** Released code, current-model scans, probe-overfitting controls, statistical uncertainty, and junction-only fine-tuning.
