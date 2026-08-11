# Show HN: Timber – Ollama for classical ML models, 336x faster than Python

- Score: 181 | [HN](https://news.ycombinator.com/item?id=47212576) | Link: https://github.com/kossisoroyce/timber

### TL;DR

Timber compiles trained XGBoost, LightGBM, scikit-learn, CatBoost, and ONNX tree models into native C99, removing Python from inference and optionally serving predictions through a local HTTP API. Its 336-times claim compares warmed, in-process single-row calls for a 50-tree XGBoost classifier on an M2 Pro: roughly 2 microseconds versus Python XGBoost, excluding network serialization. The project targets low-latency, edge, and regulated deployments, with explicit format limitations. Commenters welcomed attention to classical ML but questioned the Ollama analogy, REST overhead, interchangeability, and whether shared libraries fit performance-sensitive callers better.

### Comment pulse

- Classical models still dominate many production decisions and can classify features extracted by LLMs with tunable boundaries.
- The Ollama comparison mainly describes simple loading and a common serving API; commenters thought vLLM was a closer performance analogy.
- Separate-process serving improves portability — counterpoint: serialization and copies may erase gains where callers can load a native library directly.

### LLM perspective

- **View:** The benchmark demonstrates eliminated Python call overhead, not a universal 336-fold application-speed improvement.
- **Impact:** Edge and regulated teams gain small deterministic artifacts without shipping Python and framework dependencies.
- **Watch next:** End-to-end HTTP latency, batch tests, numerical parity, broader ONNX coverage, ARM targets, and independent runtime comparisons.
