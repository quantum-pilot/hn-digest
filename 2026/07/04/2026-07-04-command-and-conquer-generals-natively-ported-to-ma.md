# Command and Conquer Generals natively ported to macOS, iPhone, iPad using Fable

- Score: 303 | [HN](https://news.ycombinator.com/item?id=48788283) | Link: https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main

### TL;DR

A GPLv3 fork runs Command & Conquer: Generals—Zero Hour natively on Apple-silicon Macs, iPhones, and iPads, compiling the 2003 engine for ARM64 and translating DirectX 8 through DXVK, Vulkan, MoltenVK, and Metal. Building atop EA’s source release and community Unix/macOS ports, it adds iOS filesystem and lifecycle handling, RTS touch controls, packaging, and engine fixes; users supply assets. The author says Claude Code’s Fable model performed the C++ porting and debugging under human direction. HN called this a strong, low-stakes AI collaboration, while emphasizing inherited groundwork and grating AI-written documentation.

### Comment pulse

- The port shows an attractive AI niche → classic-game conversion is bounded, testable on real devices, reversible, and low-stakes enough for rapid iteration.
- Credit depends on lineage → prior projects supplied modernization, Unix portability, SDL3, and macOS/Linux rendering; this fork’s novel scope is primarily iOS.
- AI output quality split code from prose → commenters accepted model-written engineering — counterpoint: dense compound nouns and hype made the documentation harder to read.

### LLM perspective

- **View:** The meaningful achievement is integrating mature open-source layers across Apple’s restrictions, not regenerating an engine from nothing.
- **Impact:** Documented AI-assisted porting could lower the labor needed to preserve abandoned games when source and legal assets exist.
- **Watch next:** iPad memory use, background-resume stability, upstream acceptance, reproducible builds, touch usability, and the promised Renegade repository.
