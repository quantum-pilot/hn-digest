# Same-day upstream Linux support for Snapdragon 8 Elite Gen 5

- Score: 309 | [HN](https://news.ycombinator.com/item?id=46070668) | Link: https://www.qualcomm.com/developer/blog/2025/10/same-day-snapdragon-8-elite-gen-5-upstream-linux-support

## TL;DR
Qualcomm published initial Linux upstream support for its new Snapdragon 8 Elite Gen 5 SoC within a day of launch, including kernel patches for CPUs, power, storage, Wi‑Fi/Bluetooth, camera, audio, video, and partial display/GPU support, plus a Debian 13 reference image and detailed how‑tos. HN readers welcome the shift toward launch‑day upstreaming but note major gaps: older Snapdragon generations remain stuck on vendor kernels, the boot chain and BSP are still tightly locked down, and business motives—not a FOSS conversion—are driving this.

## Comment pulse
- Good step but ecosystem still closed → proprietary boot chain, hypervisor-only OEM code, incomplete mainlining for earlier gens, weak BSP/docs; some engineers now avoid Qualcomm.
- Seen as profit-motivated, not ideological → upstreaming lowers long-term support pain, enables non‑Android uses, and mirrors Valve’s success with open Linux support.
- Enthusiasts hopeful for ARM Linux boxes → yet device-specific devicetrees and scarce hardware mean little near-term desktop impact — counterpoint: strong SoC-level support is a prerequisite.  

## LLM perspective
- View: Treating upstream enablement as “day one” work is a meaningful cultural and process change for an ARM SoC vendor.  
- Impact: Kernel developers and embedded OEMs get faster bring-up, longer support horizons, and less reliance on opaque vendor trees.  
- Watch next: Backporting to Gen4/4.5, any loosening of boot-chain restrictions, and real products shipping with near‑mainline kernels.
