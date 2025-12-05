# Multivox: Volumetric Display

- Score: 204 | [HN](https://news.ycombinator.com/item?id=46149813) | Link: https://github.com/AncientJames/multivox

- TL;DR  
Multivox is open-source software for driving home‑built volumetric “orb” displays made from spinning HUB75 LED panels and a Raspberry Pi 4. It abstracts hardware into a voxel buffer shared between a real-time driver and game-like “toys” (plus an OpenGL simulator for non-owners). Hacker News discussion highlights physical limits of volumetric imagery (no backface culling, best for cutaways), contrasts spinning orbs with glass‑etched and touchable projector-based volumes, and imagines uses like 3D radar for space sims.

- Comment pulse  
  - Volumetric orbs lack backface culling → every surface visible from all sides, so cutaways and sparse scenes read best—counterpoint: parallax still feels ‘magical’ to viewers.  
  - Other volumetric approaches exist → same maker built static glass-etched voxels lit by a projector and a rubber-band-suspended, touchable projection volume.  
  - Community admires the creator’s broader portfolio → from LEGO-sized Doom consoles to fiber displays, but notes glass-etched volumes are difficult for hobbyists to fabricate.

- LLM perspective  
  - View: Treat Multivox as a reference architecture for spinning volumetric displays—hardware assumptions, voxel API, and simulator are reusable patterns.  
  - Impact: Hobbyists, artists, and researchers get a concrete platform for 3D UI experiments, spatial games, and novel data visualizations.  
  - Watch next: standardized content formats, multi-orb synchronization, and studies on which volumetric scenes remain legible under rotation and occlusion limits.
