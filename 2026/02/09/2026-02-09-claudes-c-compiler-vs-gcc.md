# Claude’s C Compiler vs. GCC

- Score: 334 | [HN](https://news.ycombinator.com/item?id=46941603) | Link: https://harshanu.space/en/tech/ccc-vs-gcc/

### TL;DR
Anthropic’s Claude-generated C compiler (CCC) is impressively capable for an AI-written project but nowhere near production-grade. In independent tests, CCC compiled all 2,844 Linux 6.9 kernel C files without front-end errors but produced broken relocations and symbol tables, so the kernel never linked. On SQLite, CCC’s binaries were 2.7–3× larger and up to 158,000× slower on subquery-heavy workloads, largely due to extreme register spilling, code bloat, ignored optimization flags, and missing debug info. Functionally correct, but practically unusable today.

---

### Comment pulse
- LLM coding agents: amazing that an AI wrote a whole compiler; critics: it’s not “working” if it can’t link a kernel or optimize—counterpoint: progress can ramp quickly with human experts.
- Anthropic’s marketing is scrutinized: blog implied bootable Linux on x86/ARM/RISC-V; evidence only clearly supports RISC-V, raising concern about overstated claims.
- Discussion on compilers: CCC shows how crucial optimization is; some doubt its correctness, citing lax type checking and error ignoring, and dispute the article’s take on compiler vs linker difficulty.

---

### LLM perspective
- View: CCC is a strong proof-of-concept for AI-assisted systems programming, but exposes how fragile deep compiler engineering is.
- Impact: Near-term, CCC is a research/teaching artifact; GCC/Clang remain mandatory for real workloads and performance-sensitive code.
- Watch next: concrete wins would be real -O tiers, improved register allocation, fixed relocations, and transparent, independently reproduced kernel/SQLite benchmarks.
