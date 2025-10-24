# C64 Blood Money

- Score: 124 | [HN](https://news.ycombinator.com/item?id=45679638) | Link: https://lemmings.info/c64-blood-money/

- TL;DR
  - Mike Dailly recounts porting Blood Money to the C64 (1989–90): a multidirectional scroller built around a sprite multiplexor, scripting, sprite compression, bitmap background collision, weapons, shop, and a simultaneous two-player mode. He used the PDS host system (PC ISA card + C64 connector) for instant assembling and in-circuit debugging via BRK, and leaned on zero-page allocation and custom IRQs. HN debates host-vs-target workflows (Turbo Assembler/REU vs UNIX/VAX workstations), notes later parts appear password-gated, and shares current Linux-friendly C64 toolchains.

- Comment pulse
  - Studios used host systems → PDS-like setups sped builds, enabled live memory pokes — counterpoint: many demosceners/small teams shipped using Turbo Assembler+REU on-device.
  - Access concern → Parts 2–3 appear password-locked with no instructions; readers suspect Patreon gating.
  - Today’s tooling → ca65/cc65, oscar64 C compiler, and web IDEs integrate with VICE; Linux support is solid.

- LLM perspective
  - View: Living documentation of 6502-era engine design and workflow under extreme constraints.
  - Impact: Bitmap-collision and sprite-multiplexor patterns inform embedded, FPGA, and retro homebrew.
  - Watch next: Release source/build scripts; publish IRQ/multiplexor benchmarks; document PDS protocol for modern hot-reload.
