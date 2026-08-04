# Orthrus-Qwen3: up to 7.8×tokens/forward on Qwen3, identical output distribution

- Score: 217 | [HN](https://news.ycombinator.com/item?id=48154865) | Link: https://github.com/chiennv2000/orthrus

### TL;DR

Orthrus adds a diffusion-based parallel decoding view to frozen Qwen3 models while sharing the autoregressive model’s KV cache and using consensus verification to preserve exactly the base output distribution. Fine-tuning 16% of parameters yields reported average speedups of 4.25×–5.36× across 1.7B, 4B, and 8B checkpoints, peaking at 7.8× with constant cache overhead. HN commenters welcomed the exactness and local-inference potential, but stressed that this is a latency optimization rather than a compute reduction; gains depend on whether generation, memory movement, or prompt processing is the actual bottleneck.

### Comment pulse

- Compute does not fall → parallel guesses exploit idle arithmetic, but invalid candidates are discarded; one example estimated 20% extra compute per accepted token.
- Provider congestion may worsen → large services already batch requests and are compute-bound, so favoring single-user latency can sacrifice aggregate throughput.
- Practical demand centers on compatibility → users want GGUF and quantized larger models; native vLLM and SGLang integration remains forthcoming.

### LLM perspective

- **View:** Identical distributions separate decoding acceleration from model-quality compromises, making bottleneck diagnosis the decisive adoption test.
- **Impact:** Deployment teams must profile workloads before choosing it, rather than treating headline speedups as universal.
- **Watch next:** Independent wall-clock benchmarks across context lengths, batch sizes, GPUs, quantization, and serving engines should test the reported advantage.
