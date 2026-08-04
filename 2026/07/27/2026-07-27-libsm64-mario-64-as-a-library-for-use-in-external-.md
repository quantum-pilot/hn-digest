# Libsm64: Mario 64 as a library for use in external game engines

- Score: 177 | [HN](https://news.ycombinator.com/item?id=49067352) | Link: https://github.com/libsm64/libsm64

### TL;DR

libsm64 packages reverse-engineered Super Mario 64 movement and rendering code as a shared library, letting external engines embed Mario through one public header. It extracts textures and animations at runtime from a user-supplied official US ROM rather than distributing those assets. Bindings and plugins cover Rust, Odin, C#, Unity, Godot, Blender, GameMaker, and mod loaders, with desktop builds and experimental WebAssembly support. Hacker News celebrated ambitious integrations while noting that the library simplifies engineering rather than making cross-game characters plug-and-play for non-programmers.

### Comment pulse

- Compatibility is deeper than a skin → Mario’s original physics, collisions, swimming, hitbox, and damage logic continue running inside host games.
- Interoperability need not require a metaverse platform → commenters saw composable mods delivering the cross-world promise without crypto, VR mandates, or centralized ownership.
- Examples drive the appeal → favorites included Blender integration, Portal-style challenges, and a Quest 3 sandbox where Mario jumps on drawn platforms.

### LLM perspective

- **View:** The project demonstrates that portable behavior can matter more than portable assets when moving a character between worlds.
- **Impact:** Cross-engine bindings lower the cost of experimental mechanics, educational demos, and mixed-reality prototypes.
- **Watch next:** Track WebAssembly maturity, setup tooling, plugin maintenance, and host-specific fixes for rails, portals, and mixed control schemes.
