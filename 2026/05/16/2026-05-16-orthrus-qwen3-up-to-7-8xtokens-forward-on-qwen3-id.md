# Orthrus-Qwen3: up to 7.8×tokens/forward on Qwen3, identical output distribution

- Score: 217 | [HN](https://news.ycombinator.com/item?id=48154865) | Link: https://github.com/chiennv2000/orthrus

### TL;DR
Orthrus is a modified Qwen3-family model that generates multiple future tokens in parallel via a diffusion-style “second view,” yet guarantees **bit-identical** output distribution to the original autoregressive model. It shares the same KV cache between views, adds only modest fine-tuning (≈16% of parameters), and reports 4–5× average speedups (up to 7.8× tokens per forward) on Qwen3 models. HN discussion notes this mainly improves **single-user latency** and local inference, not cloud provider throughput or compute cost.

---

### Comment pulse
- Cloud congestion relief? → Not really: Orthrus adds compute per token; big providers prioritize batched throughput over single-stream latency — counterpoint: better local models reduce dependence on them.  
- How it works → Moves bottleneck: predicts multiple tokens in parallel, then verifies; saves memory traffic, increases utilization, slightly increases total FLOPs per accepted token.  
- Local users’ hopes → Strong interest in GGUF/quantized Qwen/DeepSeek support; current multi-token prediction paths offer ~1.5–2× speedups on larger models.

---

### LLM perspective
- View: “Lossless” parallel decoding is a strong primitive; expect similar schemes across major open-weight backbones.  
- Impact: Biggest gains for hobbyists, on-prem, and latency-sensitive tools (coding, chat) at low batch sizes.  
- Watch next: Real-world benchmarks on consumer GPUs, GGUF/quantization support, and integration into vLLM/SGLang-style serving stacks.
