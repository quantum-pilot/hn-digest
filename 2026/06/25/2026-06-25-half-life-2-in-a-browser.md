# Half-Life 2 in a Browser

- Score: 632 | [HN](https://news.ycombinator.com/item?id=48669534) | Link: https://hl2.slqnt.dev/

### TL;DR

A hobbyist made Half-Life 2 playable in-browser by adapting an open-source Portal web port and a modified Source engine, translating OpenGL ES through Emscripten to WebGL2. The work required legacy game assets, per-map data bundles, IDBFS saves, disabled facial morphing, and fixes for weapons, NPCs, damage, lighting, water, and controls; Episodes One and Two are planned. HN celebrated browser preservation and macOS accessibility, listed similar ports, and debated whether installation-free delivery outweighs WebAssembly/WebGL limits, large downloads, weak engine support, hosting load, and missing storefront economics.

### Comment pulse

- Browsers extend software life → the port runs on modern macOS where Steam’s 32-bit build does not, and peers shared many older games.
- Web deployment reduces installation friction → users imagined games downloading assets into local storage — counterpoint: large downloads weaken the advantage.
- Tooling still blocks wider adoption → Unreal and C# Godot lack exports, WebGL is limited, WebGPU support remains uneven, and Steam supplies monetization.

### LLM perspective

- **View:** The project is more compelling as preservation and portability infrastructure than as a blueprint for contemporary blockbuster distribution.
- **Impact:** Older games can reach unsupported platforms instantly, while maintainers inherit browser storage, compatibility, and bandwidth problems.
- **Watch next:** Test complete-game stability, asset caching, controller support, WebGPU migration, hosting resilience, and progress on both episodes.
