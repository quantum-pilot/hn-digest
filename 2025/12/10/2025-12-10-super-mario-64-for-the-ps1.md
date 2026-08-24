# Super Mario 64 for the PS1

- Score: 136 | [HN](https://news.ycombinator.com/item?id=46221925) | Link: https://github.com/malucard/sm64-psx

### TL;DR

A work-in-progress port adapts the decompiled Nintendo 64 game for original PlayStation hardware and PC debugging. It replaces much floating-point math, rewrites rendering, compresses animations into VRAM, quantizes textures, adds DualShock rumble and uses display-list preprocessing to fit the target. Only US assets build today, and an original ROM is required. HN readers admired the engineering but observed severe affine texture warping; the repository also lists crashes, missing camera control, broken animations, stutters, audio gaps and unfinished menus.

### Comment pulse

- Texture artifacts dominate reactions → 2× tessellation cannot yet tame large polygons or limited per-polygon coordinates.
- Decompilations enable unlikely ports → commenters compared GBA, Dreamcast and other cross-platform recreations.
- Proof matters visually → readers requested gameplay footage because the README alone cannot show practical progress.

### LLM perspective

- View: Hardware constraints are driving inventive, visible design tradeoffs.
- Impact: Preservation developers gain another testbed for decompilation-based portability.
- Watch next: Stable levels, camera completion and better geometry preprocessing.
