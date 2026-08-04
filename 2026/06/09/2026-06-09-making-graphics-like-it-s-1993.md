# Making Graphics Like it's 1993

- Score: 746 | [HN](https://news.ycombinator.com/item?id=48459294) | Link: https://staniks.github.io/articles/catlantean-3d-blog-1/

### TL;DR

Catlantean 3D is a solo-built first-person shooter constrained to a 320×240, 256-color, early-1990s-style software renderer. Its creator details a 32-level palette colormap for constant-time distance shading, Oklab-based quantization, fixed-point game logic, Blender-to-sprite automation, hand-drawn pixel art, procedural texture and gib generation, and a custom wxPython map editor. The goal is a polished 2027 release, not a tech demo. HN praised its cohesive art and unusually rich internal tooling, then exchanged implementation tips and historical distinctions among Wolfenstein, Doom, and Build.

### Comment pulse

- Its technical lineage needs precision → perpendicular walls and fixed-height floors resemble Wolfenstein-era raycasting; Doom used BSP maps, while Build used portals.
- Simple lighting can remain dynamic → 8×8 or 16×16 light maps, updated around 15 times per second, support moving illumination cheaply.
- Modern access stays minimal → commenters showed SDL2 texture and SDL3 window-surface paths for presenting a software framebuffer across platforms.

### LLM perspective

- **View:** The authentic aesthetic comes less from low resolution than from coherent palette, pixel scale, lighting, and asset-generation rules.
- **Impact:** Solo developers can trade runtime complexity for offline preprocessing, keeping rendering simple while making iteration repeatable.
- **Watch next:** Q1 2027 will test whether the custom editor and generated-asset pipeline scale from prototype to a complete game.
