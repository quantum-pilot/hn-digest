# Software rendering in 500 lines of bare C++

- Score: 234 | [HN](https://news.ycombinator.com/item?id=49022038) | Link: https://haqr.eu/tinyrenderer/

### TL;DR
A compact C++ “tinyrenderer” walks from setting single pixels to a full software 3D renderer in ~500 lines, with no graphics libraries beyond a TGA helper. The goal is not performance but demystifying what OpenGL/Vulkan/DirectX actually do: line drawing, triangle rasterization, cameras, z-buffering, textures, shading, tangent space, shadows, and SSAO. Students typically reach competent renderers in 10–20 hours, gaining intuition for the graphics pipeline and how GPU APIs map onto simple CPU-side concepts.

---

### Comment pulse
- Hands-on rewrites (e.g., in Rust) show a single-threaded CPU renderer can drive small interactive 3D games with post-effects—counterpoint: GPUs still win for large scenes.
- Many pair this tutorial with foundational texts (Vince, Foley/van Dam) to understand the math and linear algebra behind transformations and projection.
- Triangle clipping is a recurring pain point; commenters discuss frustum clipping, Sutherland–Hodgman in clip space, attribute interpolation, and more advanced “primitive synthesis” approaches.

---

### LLM perspective
- View: Tiny software renderers are still among the clearest ways to internalize the real graphics pipeline behind high-level APIs.
- Impact: Especially valuable for engine programmers, tool developers, and students who treat OpenGL/Vulkan as opaque “draw” or “shader” boxes.
- Watch next: Extend tutorials with explicit clipping, profiling, cache/SIMD discussions, and comparisons against small GPU-based equivalents.
