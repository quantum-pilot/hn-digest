# Show HN: High-Res Neural Cellular Automata

- Score: 183 | [HN](https://news.ycombinator.com/item?id=48567877) | Link: https://cells2pixels.github.io/

- TL;DR  
This work extends neural cellular automata to real‑time, arbitrary‑resolution imagery by running the CA on a coarse grid and decoding each point’s appearance with a tiny MLP using interpolated cell states and local coordinates. That keeps updates local and GPU‑friendly while sidestepping quadratic memory/compute growth, enabling detailed 2D/3D textures and morphogenesis on meshes. HN commenters probe its fragile regeneration behavior, contrast it with texture sampling, and imagine self‑healing infrastructure and other bio‑inspired systems.

- Comment pulse  
  - Emergent regeneration exists but is brittle → model trained only to grow from a central seed, so heavy editing—especially erasing the center—causes total collapse.  
  - Toy model of morphogenesis and healing → complex patterns and repair from local rules; inspires ideas like self‑healing “Bionettes” — counterpoint: real applications remain unclear.  
  - Different from texture sampling → no global coordinate lookup; purely local rules with smaller weights than JPEG textures, but long‑range communication still needs many steps.

- LLM perspective  
  - View: Factorizing NCA state from rendering resembles neural fields, making CA‑style dynamics practical for high‑fidelity graphics.  
  - Impact: Could replace static texture maps with compact, self‑organizing materials in game engines, VFX tools, and procedural content pipelines.  
  - Watch next: Train for damage recovery, benchmark speed/quality vs tiled textures, and explore CA‑based controllers for fault‑tolerant systems.
