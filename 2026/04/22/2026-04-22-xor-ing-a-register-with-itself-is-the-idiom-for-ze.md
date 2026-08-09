# XOR'ing a register with itself is the idiom for zeroing it out. Why not sub?

- Score: 199 | [HN](https://news.ycombinator.com/item?id=47859861) | Link: https://devblogs.microsoft.com/oldnewthing/20260421-00/?p=112247

### TL;DR

`xor eax,eax` and `sub eax,eax` are equally short zeroing idioms on modern x86, and Intel recognizes both during decoding, renames the destination to an internal zero register, skips execution, and breaks dependency chains. `sub` even clears the auxiliary-carry flag that `xor` leaves undefined. Raymond Chen argues `xor` likely won through path dependence: early compiler preference encouraged programmers and later optimizations. Hacker News debated gate-level simplicity versus identical architectural latency, noted Pentium Pro reportedly optimized only `xor`, contrasted IBM’s `sub` tradition, and proposed using equivalent encodings as a steganographic bit channel.

### Comment pulse

- XOR’s independent bit gates can use less energy — counterpoint: register files and out-of-order machinery dominate while both idioms have one-cycle latency.
- IBM systems sometimes favored `sub`; some smaller processors uniquely let self-`xor` bypass parity checks when clearing corrupted storage.
- Assembly choices reveal authorial style and can encode hidden data because multiple equivalent instruction forms preserve program behavior.

### LLM perspective

- **View:** Compiler idioms coevolve: convention informs hardware optimization, then that optimization entrenches the convention.
- **Impact:** Assembly and compiler authors should prefer recognized idioms unless flags or target-specific behavior matters.
- **Watch next:** Vendor zero-idiom documentation, microarchitecture benchmarks, flag dependencies, disassembler aliases, and steganographic detection.
