# Assembly Hall of Shame

- Score: 226 | [HN](https://news.ycombinator.com/item?id=49214098) | Link: https://github.com/xoreaxeaxeax/asm-hall-of-shame

## TL;DR

A security researcher built an “Assembly Hall of Shame” leaderboard for the *slowest possible* single CPU instructions, turning microarchitectural quirks into a sport. By abusing MMIO, PCIe fabric congestion, microcode assists and weird device registers, they push instructions that normally take nanoseconds into milliseconds or even seconds. The current x86 champion is `fxrstor64` loading FPU state from a high-latency MMIO region while other cores hammer the bus, stretching one instruction to 62 seconds. HN admires the ingenuity, debates rules, and notes the broader exploit potential.

---

## Comment pulse

- Rule nitpicking → Some suspect the very slow ACPI port I/O likely traps into System Management Mode, arguably timing SMM handlers—counterpoint: author’s rules say only trap latency should count.  
- Author meta → Mixed views on the playful, bloggy tone; several cite his earlier hardcore tools (sandsifter, smiiiiii, “only-mov” compiler) as serious research.  
- Culture/humor → Comparisons to Core War and jokes that `nop` is “infinitely slow for what it does” reflect HN’s fondness for playful low-level antics.

---

## LLM perspective

- View: Treating worst-case latency as a game systematically exposes obscure microarchitectural behaviors and potential abuse surfaces.  
- Impact: Kernel, hypervisor, and firmware developers gain concrete worst-case timings for SMM, MSRs, MMIO, and fabric contention.  
- Watch next: ARM/RISC‑V leaderboards, reproductions on newer server CPUs, and whether vendors quietly clamp down on these pathological cases.
