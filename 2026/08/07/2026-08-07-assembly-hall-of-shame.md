# Assembly Hall of Shame

- Score: 226 | [HN](https://news.ycombinator.com/item?id=49214098) | Link: https://github.com/xoreaxeaxeax/asm-hall-of-shame

### TL;DR

This contest reverses normal optimization work by finding the slowest possible execution of one noninterruptible CPU instruction. Its x86 ladder progresses from a one-cycle `nop` through microcode assists, split locks, exhausted entropy, cache writeback, I/O, and pathological PCIe MMIO reads. The champion runs `fxrstor64` against a 512-byte high-latency MMIO region while other cores saturate the fabric, taking about 198 billion normalized cycles—or 62 seconds—on a Ryzen 7 5800H. Traps may count only entry time; hardware must remain stock.

### Comment pulse

- Some questioned whether a 12-millisecond ACPI-port read violates the rule by executing an SMM handler.
- The slow-instruction research has security relevance: a related experiment used pathological MMIO loads to undermine System Management Mode.
- Readers enjoyed the inversion, comparing it with Core War and joking that `nop` is infinitely slow per useful work.

### LLM perspective

- View: Pessimization exposes obscure microarchitectural paths that ordinary benchmarks never exercise.
- Impact: Extreme latency cases can reveal denial-of-service and firmware-isolation weaknesses.
- Watch next: Proposed 8 KB AMX `xrstor64` attempt and future ARM or RISC-V entries.
