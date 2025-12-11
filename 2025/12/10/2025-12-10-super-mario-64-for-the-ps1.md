# Super Mario 64 for the PS1

- Score: 136 | [HN](https://news.ycombinator.com/item?id=46221925) | Link: https://github.com/malucard/sm64-psx

## TL;DR
This project ports the fully decompiled Super Mario 64 engine to run natively on the original PlayStation, replacing N64 hardware features with PS1-friendly techniques: fixed‑point math, custom soft‑float, JIT‑compiled display lists, 4bpp texture quantization, compressed animations in VRAM, and DualShock rumble support. It’s still highly experimental, with major bugs, missing menus, and audio/camera issues. HN discussion focuses on texture warping, tessellation limits on PS1, and how this fits into a broader wave of fan-made ports.

## Comment pulse
- Porting SM64 to old hardware is booming → commenters cite GBA Rust reimplementation, Dreamcast SM64, plus Star Fox 64 and Mario Kart 64 ports.  
- Visual quality concerns → affine texture warping persists; tessellation currently limited and lacks preprocessing, so large polygons and stretched textures remain obvious.  
- Curiosity about implementation details → questions on missing source for GBA clone and whether PS1 port uses soft floats to avoid classic wobbling geometry.  

## LLM perspective
- View: Decompilation-plus-ports is turning classic console games into semi-portable codebases targeting wildly different 90s architectures.  
- Impact: Expect more “impossible” demakes as enthusiasts combine modern tooling with deep hardware knowledge across many retro consoles.  
- Watch next: Needed advances: better automatic tessellation/texture tools for affine GPUs, legal-friendly audio asset pipelines, and reproducible performance benchmarks on real hardware.
