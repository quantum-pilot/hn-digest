# I put a real-time 3D shader on the Game Boy Color

- Score: 231 | [HN](https://news.ycombinator.com/item?id=46935791) | Link: https://blog.otterstack.com/posts/202512-gbshader/

- TL;DR  
On a Game Boy Color, Danny Spencer renders animated normal-mapped sprites with real-time Lambert lighting, controlled by an orbiting light source. Because the SM83 CPU lacks multiplication and floats, he encodes per-pixel spherical normal data into 8‑bit fractions, replaces multiplies with log/exp lookup tables (including a cos_log table), and even uses self-modifying code to shave cycles. About 89% of each frame is spent shading tiles. He documents limited, carefully disclosed use of AI tools, which failed at performance-critical assembly.

- Comment pulse  
  - It’s “3D” via prerendered normal-map frames plus real-time lighting → mirrors modern deferred rendering and imposters; shaders care about vectors, not how buffers were produced.  
  - People love seeing low-level, cycle-counted hacking → feels refreshingly non-AI-driven—counterpoint: some still wish the author were more enthusiastic about AI.  
  - Readers praise detailed AI-use disclosure → aligns with growing concern over hidden AI assistance and reinforces trust in craftsmanship under tight hardware limits.

- LLM perspective  
  - View: Great example of treating LLMs as junior helpers for boilerplate, not architects of performance-critical low-level systems.  
  - Impact: Inspires retro-console developers, shader hackers, and educators showing numeric methods under extreme constraints.  
  - Watch next: Environment-map experiments on GB, shared benchmarks vs naive approaches, and small tools to auto-generate log/lookup tables for 8‑bit targets.
