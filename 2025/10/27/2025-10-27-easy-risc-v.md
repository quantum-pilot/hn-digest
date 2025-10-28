# Easy RISC-V

- Score: 142 | [HN](https://news.ycombinator.com/item?id=45726192) | Link: https://dramforever.github.io/easyriscv/

TL;DR
An interactive, browser-based primer to RISC‑V assembly (RV32I + Zicsr) that teaches registers and core ops, control flow (branches/jumps/jalr), memory and smaller widths, calling conventions and the stack, memory‑mapped I/O, and position‑independent code with auipc—ending with exceptions and a tiny OS. HN discussion highlights its MIPS lineage and contrasts RISC‑V’s conservative base/extension model with AArch64’s pragmatic fused operations. Commenters note minor errata (two’s‑complement negation, auipc example nuance), suggest moving the first emulator earlier, and share real-world tooling/projects.

Comment pulse
- RISC‑V’s minimal ISA → easier to add than remove; keeps compiler targets simple, extensions justified — counterpoint: AArch64 fused addressing/shift ops yield performance and density.
- Erratum: negating 0x123 → 0xFFFFFEDD, not 0xFFFFFCCD; emulator shows the correct two’s‑complement result.
- PIC clarification → auipc/addi computes PC+offset; LUI loads absolute upper bits, so it’s not position‑independent.

LLM perspective
- View: Clear, hands‑on ISA teaching; covers enough to write loops, functions, I/O, PIC, and basic OS behavior.
- Impact: Lowers entry barriers for students and hobbyists; useful refresher for MIPS/AArch64 developers crossing to RISC‑V.
- Watch next: Fix errata; add RV64I/M/C material, linker relaxation, ABI details, and toolchain projects like network or Core War.
