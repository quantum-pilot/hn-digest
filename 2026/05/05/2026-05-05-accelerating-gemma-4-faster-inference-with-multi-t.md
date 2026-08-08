# Accelerating Gemma 4: faster inference with multi-token prediction drafters

- Score: 414 | [HN](https://news.ycombinator.com/item?id=48024540) | Link: https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/

### TL;DR

Google released Apache-2.0 multi-token-prediction drafters for every Gemma 4 model, claiming up to 3× faster generation with identical outputs. A small drafter proposes several future tokens using the target model’s activations and shared KV cache; the full model verifies them together, accepting valid runs while preserving its original distribution. Support spans LiteRT-LM, MLX, Transformers, vLLM, SGLang, Ollama, and mobile demos. Gains depend on hardware and batching: the 26B MoE reaches roughly 2.2× on Apple Silicon at batch sizes four to eight. Commenters welcomed local gains but flagged added VRAM pressure.

### Comment pulse

- Users said Gemma often answers in fewer tokens than rivals — counterpoint: mistakes can erase savings through corrective turns.
- Local reports showed MTP lifting Qwen generation from about 20 to 55 tokens per second, while prefill slowed.
- Some preferred Gemma 4’s efficiency and intuition; others still favored Qwen’s accuracy and tunability.

### LLM perspective

- Speculative decoding converts idle compute into lower latency, but acceptance rate—not draft speed alone—determines realized benefit.
- Deployment planning must include drafter memory, projector placement, batch shape, quantization, and runtime support.
- Watch independent benchmarks across prompts, contexts, batch sizes, devices, and end-to-end energy consumption.
