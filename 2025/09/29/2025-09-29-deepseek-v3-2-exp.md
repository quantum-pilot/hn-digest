# DeepSeek-v3.2-Exp

- Score: 295 | [HN](https://news.ycombinator.com/item?id=45412098) | Link: https://github.com/deepseek-ai/DeepSeek-V3.2-Exp

- TL;DR
    - DeepSeek-V3.2-Exp is an MIT-licensed, experimental upgrade introducing DeepSeek Sparse Attention: a fine‑grained sparse attention that keeps output quality while cutting long‑context compute. Trained to parity with V3.1-Terminus across public benchmarks (e.g., MMLU‑Pro 85.0; notable gains on BrowseComp, Codeforces), it ships readable TileLang kernels and high‑performance CUDA in DeepGEMM/FlashMLA, with day‑0 vLLM/SGLang support. HN focuses on rapidly falling inference prices (plus a 50% API cut to $0.28/M input, $0.42/M output), the outsized role of KV caching, and data‑usage flags on OpenRouter.

- Comment pulse
    - Inference costs falling faster than Moore’s via optimizations/HBM/electric buildout; some expect ~10x/year declines and 1000x in five years — counterpoint: pricing has been volatile.
    - Caching dominates agent workloads; without provider KV caching, “cheap” models get expensive. DeepSeek offers KV cache hits at $0.028/M, easing this.
    - Data policy uncertainty: OpenRouter marks the model as training on prompts; users question accuracy and OpenRouter’s “openness.”

- LLM perspective
    - View: DSA pairs a learned indexer with top‑k attention, shifting cost to O(L) scanning while capping per‑query attention compute.
    - Impact: If parity holds, long‑context training/inference become cheaper, enabling larger windows, higher throughput, and more viable multi‑tool agents.
    - Watch next: Independent long‑context evals, end‑to‑end latency/throughput vs dense attention, and kernel uptake in vLLM/SGLang plus clear data‑use policies.
