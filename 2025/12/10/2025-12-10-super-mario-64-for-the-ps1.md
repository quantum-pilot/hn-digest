# Super Mario 64 for the PS1

- Score: 136 | [HN](https://news.ycombinator.com/item?id=46221925) | Link: https://github.com/malucard/sm64-psx

### TL;DR

A work-in-progress port adapts the decompiled Super Mario 64 codebase to PlayStation 1 hardware and PC debugging, currently building only from a user-supplied US ROM. It replaces or compresses systems around floating-point math, rendering, display lists, textures, animation storage, shadows, and DualShock rumble to fit different hardware constraints. Major gaps remain: crashes, missing animations, unfinished camera and menus, audio defects, loading stutters, and warped graphics. Commenters admired the technical effort while focusing on visible affine texture distortion, gameplay footage, and related retro ports.

### Comment pulse

- Hardware enthusiasts praised bringing an N64 landmark onto weaker, architecturally different PlayStation hardware despite obvious visual compromises.
- Developers attributed severe texture warping to insufficient tessellation and unfinished polygon preprocessing rather than a completed rendering design.
- Related GBA, Dreamcast, and decompilation ports show a broader community turning recovered game source into cross-platform engineering experiments.

### LLM perspective

- View: The port is most valuable as constraint-driven systems work, not yet as a faithful way to play.
- Impact: Contributors can study practical fixed-point, memory, and rendering tradeoffs on original-era hardware.
- Watch next: Level stability, camera completion, polygon preprocessing, texture correction, audio reliability, and footage from physical consoles.
