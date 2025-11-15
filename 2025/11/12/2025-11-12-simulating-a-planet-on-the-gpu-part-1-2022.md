# Simulating a Planet on the GPU: Part 1 (2022)

- Score: 112 | [HN](https://news.ycombinator.com/item?id=45897122) | Link: https://www.patrickcelentano.com/blog/planet-sim-part-1

- TL;DR
    - An indie dev chases a modern SimEarth: polygonal Voronoi/Delaunay worlds in Unity couldn’t handle realistic plate collisions; a custom C++/Vulkan engine was too heavy. He moved to GPU compute shaders with cubemaps, achieving plate motion/subduction/spreading but lacking deformation. Inspired by sand demos, he implemented SPH on a sphere via compute shaders, learning GPU debugging is hard and memory dominates performance. Next: visualize currents/winds, moisture/precipitation, volcanoes, and optimize for broader hardware. HN discusses shader ergonomics, GPU capacity intuition, tectonics.js, and the absence of Part 2.

- Comment pulse
    - Shaders are fun, immediate feedback → per-pixel mental model; debugging compute/pixel shaders is painful — counterpoint: HIP allows kernel breakpoints and printf on GPU.
    - How much can a GPU move? → Memory bandwidth and interactions dominate; simple advection scales to billions, collisions drop throughput dramatically.
    - Pointers to prior art → tectonics.js offers deep plate-simulation write-ups; commenters note the blog’s Part 2 never arrived.

- LLM perspective
    - View: Switching to SPH-on-sphere with compute shaders trades mesh complexity for particle locality, enabling crust deformation within GPU-friendly kernels.
    - Impact: Requires efficient neighbor search, SoA memory, and tiling; plate-scale sims become feasible on consumer GPUs, broadening research and hobbyist tooling.
    - Watch next: Publish kernels and perf baselines; prototype in WebGPU; compare SPH with MPM/FLIP for solid-fluid coupling and stable mountain-building.
