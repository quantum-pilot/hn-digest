# Gemma 4 QAT models: Optimizing compression for mobile and laptop efficiency

- Score: 236 | [HN](https://news.ycombinator.com/item?id=48414653) | Link: https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/

### TL;DR

Google released quantization-aware Gemma 4 checkpoints in Q4_0 and a mobile-specific format, training around low precision rather than compressing only afterward. The mobile scheme precomputes activation scales, aligns channels to edge accelerators, applies 2-bit quantization selectively, and compresses embeddings and KV cache. An E2B text-only build uses under 1 GB; Q4_0 weights support llama.cpp, Ollama, LM Studio, vLLM, MLX, and others. HN welcomed usable local multimodality and a 6.7 GB 12B option, but exposed confusion over whether tested artifacts were QAT and whether benchmark charts compared against truly unquantized BF16.

### Comment pulse

- Artifact identity is unclear → one 3.2 GB LiteRT model handled SVG, images, and audio, but readers questioned whether it was QAT.
- Benchmark labels mislead → BF16 QAT Q4_0 stores four-bit values in a wider container; it is not the original unquantized BF16 baseline.
- Packaging lags capability → the 6.7 GB 12B quant should fit 16 GB Macs — counterpoint: Google Edge Gallery still marks it unsupported.

### LLM perspective

- **View:** QAT’s value is predictable deployable quality at the precision users actually run, not merely a smaller download.
- **Impact:** Phones and ordinary laptops gain local, offline text and multimodal inference with broader runtime choice.
- **Watch next:** Publish matched BF16, PTQ, and QAT benchmarks across quality, latency, energy, context length, and device classes.
