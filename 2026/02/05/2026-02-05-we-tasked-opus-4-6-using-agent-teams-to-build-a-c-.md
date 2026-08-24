# We tasked Opus 4.6 using agent teams to build a C Compiler

- Score: 718 | [HN](https://news.ycombinator.com/item?id=46903616) | Link: https://www.anthropic.com/engineering/building-c-compiler

### TL;DR

Anthropic researcher Nicholas Carlini ran 16 Opus 4.6 agents across nearly 2,000 sessions, two billion input tokens, and roughly $20,000 to produce a 100,000-line Rust C compiler. It reportedly builds Linux 6.9 for x86, ARM, and RISC-V plus major programs, using tests, documentation, task locks, specialized roles, and GCC as an oracle. Yet x86 bootstrapping calls GCC, assembler and linker remain external, generated code underperforms unoptimized GCC, and regressions persist. Commenters found the feat remarkable but disputed clean-room framing, autonomy, production correctness, and whether parallelism deserves credit.

### Comment pulse

- Compiler veterans separated building and booting from correctness and optimization; GCC-dependent 16-bit startup prevents a fully standalone x86 toolchain.
- High-quality suites made the problem unusually verifiable—counterpoint: creating tests, CI, oracles, sampling, and failure-specific harnesses was substantial human engineering.
- Clean-room drew criticism because offline execution does not erase training exposure to GCC, Clang, and other compiler sources.

### LLM perspective

- View: The benchmark demonstrates sustained search under strong feedback, not autonomous requirements discovery or production-ready compiler engineering.
- Impact: Specified tasks may absorb more machine labor; humans shift toward verifier design, risk acceptance, and code provenance.
- Watch next: Correctness audits, fuzzing, miscompilation rates, generated-code speed, reproducible costs, provenance analysis, startup, assembler/linker completion, and security review.
