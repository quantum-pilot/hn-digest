# I Ported Coreboot to the ThinkPad X270

- Score: 285 | [HN](https://news.ycombinator.com/item?id=47130860) | Link: https://dork.dev/posts/2026-02-20-ported-coreboot/

### TL;DR

A developer ported coreboot to a Kaby Lake ThinkPad X270 by adapting the similar X280 board definition. They externally dumped and reflashed SPI firmware with an RP2040, preserved Intel descriptor, Ethernet, and Management Engine regions, repaired a capacitor accidentally knocked from the board, and debugged a partial boot where NVMe and Wi-Fi vanished. Schematics revealed the X270’s PCIe clock-request routing differed; correcting those allocations produced working GRUB, Guix, NVMe, and wireless. Changes are being upstreamed. HN discussed open firmware’s auditability and debugging value, alongside remaining opaque auxiliary processors.

### Comment pulse

- A nearby board port reduced blind debugging → the X280 template booted far enough for live-USB cbmem logs.
- Schematics resolved what firmware guesses could not → one shifted CLKREQ mapping disabled both Wi-Fi and NVMe.
- Open firmware increases owner control → counterpoint: Intel ME and other embedded processors prevent complete transparency.

### LLM perspective

- **View:** Firmware freedom remains hardware-specific reverse engineering, not a drop-in software replacement.
- **Impact:** X270 owners may gain auditable boot code and more control over platform policies.
- **Watch next:** Upstream review, model variants, suspend, thermal and battery behavior, peripheral regressions, and reproducible installation guidance.
