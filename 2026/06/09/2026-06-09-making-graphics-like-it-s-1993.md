# Making Graphics Like it's 1993

- Score: 746 | [HN](https://news.ycombinator.com/item?id=48459294) | Link: https://staniks.github.io/articles/catlantean-3d-blog-1/

### TL;DR
A solo developer is building Catlantean 3D, a fully software‑rendered FPS constrained to early‑90s tech: 320×240 resolution, 256‑color palette, handmade rendering and audio, fixed‑point game logic, and no third‑party engines. He designs a custom palette and precomputed colormap using Oklab and hue‑shifting for depth‑cue lighting, then builds three asset pipelines: Blender‑rendered sprites quantized to the palette, strictly scaled hand‑drawn pixel art, and Python‑generated textures, gibs, and particles. A custom wxPython map editor completes the toolchain. HN comments add engine history, fixed‑point and lighting tricks, SDL software‑rendering tips, and nostalgia for 90s graphics craft.

---

### Comment pulse
- Software rendering remains approachable → commenters share minimal SDL2/SDL3 code paths for pushing memory framebuffers, plus micro‑optimizations and notes on preserving classic software renderers in modern ports.  
- Engine lineage clarification → users contrast this raycaster with Wolf3D, Doom BSP, and Build’s portal system, discussing textured floors, room‑over‑room hacks, and perspective shortcuts.  
- Old‑school tricks still useful → people describe 8×8 lightmaps, baked dynamic lighting, and fixed‑point math as performant, underused techniques; others praise the author’s integrated tooling and art direction.  

---

### LLM perspective
- View: Extreme self‑imposed constraints plus robust tooling yield coherence and personality that many asset‑driven indie games lack.  
- Impact: Inspires solo devs to invest in pipelines, editors, and deterministic tech instead of leaning on heavyweight engines for small projects.  
- Watch next: How the engine performs on low‑end hardware, license choices for the released source, and whether community map/mod ecosystems emerge.
