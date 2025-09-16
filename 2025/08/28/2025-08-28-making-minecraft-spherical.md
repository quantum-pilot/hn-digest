# Making Minecraft Spherical

- Score: 900 | [HN](https://news.ycombinator.com/item?id=45055205) | Link: https://www.bowerbyte.com/posts/blocky-planet/

- TL;DR
  - A Unity tech demo maps Minecraft-like voxels onto a sphere using a quad-sphere with pre‑distortion, multi-shell depth scaling, and 16³ chunks. It tackles tricky neighbor lookups across sector/shell boundaries, custom center‑seeking gravity, 3D noise terrain, and structure placement via relative directions; future ideas include multiple planets and voxel lighting. HN discusses alternatives—torus/torisphere worlds, fixed‑point gravity à la Space Engineers, or simply capping dig depth—and mapping tips like slerp subdivision; one commenter corrects that WGS84 is a reference frame, not a projection.

- Comment pulse
  - Limit digging near core → fewer squashed blocks and saner gravity — counterpoint: players want to reach zero‑g center and build there.
  - Use quad-sphere with slerp subdivision → preserves area/angles better than lerp normalization; avoids polar seams. Note: WGS84 is a reference frame, not projection.
  - Alternative topologies → torus/torisphere worlds give perfect grids and seamless noise; fixed-point gravity plus no voxel-building (Space Engineers) sidesteps many issues.

- LLM perspective
  - View: The smart bits are pre-distorted quad-sphere, shell-based scaling, and robust neighbor addressing across sector/shell boundaries.
  - Impact: Enables tiny, destructible planets with walkable surfaces, chunking performance, and consistent building—opening paths to multi-planet sandbox or KSP-like gameplay.
  - Watch next: Benchmarks of lerp vs slerp mapping, shell depth limits, neighbor edge-case coverage; release a minimal code sample/library.
