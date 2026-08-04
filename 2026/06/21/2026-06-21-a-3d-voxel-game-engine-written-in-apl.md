# A 3D voxel game engine written in APL

- Score: 147 | [HN](https://news.ycombinator.com/item?id=48616713) | Link: https://github.com/namgyaaal/avoxelgame

### TL;DR

An experimental voxel game uses Dyalog APL for game logic and SDL3 for graphics, testing whether array-oriented notation makes voxel development easier. It supports movement, jumping, camera control, block selection and placement, multiple GPU backends, and macOS, Linux, and Windows setup paths. The author explicitly labels it buggy: Windows performance regressed, DirectX 12 is unsupported there, repeated play can crash, and memory may leak. HN readers admired the unusual pairing and debated whether voxel grids make APL naturally suitable or merely an entertaining constraint.

### Comment pulse

- Voxel worlds suit array languages → commenters argued the domain’s multidimensional data makes APL’s notation less strange than the engine choice appears.

- The README’s candor builds trust → calling the project experimental and buggy invited technical curiosity instead of overselling an unfinished engine.

- Performance remains the unanswered test → readers requested like-for-like benchmarks against C++ or Rust implementations before judging APL’s practicality.

### LLM perspective

- **View:** The project tests where array-language expressiveness survives contact with graphics APIs, platform tooling, and mutable game state.

- **Impact:** APL learners gain a concrete systems example; engine developers gain evidence about which voxel operations benefit from array primitives.

- **Watch next:** Benchmark frame time, memory, chunk generation, meshing, and Windows backends; document which APL idioms simplified or complicated development.
