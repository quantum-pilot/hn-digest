# Shaders: How to draw high fidelity graphics with just x and y coordinates

- Score: 319 | [HN](https://news.ycombinator.com/item?id=46023013) | Link: https://www.makingsoftware.com/chapters/shaders

### TL;DR

This visual tutorial explains how GPUs trade single-task latency for massive throughput and how vertex shaders, rasterization, and fragment shaders turn geometry into pixels. It walks through coordinate transforms, varyings, depth, anti-aliasing, gradients, and Phong ambient, diffuse, and specular lighting, then surveys GLSL, HLSL, Metal, Vulkan, WebGPU, compute shaders, and CUDA. Commenters praised the presentation and suggested playgrounds, but corrected platform diagrams and stressed SIMT execution, native WebGPU libraries, shader use beyond rasterization, and the difficult cross-platform debugging experience.

### Comment pulse

- Teaching strength → interactive diagrams make transforms, interpolation, normals, and per-fragment lighting approachable to newcomers.
- Technical correction → shaders are callbacks that may run beyond GPUs or rasterization, while neighboring GPU threads commonly share instructions.
- Tooling burden → APIs, data movement, backend differences, synchronization, and weak debuggers complicate the elegant per-element model.

### LLM perspective

- View: The tutorial succeeds as an intuition builder, though its simplifying platform map should not become an implementation reference.
- Impact: Beginners gain enough pipeline context to experiment while recognizing that frameworks hide substantial portability work.
- Watch next: Correct API diagrams, add SIMT divergence, profile CPU-GPU transfers, and compare WebGPU’s native implementations.
