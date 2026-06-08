# Speculative KV coding: losslessly compressing KV cache by up to ~4×

- Score: 140 | [HN](https://news.ycombinator.com/item?id=48400151) | Link: https://fergusfinn.com/blog/kv-entropy-coder/

### TL;DR
Speculative KV coding is a lossless compression method for LLM KV caches that uses a cheaper “predictor model” to estimate the cache, then entropy-codes only the residual error. A simple instantiation uses an FP8-quantized copy of the target model as the predictor and a Gaussian-mixture residual model, achieving ~2.4–2.7× compression over bf16, and ~3.1–3.9× over already-quantized FP8 caches (6–8× vs original bf16). It targets bandwidth-bound scenarios like cross-DC prefill and large shared/prefix caches.

### LLM perspective
- View: Treat KV as deterministic and compress its residuals against a correlated model, not as standalone random tensors.  
- Impact: Makes very long contexts and cross-machine/PCIe KV movement more viable without model-quality changes.  
- Watch next: Open-source implementations, predictor–target architecture mapping tricks, and real throughput benchmarks under vLLM/SGLang/TRT-LLM.
