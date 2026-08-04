# Learn OpenGL, extensive tutorial resource for learning Modern OpenGL

- Score: 169 | [HN](https://news.ycombinator.com/item?id=49022634) | Link: https://learnopengl.com/

### TL;DR

LearnOpenGL is a free, step-by-step online book and PDF teaching modern core-profile OpenGL from first window and triangle through shaders, textures, cameras, lighting, model loading, framebuffers, PBR, compute shaders, and a complete 2D game. It targets beginners while remaining a reference for experienced developers, with a matching paid print edition. HN readers praised it as a durable graphics foundation despite OpenGL’s age: the rendering concepts transfer. Discussion split between starting here, building a CPU software renderer first, or choosing newer graphics APIs and abstractions.

### Comment pulse

- API age need not block learning → commenters valued OpenGL’s clear mapping from pipeline concepts to hardware before confronting lower-level driver complexity.
- First-principles advocates prefer CPU rendering → manually implementing projection, rasterization, model loading, and skeletal animation can reveal which later pipeline stages become programmable.
- Modern API recommendations varied → WebGPU, SDL-GPU, Sokol, and Metal promise nicer interfaces — counterpoint: Vulkan and DX12 experience still matters professionally.

### LLM perspective

- **View:** The resource succeeds by sequencing visible results with theory, preserving motivation while steadily exposing the programmable rendering pipeline.
- **Impact:** Learners gain concepts applicable beyond OpenGL; hobbyists get a bounded path from blank window to complete interactive project.
- **Watch next:** Pair chapters with experiments, then port one renderer to a modern API to test transfer and platform constraints.
