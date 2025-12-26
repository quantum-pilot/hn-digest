# Python 3.15’s interpreter for Windows x86-64 should hopefully be 15% faster

- Score: 297 | [HN](https://news.ycombinator.com/item?id=46384167) | Link: https://fidget-spinner.github.io/posts/no-longer-sorry.html

## TL;DR
Python 3.15 adds a tail-call–threaded interpreter, using `musttail` attributes on Clang and now MSVC, which breaks the 12k-line monolithic eval loop into many tiny functions. This lets compilers inline and optimize bytecode handlers much more effectively, instead of being blocked by giant-function heuristics. Benchmarks show ~5% geomean speedup on macOS AArch64 and roughly 15% on Windows x86-64 with MSVC 18/VS 2026, with some pure-Python workloads seeing 40%+ gains. HN discussion focuses on correctness, tooling details, and expectations of CPython performance.

---

## Comment pulse
- Tail-call implementation details → `Py_MUSTTAIL` macro maps to `[[msvc::musttail]]` / `__attribute__((musttail))`; MSVC attribute placement is finicky, now properly documented.  
- Reliability concerns → commenters recall 3.14’s LLVM bug; appreciate the author’s explicit “share early” philosophy and that new design encodes the desired control flow, reducing heuristic fragility.  
- Broader expectations → some expect hand-tuned asm; others note Python historically favored simplicity over speed, musttail is very new, and Windows wasn’t the main perf target anyway.

---

## LLM perspective
- View: Tail-call interpreters show that reshaping interpreter structure can beat micro-tweaks when compilers struggle with giant dispatch loops.  
- Impact: Windows-centric Python shops, GUI tools, and pure-Python libraries gain most; C-extension–heavy workloads see less benefit.  
- Watch next: Public MSVC builds, wider benchmarking across real apps, and interaction with future JIT efforts and alternative interpreter designs.
