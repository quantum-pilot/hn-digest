# I ported Mac OS X to the Nintendo Wii

- Score: 1151 | [HN](https://news.ycombinator.com/item?id=47691730) | Link: https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html

### TL;DR

Bryan Keller got Mac OS X 10.0 Cheetah running natively on the Wii by exploiting their related PowerPC lineage, then replacing nearly everything around it. A custom bootloader loads Mach-O XNU, supplies boot arguments and a hard-coded device tree, and injects Wii-specific drivers. Kernel patches adapt memory mappings; new IOKit drivers expose the Hollywood SoC, SD storage, dual RGB/YUV framebuffers, and USB input. Serial logs, LED-instruction patches, disassembly, old source archives, and travel-time debugging turned an apparently impossible port into a usable desktop.

### Comment pulse

- Readers praised IOKit’s provider-client abstractions → new Wii drivers could slot beneath existing storage, graphics, and USB families.
- The travel photos became part of the legend → kernel debugging beside a Wii in economy seating signaled unusual persistence.
- Retro-port authors welcomed the result → prior NetBSD, Linux, and Windows work supplied both inspiration and technical precedents.

### LLM perspective

- **View:** The port succeeds by preserving Darwin’s abstractions while replacing only boot and hardware-specific layers.
- **Impact:** Retro OS developers gain a documented template for adapting old PowerPC software to unconventional hardware.
- **Watch next:** Mac OS X 10.1 support, remaining hardware drivers, upstream documentation, and long-term reproducibility of the build environment.
