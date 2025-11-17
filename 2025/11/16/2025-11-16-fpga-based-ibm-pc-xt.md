# FPGA Based IBM-PC-XT

- Score: 129 | [HN](https://news.ycombinator.com/item?id=45945784) | Link: https://bit-hack.net/2025/11/10/fpga-based-ibm-pc-xt/

TL;DR
Builder recreates an IBM PC/XT around a low‑power NEC V20 and 1 MB SRAM, with an FPGA as the chipset: CGA/EGA, PIT/PIC, SPI SD “fixed disk” via an INT13h option ROM, Adlib‑compatible audio (jtopl YM3812 → real YM3014 DAC), and a PS/2‑to‑serial mouse bridge. A bus‑cycle state machine, emulator, and Supersoft diagnostics eased bring‑up. Piezo “seek” clicks add nostalgia. HN praises the hybrid design, debates the “FPGA‑based” label, and asks why not use onboard SDRAM—answer: SRAM simplicity over writing a DRAM controller.

Comment pulse
- Hybrid authenticity over pure FPGA → Real V20 CPU, YM3014 DAC, external SRAM; FPGA supplies video, disk, glue — counterpoint: title suggests a fully FPGA computer.
- Use board SDRAM instead of SRAM → Author chose SRAM for ease; DRAM controller complexity deferred; potential future swap after learning curve.
- Bus timing concerns → V20’s 50% clock and FPGA‑derived phases simplified control; early write‑sampling bug fixed; stable operation at 10 MHz.

LLM perspective
- View: Smart hybrid: FPGA for mutable chipset; real V20 and DAC preserve period behavior and 3.3V interfacing simplicity.
- Impact: Makes DIY retro PCs more approachable; reduces reliance on scarce parts while keeping cycle‑accurate “feel.”
- Watch next: SDRAM controller integration, ISA slots, higher clock trials, compatibility test suites for EGA/Adlib, formal verification.
