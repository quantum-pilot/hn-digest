# Claude’s C Compiler vs. GCC

- Score: 334 | [HN](https://news.ycombinator.com/item?id=46941603) | Link: https://harshanu.space/en/tech/ccc-vs-gcc/

### TL;DR

A benchmark compares Claude-generated CCC with GCC 14.2 on Linux 6.9 and SQLite 3.46. CCC compiled 2,844 kernel C files but failed final linking with 40,784 undefined references. Its SQLite build returned correct results and passed five edge tests, yet the benchmark took 2 hours 6 minutes versus GCC’s 10.3 seconds at -O0; binaries were about 2.8 times larger, compiler memory 5.9 times higher, and optimization flags changed nothing. Commenters agreed the prototype is remarkable but challenged calling error-free compilation correctness, disputed parts of the analysis, and split over potential.

### Comment pulse

- Compilation is not a bootable kernel → successful translation of source files does not establish semantically correct object code or linking.
- Optimization dominates native performance → CCC spills registers heavily, emits bloated code, and treats every optimization level identically.
- Progress framing divides readers → counterpoint: rapid generation is striking, but comparisons were invited by claims of bootable multi-architecture Linux.

### LLM perspective

- View: CCC demonstrates agent-produced systems breadth, while GCC demonstrates the accumulated depth hidden behind production-tool reliability and optimization.
- Impact: Compiler engineers remain essential for semantics, code generation, diagnostics, debugging metadata, relocation correctness, and trustworthy evaluation.
- Watch next: Kernel configurations, invalid-code rejection, independent benchmarks, register allocation, linker fixes, symbol generation, optimization tiers, and agent-maintained improvement velocity.
