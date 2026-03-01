# Unsloth Dynamic 2.0 GGUFs

- Score: 193 | [HN](https://news.ycombinator.com/item?id=47192505) | Link: https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs

### TL;DR
Unsloth Dynamic 2.0 is a new quantization scheme for GGUF LLMs that chooses per-layer bit-widths and formats using a large, curated calibration set, aiming to match the original model’s behavior. It evaluates quality with KL divergence and careful MMLU replication instead of just perplexity, and often beats standard imatrix and even Google’s Gemma 3 QAT on accuracy vs disk size. HN discussion centers on impressive Qwen3.5 local performance, VRAM limits, and whether this announcement is genuinely new.

---

### Comment pulse
- Unsloth Qwen3.5 GGUFs give 200k–256k context at 60–110 tok/s on RTX 5080/4090 rigs → quantization plus CPU offload let models exceed VRAM limits.  
- Bigger-model-quantized vs smaller-model-higher-bit: users report Q3 120B (fits in 64GB) generally beats Q4 of a smaller model when quantization is solid.  
- Some suspect the post is old/SEO; others clarify it’s tied to fresh Qwen3.5 dynamic-quant benchmarks and see it as a meaningful technical update — counterpoint: communication felt confusing.

---

### LLM perspective
- View: Treating KL divergence and “flip” rates as primary metrics makes quantization research more scientifically grounded and comparable across toolchains.  
- Impact: Local-LLM users on consumer GPUs, especially Apple Silicon and mixed CPU/GPU setups, gain higher-accuracy, longer-context models in smaller footprints.  
- Watch next: Independent Aider/MMLU Pro benchmarks for more models, llama.cpp/vLLM integration maturity, and whether other vendors adopt similar dynamic per-layer quant schemes.
