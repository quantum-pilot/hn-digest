# Phyllotaxis: An audio-reactive LED display

- Score: 309 | [HN](https://news.ycombinator.com/item?id=49880411) | Link: https://jagi.studio/posts/phyllotaxis/

### TL;DR

The author turned a golden-ratio phyllotaxis pattern into an 89-cell, audio-reactive LED sculpture. Voronoi geometry generated in Processing became CadQuery and FreeCAD parts, translucent paper diffused addressable LEDs, and an STM32 analyzed microphone input with Fourier transforms and multiband energy. A second version uses five identical interlocking PCBs, 3D-printed walls, an ESP32, Rust firmware, and a local WebAssembly sketch uploader. Assembly and fragile paper remain obstacles before a possible third, more reproducible version.

### Comment pulse

- Fivefold PCB symmetry cleverly fits manufacturing constraints → one repeated board forms the ring while minimizing unique parts.
- Fabrication assembly could remove the worst bottleneck → commenters recommended having the board vendor place the awkward surface-mount LEDs.
- Related Fibonacci displays show convergent ideas → commenters found products sharing radial LEDs or Voronoi-like presentation, without identical internals.

### LLM perspective

- View: The project’s strength is translating one mathematical structure consistently across geometry, electronics, and animation.
- Impact: Networked firmware turns a sculpture into a shared platform for sketches and games.
- Watch next: Test assembled LEDs, tougher diffusers, magnetic faceplates, licensing, and version-three repairability.
