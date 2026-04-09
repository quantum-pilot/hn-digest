# I ported Mac OS X to the Nintendo Wii

- Score: 1151 | [HN](https://news.ycombinator.com/item?id=47691730) | Link: https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html

### TL;DR
Bryan Keller got Mac OS X 10.0 (Cheetah) running natively on a Nintendo Wii by treating it like an old PowerPC Mac with very weird peripherals. He wrote a custom bootloader to load and relocate the XNU kernel and construct a fake device tree, then incrementally patched XNU’s low‑level memory setup for the Wii’s dual-memory layout. Using IOKit, he implemented new drivers for the Hollywood SoC, SD card (via the Starlet coprocessor), dual RGB→YUV framebuffers, and USB OHCI, finally booting an unmodified installer and desktop with keyboard and mouse support.

---

### Comment pulse
- Mac OS X’s IOKit abstractions are impressively clean → once learned, they let the author “just” plug in Wii-specific drivers and watch the system come alive.  
- Doing kernel, driver, and USB reverse-engineering on planes/trains with a Wii in tow → people are as amazed by the dedication as by the tech.  
- Wii’s 88 MB RAM vs contemporary Vista PCs → highlights how much was done with little memory and how expectations for RAM have shifted.

---

### LLM perspective
- View: This is a masterclass in applied systems archaeology: reusing old abstractions (IOKit, device trees) on completely new hardware.  
- Impact: Inspires hobby OS work, teaches practical device-tree/driver patterns, and documents rare Cheetah-era kernel/USB stack behavior.  
- Watch next: Ports of 10.1+ (Puma/Jaguar), GPU/audio/network drivers, and tooling to make Wii-OS X a repeatable playground for low-level devs.
