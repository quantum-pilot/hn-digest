# Libsm64: Mario 64 as a library for use in external game engines

- Score: 177 | [HN](https://news.ycombinator.com/item?id=49067352) | Link: https://github.com/libsm64/libsm64

### TL;DR
Libsm64 turns Super Mario 64’s reverse‑engineered movement and rendering code into a shared library with a clean C API, so developers can drop “real” Mario 64 physics and animations into other engines. It loads assets from a user-supplied ROM at runtime, avoiding bundling copyrighted content. The Hacker News discussion focuses on wild crossovers this enables, how it’s a “metaverse without crypto,” the remaining barrier for non‑programmers, and the ever-present specter of Nintendo’s legal team.

---

### Comment pulse
- Mario actually runs invisibly in the background → libsm64 forwards positions and collisions into the host game, enabling authentic physics in Half‑Life 2, Rocket League, Sonic, Minecraft.
- Feels like the metaverse done right → interoperable characters via open tech, not crypto/platform lock‑in — counterpoint: still requires custom mods, so regular gamers must wait.
- People want demos and projects → playlists, Blender addon, AR sandbox on Quest 3 where you draw platforms in your room and Mario traverses real furniture.

---

### LLM perspective
- View: This is a reusable, battle-tested 3D character controller packaged as a drop-in module, not just a nostalgia hack.
- Impact: Lowers the cost for hobbyists and indies to prototype platformers or mashups with instantly satisfying movement.
- Watch next: Similar libraries for other classics, standardized “character APIs,” and whether rights holders tolerate or formalize such reuse.
