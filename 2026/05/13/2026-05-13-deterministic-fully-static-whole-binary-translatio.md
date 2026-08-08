# Deterministic Fully-Static Whole-Binary Translation Without Heuristics

- Score: 289 | [HN](https://news.ycombinator.com/item?id=48117810) | Link: https://arxiv.org/abs/2605.08419

### TL;DR

Elevator deterministically translates whole x86-64 executables into self-contained AArch64 binaries without source, debug symbols, layout assumptions, heuristics, or runtime fallback. It treats every byte as potentially data, opcode, or operand, builds a superset control-flow graph, and pre-generates each feasible path from ISA-derived code tiles, pruning only abnormal termination. SPECint 2006 results match or beat QEMU user-mode JIT, while producing inspectable, testable, certifiable, signable output. Commenters emphasized the tradeoff: roughly 50× text growth, sevenfold executed instructions, incomplete ISA coverage, single-threading, and no exception unwinding.

### Comment pulse

- Certification was the standout use case because regulated systems require deployed code to match reviewed artifacts and may prohibit JITs.
- QEMU is a broad multiarchitecture baseline — counterpoint: specialized Box64 and FEX reportedly run faster where JIT is allowed.
- Indirect jumps can map original targets to translated blocks through a lookup table, adding overhead mainly outside tight loops.

### LLM perspective

- View: Determinism and ahead-of-time verifiability, not peak speed or compactness, define Elevator’s novelty.
- Impact: Legacy binaries could migrate across architectures in aviation, medical, and other assurance-heavy environments.
- Watch next: Threads, exceptions, full-ISA support, binary-size reduction, and specialized-translator comparisons.
