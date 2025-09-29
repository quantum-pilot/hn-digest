# The Weird Concept of Branchless Programming

- Score: 108 | [HN](https://news.ycombinator.com/item?id=45405750) | Link: https://sanixdk.xyz/blogs/the-weird-concept-of-branchless-programming

- TL;DR
    - The article demystifies branchless programming: replacing unpredictable branches with arithmetic, masks, and cmov/setcc/adc to keep pipelines full. C examples (abs, clamp, quicksort partition) show negligible gains for predictable branches and a modest speedup when comparisons are data-dependent. It advises using branchless techniques selectively (hot loops, crypto, SIMD). HN pushes back: modern compilers already lower simple conditionals to branchless, the benchmarks are too crude, and better demos (e.g., CRC, constant‑time crypto) show bigger wins.

- Comment pulse
    - Compilers already generate branchless for simple conditionals → ?: and if often compile to cmov/setcc; verify assembly. — counterpoint: For control-critical code, write/inspect assembly.
    - Benchmarks are weak → millisecond precision and small inputs mask differences; reruns show branchless sometimes slower with -O3, faster only at O0.
    - Use cases with real gains → CRC and constant-time crypto see large speedups and side-channel mitigation due to unpredictable, data-dependent branches.

- LLM perspective
    - View: Treat branchless as a surgical optimization; prefer clarity, profile hotspots, leverage compiler vectorization/intrinsics.
    - Impact: Biggest benefits in unpredictable tight loops, crypto, and SIMD kernels; limited or negative on well-predicted branches.
    - Watch next: Publish rigorous microbenchmarks with perf counters and disassembly; include CRC, LUT, SIMD on x86/ARM/RISC-V.
