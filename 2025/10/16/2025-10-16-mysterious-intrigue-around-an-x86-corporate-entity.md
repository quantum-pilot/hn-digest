# Mysterious Intrigue Around an x86 "Corporate Entity Other Than Intel/AMD"

- Score: 149 | [HN](https://news.ycombinator.com/item?id=45608285) | Link: https://www.phoronix.com/news/x86-Opcodes-Not-AMD-Or-Intel

- TL;DR
  - Veteran x86 expert Christian Ludloff posted to LKML and binutils that a corporate entity other than Intel/AMD is actively using several x86 opcode slots and E000_xxxx CPUID/MSR ranges. The encodings include 0E in PM64, 0F 36/3E, 0F 3A E0–EF across classic/VEX/EVEX maps, and 0F 1E /0 (hint NOP); historic collisions are noted but dismissed. Speculation spans VIA/Zhaoxin leveraging Cyrix’s license to hyperscalers commissioning custom instructions. Toolchain/kernel folks are asked to avoid collisions until details are published.

- Comment pulse
  - Likely VIA/Zhaoxin via Cyrix license → VIA bought Cyrix; Zhaoxin JV builds x86; history of kernel/GCC patches — counterpoint: they'd normally post directly, not anonymously.
  - Hyperscaler-specific ISA tweaks → large buyers get custom microcode/instructions; examples include AWS- and Oracle-only Xeons; internal JITs benefit at scale.
  - Could relate to FineIBT hardening → Linux reserving undefined opcode 0xD6; new allocations flagged to avoid conflicts with emerging security tooling.

- LLM perspective
  - View: Treat as a real third-party x86 core; reserve encodings in assemblers and kernels to prevent accidental reuse.
  - Impact: Toolchains and JITs must parse new maps; CPUID probing updates; clouds may expose instance types leveraging the new ops.
  - Watch next: Sandpile and vendor docs, binutils/LLVM reservations, Linux cpufeature flags, and any public microcode drops or benchmarks revealing semantics.
