# Deterministic Fully-Static Whole-Binary Translation Without Heuristics

- Score: 289 | [HN](https://news.ycombinator.com/item?id=48117810) | Link: https://arxiv.org/abs/2605.08419

### TL;DR
Elevator is a static translator that converts entire x86‑64 binaries to AArch64 without heuristics or runtime help by enumerating every feasible interpretation of each byte. This yields huge binaries (with large code-size growth and multi‑fold slowdown vs native) but fully deterministic, testable output suitable for certification and signing, unlike JITs. HN discussion highlights that beating widely used generic JIT emulators is expected, with some specialized translators remaining faster, yet regulated environments may value Elevator’s predictability over performance and size.

---

### Comment pulse
- Elevator vs JITs → Beating QEMU’s TCG JIT seems easy; specialized x86↔AArch64 JITs are faster — counterpoint: some domains prize static determinism over speed.
- Cost of guarantees → Exploring all possible code paths inflates .text by ~50× and slows runtime ~5×; prototype also lacks threading, exceptions, full ISA coverage.
- Indirect jumps → A simple method maps source addresses to translated blocks via a table; slower than direct jumps but indirect branches are infrequent.

---

### LLM perspective
- View: Treating every byte as code and data resembles exhaustive symbolic decoding; conceptually simple, trading human heuristics for mechanical completeness.  
- Impact: Could extend software lifetimes by migrating unmaintained x86 binaries onto cheaper ARM hardware in safety-critical or highly regulated deployments.  
- Watch next: Techniques to shrink binaries without losing soundness, plus added support for multithreading, signals, and Linux exception unwinding.
