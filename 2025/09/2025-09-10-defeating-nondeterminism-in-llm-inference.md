# Defeating Nondeterminism in LLM Inference

- Score: 178 | [HN](https://news.ycombinator.com/item?id=45200925) | Link: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/

TL;DR
Most “temperature 0” nondeterminism isn’t GPU randomness; it’s batch-size–dependent numerics. Kernels in LLM forward passes are run-to-run deterministic yet not batch-invariant, so varying server load changes reduction order in RMSNorm, matmuls, and attention. The authors implement batch‑invariant kernels (fixed reduction orders, fixed split-size attention, consistent KV layout) via FlexAttention/torch.Library, yielding identical outputs and enabling true on-policy RL, with ~1.6× overhead. HN notes practical limits (context/paraphrase variance), prior art (JAX), and regulatory motivations for determinism.

Comment pulse
- Determinism helps debugging and compliance, but doesn’t solve context- or paraphrase-variance → same input should repeat; context is input — counterpoint: desire invariance misreads LLMs.
- Known issue in JAX/XLA: batch variance and reduction-order effects documented; this write-up systematizes and demonstrates an end-to-end deterministic path.
- Real-world gotchas: UIs set temperature to epsilon; regulated domains require reproducibility and audit trails, making nondeterminism costly or unacceptable.

LLM perspective
- View: Batch-size variation, not GPU randomness, drives user-visible nondeterminism; enforce batch-invariant reductions across RMSNorm, matmul, attention.
- Impact: Deterministic inference enables precise bug repro, stable evals, and true on-policy RL; cost is ~20–60% throughput loss today.
- Watch next: Upstream fixed-split attention, vendor deterministic modes, and benchmarks across GPUs/models to quantify trade-offs versus cuBLAS/FlashInfer at low batch.
