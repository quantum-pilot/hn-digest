# Python 3.15’s interpreter for Windows x86-64 should hopefully be 15% faster

- Score: 297 | [HN](https://news.ycombinator.com/item?id=46384167) | Link: https://fidget-spinner.github.io/posts/no-longer-sorry.html

### TL;DR

CPython 3.15 may make Windows x86-64 execution roughly 15–16% faster by using MSVC’s experimental mandatory tail calls instead of a switch-based interpreter. Separating bytecode handlers into functions appears to restore compiler inlining defeated by CPython’s 12,000-line evaluation loop; public Visual Studio 2026 tests showed 14% on xDSL and larger microbenchmark gains. macOS AArch64 sees about 5%. HN welcomed the transparent, preliminary framing after an earlier LLVM-skewed claim, while debating portability, maintenance, and why the interpreter was not already hand-optimized.

### Comment pulse

- Evidence quality → commenters accepted early disclosure because public scrutiny caught the prior compiler bug and improved CPython.
- Design control → explicit tail calls reduce dependence on unstable optimizer heuristics while unlocking inlining.
- Engineering priorities → assembly advocates saw easy savings — counterpoint: portable hand-tuned interpreters are costly, and MSVC support is brand new.

### LLM perspective

- View: Reshaping source for compilers can outperform increasingly elaborate tuning of one enormous dispatch function.
- Impact: Windows Python workloads may gain broadly without application changes if official binaries adopt the experimental path.
- Watch next: Verify independent pyperformance results, regression outliers, MSVC feature stability, and final Python 3.15 packaging.
