# Fp8 runs ~100 tflops faster when the kernel name has "cutlass" in it

- Score: 328 | [HN](https://news.ycombinator.com/item?id=45458948) | Link: https://github.com/triton-lang/triton/pull/7298

### TL;DR

A Triton pull request rewrote an attention kernel to remain persistent, improving some low-context performance while exposing a striking compiler behavior: adding “cutlass” to an FP8 kernel name enabled a ptxas optimization and raised measured throughput by roughly 100–150 TFLOPS in some cases. Disassembly discussion indicated the name check was hard-coded. Contributors suggested the optimization may be experimental and selectively enabled because it helps some kernels but harms others. The same rewrite also reduced performance for some dimension-64 cases.

### Comment pulse

- Compiler practitioners said name-based gates can safely restrict unstable optimizations, though they create opaque coupling and collision risks.
- Readers compared the behavior with historical benchmark-specific compiler and driver optimizations.

### LLM perspective

- View: A function name affecting code generation is pragmatic vendor signaling but a brittle, undocumented interface.
- Impact: Performance can hinge on invisible heuristics, undermining reproducibility and portable tuning.
- Watch next: Explicit compiler attributes and published scheduling criteria would replace accidental naming contracts.
