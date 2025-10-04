# Fp8 runs ~100 tflops faster when the kernel name has "cutlass" in it

- Score: 328 | [HN](https://news.ycombinator.com/item?id=45458948) | Link: https://github.com/triton-lang/triton/pull/7298

- TL;DR
    - Triton rewrote its attention kernel to a persistent design: better at low context, but FP16 regresses at large context due to ptxas scheduling. Oddly, FP8 gets ~100–150 TFLOPS faster if the kernel name includes “cutlass”; the PR conditionally prefixes cutlass_ for FP8. Disassembly implies NVIDIA ptxas string‑matches “cutlass” to enable an aggressive optimization. HN debates heuristic vendor optimizations vs “cheating” precedents, stability/accuracy risks, and asks for an explicit compiler flag. Benchmarks show FP8 gains; D64 FP16 drops.

- Comment pulse
    - Name-based heuristics are common → safer to enable risky transforms for vendor libs; limited metadata — counterpoint: creates barriers and surprise breakage.
    - Performance variability is expected → GPU compiler passes help some kernels, hurt others; universal non-negative speedups are rare, so CUTLASS gating avoids regressions.
    - This echoes past “optimizations” → ATI Quake3, Intel ICC, phone benchmarks; vendor-specific tweaks are normalized in graphics but raise trust concerns elsewhere.

- LLM perspective
    - View: Treat kernel naming as a control surface; document it, but do not rely on it for correctness or portability.
    - Impact: ML infra teams can unlock FP8 speedups today by prefixing cutlass_, while guarding accuracy and A/B testing across driver versions.
    - Watch next: Look for an official ptxas flag or PTX directive; Triton may expose an opt-in; independent microbenchmarks and disassembly across architectures.
