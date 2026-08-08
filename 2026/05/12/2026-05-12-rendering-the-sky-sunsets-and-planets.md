# Rendering the Sky, Sunsets, and Planets

- Score: 392 | [HN](https://news.ycombinator.com/item?id=48107997) | Link: https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/

### TL;DR

Maxime Heckel builds a browser shader from first principles: raymarch atmospheric density, apply Beer’s Law plus Rayleigh, Mie, and ozone terms, then light-march toward the Sun to produce day, sunset, and sunrise colors. Depth reconstruction turns the flat sky into scene-aware fog; ray-sphere intersections and logarithmic depth extend it to planetary shells, eclipses, and Mars-like presets. A partial LUT implementation precomputes costly transmittance and sky data. HN praised the interactive pedagogy and browser performance, while noting the demo unrealistically turns black immediately after sunset instead of showing twilight.

### Comment pulse

- Graphics enthusiasts valued calm, technically deep explanations and shared related planet, cloud, and classic 1993 scattering implementations.
- Browser and mobile capability impressed readers; compact equations can upgrade a static skybox into a full day-night cycle.
- The sunset model lacks atmospheric twilight — counterpoint: physically tracing post-sunset sunlight may be impractical, while common approximations can cover 18°.

### LLM perspective

- View: The tutorial’s strongest abstraction is separating physical ingredients, scene integration, and caching, letting readers trade accuracy against real-time cost.
- Impact: Web developers can add physically grounded skies, fog, planetary atmospheres, eclipses, and alien presets without moving beyond browser shaders.
- Watch next: Complete Hillaire’s 3D aerial-perspective and multi-scattering LUTs, test WebGPU compute paths, and model twilight and occlusion more accurately.
