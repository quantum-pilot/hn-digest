# 486Tang – 486 on a credit-card-sized FPGA board

- Score: 134 | [HN](https://news.ycombinator.com/item?id=45232565) | Link: https://nand2mario.github.io/posts/2025/486tang_486_on_a_credit_card_size_fpga_board/

- TL;DR
  - 486Tang ports the ao486 MiSTer PC core to a Sipeed Tang Console (Gowin GW5A), using SDRAM as main memory (double‑pumped to emulate 32‑bit words), DDR3 for the framebuffer, and SD‑backed IDE with a bootloader that pulls BIOS/VGA BIOS/CMOS/IDENTIFY from the SD card. Whole‑system Verilator simulation (BIOS port 0x8888 logs, scoped tracing, Bochs listings) enabled rapid bring‑up and bug isolation. Optimizations—reset fan‑out replication, simpler fetch‑queue accounting, and a 4‑way TLB—pushed performance to roughly 486SX‑20 (+35%). HN debated SDRAM vs. era‑correct FPM/EDO, DDR3’s minimum‑frequency pain, and x86‑compatible alternatives.

- Comment pulse
  - SDRAM over DDR3 for main RAM → flexible clocks and simpler integration; DDR3 suits video bursts—counterpoint: era‑correct would be FPM/EDO, not SDRAM.
  - “Buy a 486 CPU” → Vortex86/VIA Eden exist, but are too fast and OS/timer quirks break cycle‑timed software.
  - Interest in a tiny, ready‑to‑use 486 PC → Tang Console is affordable; complete boxed solutions face cost and peripheral integration trade‑offs.

- LLM perspective
  - View: Smart memory/IO mapping plus Verilator-first workflow makes complex x86 FPGA ports feasible on low-cost boards.
  - Impact: Broadens ao486 beyond Altera; encourages Gowin ecosystem and cross‑vendor portability for retro‑PC cores.
  - Watch next: Publish DOS/Windows benchmarks, Doom FPS, IDE throughput; refine TLB/cache; upstream patches and release ready‑to‑flash SD images.
