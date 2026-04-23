# XOR'ing a register with itself is the idiom for zeroing it out. Why not sub?

- Score: 199 | [HN](https://news.ycombinator.com/item?id=47859861) | Link: https://devblogs.microsoft.com/oldnewthing/20260421-00/?p=112247

### TL;DR
Chen asks why x86 assembly almost always uses `xor r, r` to zero a register instead of equally short `sub r, r`, which even leaves flags “cleaner”. Architecturally, modern x86 cores special‑case both as zeroing idioms with zero-cycle latency and dependency breaking, so they’re effectively identical. The dominance of `xor` seems to have come from early compiler behavior, Intel recommendations, and social convention, not hard technical necessity. Discussion explores microarchitectural intuition, historical CPU quirks, and even steganographic uses of the xor/sub choice.

---

### Comment pulse
- XOR seems “obviously faster” due to no carry propagation → but real CPUs use fast adders, so SUB matches XOR’s single-cycle latency.
- Historical and vendor quirks: IBM code culture favored `sub`, Z80’s flag behavior favored `xor`; some small IBM CPUs special-cased `xor r,r` for error-handling.
- Steganography/style: choosing `xor r,r` vs `sub r,r` (or encoding variants) can hide bits or fingerprint an assembly programmer’s style.

---

### LLM perspective
- View: This is a case study in how folklore, docs, and compilers cement idioms beyond their technical necessity.
- Impact: Assembly programmers, compiler writers, and performance tuners should prioritize clarity and portability over micro-optimizing indistinguishable idioms.
- Watch next: Benchmark zeroing idioms across non‑x86 CPUs; examine toolchains for how they normalize or preserve xor/sub stylistic differences.
