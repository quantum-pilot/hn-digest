# Making Minecraft Spherical

- Score: 900 | [HN](https://news.ycombinator.com/item?id=45055205) | Link: https://www.bowerbyte.com/posts/blocky-planet/

TL;DR
Unity tech demo maps Minecraft‑style voxels to a spherical, destructible planet. Surface uses a quad‑sphere with pre‑distortion to reduce skew; depth uses expanding “shells” to preserve block height and edge alignment; storage is uniform 16³ chunks; neighbor lookup handles sector flips and multi‑to‑one vertical mappings; terrain samples 3D noise; gravity points to the center with a thruster. HN compares with Space Engineers/Eco, proposes torus or slerp‑based alternatives, and debates limiting dig depth versus letting players reach the zero‑g core.

Comment pulse
- Use slerp to subdivide cube faces → keeps quad sizes more uniform than lerp+normalize — counterpoint: OP pre-distorts grids to similar effect.
- Limit digging depth → avoids tiny blocks and odd gravity near core; simpler neighbor logic — counterpoint: players want to reach zero‑g cores.
- Torus/torisphere worlds or fixed-point gravity (Eco, Space Engineers) → sidestep spherical tiling/build‑up issues, at realism/gameplay tradeoffs.

LLM perspective
- View: Quad‑sphere plus shelling is a pragmatic compromise; hardest parts are neighbor addressing and distortion at sector and shell seams.
- Impact: Techniques generalize to curved‑world sandboxes, modded Minecraft clones, and engines needing chunk‑agnostic batch processing on non‑Euclidean grids.
- Watch next: Publish code and metrics; compare slerp vs pre‑distortion; implement caves, voxel lighting, and multi‑body gravity/collisions with stability/perf benchmarks.
