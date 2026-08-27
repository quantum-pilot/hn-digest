# Simulating a Planet on the GPU: Part 1 (2022)

- Score: 112 | [HN](https://news.ycombinator.com/item?id=45897122) | Link: https://www.patrickcelentano.com/blog/planet-sim-part-1

### TL;DR

Seeking a modern successor to SimEarth, the author spent more than a year building a planetary simulation in Unity. Polygonal Voronoi plates proved too expensive and insufficient for realistic deformation, while a cubemap compute-shader version handled collision, subduction, and seafloor spreading but still could not deform crust. Smoothed-particle hydrodynamics then offered a particle-based foundation for crust, air, and water. The project’s practical lesson was that GPU arithmetic is cheap while memory access, debugging, and profiling dominate difficulty.

### Comment pulse

- Shader programmers praised the parallel, per-pixel mental model but agreed failures remain frustrating to debug.
- Readers admired the ambition while noting the promised second installment apparently never arrived.

### LLM perspective

- View: Changing representation, not merely optimizing code, unlocked each major step in the simulation.
- Impact: GPU-friendly particles make deeper planetary systems plausible for individual developers, though scientific fidelity remains expensive.
- Watch next: Validation of plate behavior, adaptive resolution, atmosphere coupling, and performance beyond one laptop would establish progress.
