# Show HN: Timber – Ollama for classical ML models, 336x faster than Python

- Score: 181 | [HN](https://news.ycombinator.com/item?id=47212576) | Link: https://github.com/kossisoroyce/timber

## TL;DR
Timber is an ahead-of-time compiler for classical tree-based ML models (XGBoost, LightGBM, scikit-learn, CatBoost, ONNX TreeEnsemble). It converts trained models into tiny, dependency-free C99 binaries and exposes them via an Ollama-style HTTP API (`timber load` / `timber serve`). Benchmarks claim ~2 µs in-process latency and ~336× speedup over Python XGBoost for single-sample inference, targeting fraud/risk, edge/embedded, and regulated environments where predictable, auditable, non-Python inference artifacts matter.

---

## Comment pulse
- Classical ML still dominates real-world systems → People like seeing infra that treats tree models as first-class, including LLM+features → small classifier stacks.
- “Ollama” analogy disputed → Some see it closer to vLLM; others say the similarity is just the simple `serve` REST API — counterpoint: classical models aren’t swappable like LLMs.
- Architecture questions → Some want shared libraries for zero-copy integration; others accept HTTP as “fast enough” for simplicity, language-agnostic use, and no Python dependency.

---

## LLM perspective
- View: Strong niche: high-throughput, low-latency tree models where Python/ONNX overhead and operational determinism are pain points.
- Impact: MLOps/platform and fintech/IoT teams can standardize on compiled classical models instead of ad‑hoc Python services.
- Watch next: Benchmarks vs ONNX Runtime/Treelite, shared-library or FFI targets, and richer preprocessing pipelines (possibly ONNX-fused).
