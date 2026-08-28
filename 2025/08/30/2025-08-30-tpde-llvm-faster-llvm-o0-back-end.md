# TPDE-LLVM: Faster LLVM -O0 Back-End

- Score: 165 | [HN](https://news.ycombinator.com/item?id=45072481) | Link: https://discourse.llvm.org/t/tpde-llvm-10-20x-faster-llvm-o0-back-end/86664

### TL;DR

TPDE-LLVM is an open-source baseline backend claiming 10–20× faster code generation than LLVM 19 at `-O0`, with comparable runtime performance and typically 10–30% larger binaries. On the supplied SPEC CPU 2017 data, its geometric-mean speedup is 13.34× for unoptimized IR. It combines lowering, register allocation, and encoding in one of three passes, targeting x86-64 and AArch64. The project currently supports only a common LLVM IR subset; planned work includes DWARF, better allocation, and broader IR coverage, while optimized LLVM remains substantially faster at runtime.

### Comment pulse

- The author says Clang front-end work becomes more than 98% of compile time with TPDE, limiting whole-build gains.
- Readers debated whether the constrained feature set and maintenance burden complicate adoption despite impressive baseline results.

### LLM perspective

- View: TPDE shows how much speed LLVM’s general backend architecture leaves unavailable for baseline compilation.
- Impact: Faster edit-test loops and lower JIT startup are plausible, but gains depend on backend share of total time.
- Watch next: Rust integration, DWARF quality, vector coverage, and real-project end-to-end benchmarks will determine practical value.
