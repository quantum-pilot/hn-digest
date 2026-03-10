# Building a Procedural Hex Map with Wave Function Collapse

- Score: 358 | [HN](https://news.ycombinator.com/item?id=47311815) | Link: https://felixturner.github.io/hex-map-wfc/article/

## TL;DR
A developer builds a procedural medieval island generator using Wave Function Collapse (WFC) on a 4,100‑hex map, tackling the harder hex case with elevation, roads, rivers, and coastlines. They stabilize WFC by splitting the world into 19 sub‑grids, adding layered recovery (backtracking, local re‑solves, and “mountain patching”), and offloading work to Web Workers. Visual polish comes from WebGPU, batched instancing, clever water shaders, and post‑processing, while trees and buildings use noise-based placement instead of WFC for large‑scale structure. Hacker News discusses constraint solvers, performance, and optimization tricks.

## Comment pulse
- Use real constraint programming → Algorithm X or MiniZinc could give better success rates than ad‑hoc backtracking—counterpoint: heavier tooling complicates a web demo.
- Performance mixed → some see 5 FPS and prefer noise-based worldgen with separate river/road passes for more natural, global structure.
- Optimize WFC state → bitfields/bitsets for tile superpositions can make recomputation faster than complex backtracking on large chunks.

## LLM perspective
- View: This is a showcase of combining local constraint solving with global noise to balance structure and organic variation.
- Impact: Useful reference for indie gamedevs and technical artists building tile-based maps with modern web graphics.
- Watch next: Benchmarks comparing WFC vs constraint solvers, plus experiments mixing WFC with noise-driven macro layouts.
