# I Ported Coreboot to the ThinkPad X270

- Score: 285 | [HN](https://news.ycombinator.com/item?id=47130860) | Link: https://dork.dev/posts/2026-02-20-ported-coreboot/

- TL;DR  
  - An individual ports coreboot/libreboot to a ThinkPad X270 by dumping Lenovo’s BIOS via RP2040-based SPI flashing, extracting Intel ME/GbE/IFD regions, and using deguard to generate a cleaned ME image. Using the X280 coreboot port as a template, they debug subtle hardware differences (Thunderbolt removal, PCIe clock/CLKREQ wiring) that initially break NVMe and WiFi. After correcting GPIO/CLKREQ mappings, the laptop boots Guix from encrypted NVMe. The work is being upstreamed; HN discusses firmware throttling quirks, reasons to escape proprietary BIOS, and practical debugging methods.

- Comment pulse  
  - Firmware throttling hacks → X270 owners report PROCHOT-based underclocking with third‑party batteries; scripts or tools like ThrottleStop can override it—counterpoint: fixes may need firmware mods.  
  - Why replace stock BIOS → Commenters stress open firmware reduces opaque SMM behavior, aids security/debugging, and aligns control with users instead of vendors.  
  - Coreboot porting practice → Similar platforms and schematics reduced need for serial; tools like cbmem and flash logging substitute when UART isn’t exposed.

- LLM perspective  
  - View: Community firmware ports on older ThinkPads remain practical avenues for gaining transparency and repairability on x86 laptops.  
  - Impact: Successful X270 upstreaming strengthens support for Kaby Lake platforms and provides a template for nearby models with similar schematics.  
  - Watch next: Measure power, thermals, and throttling under coreboot vs stock firmware to test claims about efficiency and PROCHOT behavior.
