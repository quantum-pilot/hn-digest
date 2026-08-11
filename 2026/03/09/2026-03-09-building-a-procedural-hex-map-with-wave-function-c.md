# Building a Procedural Hex Map with Wave Function Collapse

- Score: 358 | [HN](https://news.ycombinator.com/item?id=47311815) | Link: https://felixturner.github.io/hex-map-wfc/article/

### TL;DR

Felix Turner built deterministic medieval islands from 4,100 hex cells using Wave Function Collapse across 19 separately solved grids. Each cell can begin with 900 tile, rotation, and elevation states; a layered recovery system combines delta-based backtracking, relaxed boundary constraints, local 19-cell re-solves, and mountains that hide irreparable seams. Perlin noise handles forests and villages because WFC struggles with global patterns, while Three.js WebGPU batching drives rendering. HN praised the demo but suggested industrial constraint solvers and bitfields, questioned nonlocal realism, and reported hardware far below the claimed 60 fps.

### Comment pulse

- Algorithm X or MiniZinc could improve border solving and free development time, though integrating a general solver adds modeling complexity.
- WFC excels at local compatibility — counterpoint: rivers, roads, and biomes often need global simulation or separate generative passes.
- One Iris Xe user measured 5 fps despite the 60-fps claim; platform-specific benchmarks would clarify GPU and fallback behavior.

### LLM perspective

- **View:** Hybrid generation fits the problem: constraints for seams, noise and rules for spatial structure.
- **Impact:** Game developers gain a reproducible WebGPU reference and concrete recovery techniques for chunked WFC.
- **Watch next:** Memory profiles, mobile performance, alternative solvers, global hydrology, larger grids, and independent success-rate reproduction.
