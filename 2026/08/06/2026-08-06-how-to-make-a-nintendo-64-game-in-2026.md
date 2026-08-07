# How to Make a Nintendo 64 Game in 2026

- Score: 471 | [HN](https://news.ycombinator.com/item?id=49168622) | Link: https://phoboslab.org/log/2026/08/xibalba64-making-of

### TL;DR

Dominic Szablewski turned his C rewrite of the Impact engine into Xibalba 64, a new physical N64 first-person shooter published for Modretro’s M64. Libdragon supplied the platform layer and Tiny3D drove custom RSP/RDP rendering; batching, texture-aware sorting, recursive raycasting, and 4-bit palettes overcame 4KB texture memory and delivered stable 60 FPS outside some split-screen scenes. Levels compile from JSON into endian-specific binary data, while 31 of the 32MB ROM holds VADPCM audio. HN credited modern open toolchains, emulators, flash cartridges, and homebrew communities for making fifth-generation console development approachable.

### Comment pulse

- Developers said Libdragon’s recent advances now enable bump mapping, HDR, and large seamless worlds beyond original commercial-era expectations.
- Real hardware remains essential because accurate emulators still miss memory-bandwidth behavior; USB flash cartridges make iteration nearly desktop-like.
- Physical cartridges retain appeal — counterpoint: the niche may favor piracy and emulation, leaving uncertain demand after launch.

### LLM perspective

- View: Mature community infrastructure converted a quirky proprietary console into a tractable embedded target without erasing hardware-specific constraints.
- Impact: Hobbyists can ship real cartridges and reuse portable engines, while publishers gain distinctive catalog titles for clone hardware.
- Watch next: Follow engine source release, sales longevity, audio-codec work, emulator accuracy, and performance across original consoles and M64.
