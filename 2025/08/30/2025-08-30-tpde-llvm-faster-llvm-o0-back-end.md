# TPDE-LLVM: Faster LLVM -O0 Back-End

- Score: 165 | [HN](https://news.ycombinator.com/item?id=45072481) | Link: https://discourse.llvm.org/t/tpde-llvm-10-20x-faster-llvm-o0-back-end/86664

- TL;DR
  - TPDE-LLVM is an alternative fast baseline back-end for LLVM that compiles 10–20x faster than -O0 while running about as fast, with 10–30% larger code, on x86-64/AArch64. It uses three compact passes (prep, analysis, combined lowering+regalloc+emit) and is aimed at debug/JIT; on optimized IR, LLVM still wins on speed and size. HN notes this only accelerates the back-end, but real users (e.g., Wasmer) are interested. Limits include partial IR coverage and vector legalization; “copy-and-patch” compiles faster but runs ~2.5x slower.

- Comment pulse
  - Backend acceleration only → front-end often 50–80% of -O0 builds; with TPDE, >98% front-end. Best for debug/JIT; supports most clang/rustc IR; linking minor.
  - Scope is narrower than LLVM back-end; vectors/legalization incomplete. Some worry LLVM IR semantics — counterpoint: TPDE avoids many exotic types to keep correctness manageable.
  - Copy-and-Patch is faster but ~2.5x slower at runtime due to registers. Wasmer plans trials; AArch64 speedups higher because GlobalISel -O0 is slower than FastISel.

- LLM perspective
  - View: A specialized -O0 backend delivering order-of-magnitude compile speedups without harming debug runtime fills a longstanding tooling gap.
  - Impact: Largest wins in JITs, IDE live builds, tests; rustc/clang integrations could shift dev workflows away from Cranelift/fast paths.
  - Watch next: DWARF support, better regalloc, vector legalization; measure end-to-end wall time on large C++/Rust repos; upstreamability and multi-target coverage.
