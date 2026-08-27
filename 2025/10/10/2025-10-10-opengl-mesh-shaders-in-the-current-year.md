# OpenGL: Mesh shaders in the current year

- Score: 115 | [HN](https://news.ycombinator.com/item?id=45537890) | Link: https://www.supergoodcode.com/mesh-shaders-in-the-current-year/

### TL;DR

The OpenGL/ES Working Group approved `GL_EXT_mesh_shader`, described by the author as OpenGL's largest extension this decade. AMD led the specification, Mesa implementation, and optional conformance tests; Zink and RadeonSI support were being prepared, with Minecraft's Nvidium mod expected to adopt the vendor-neutral extension. HN discussion explained mesh shaders as a more explicit, packet-oriented replacement for parts of the vertex and geometry pipeline, enabling custom mesh processing and line generation. Commenters expected modest gains for conventional rendering but cleaner control for specialized workloads.

### Comment pulse

- Mesh shaders expose modern GPU organization → offline meshlets and programmable workgroups reduce reliance on fixed vertex-processing machinery.
- Traditional scenes may gain little → the feature primarily improves flexibility and elegance rather than guaranteeing broad speedups.
- Minecraft helped motivate portability → Nvidium already uses NVIDIA's proprietary version and could reach other vendors through EXT.

### LLM perspective

- View: The extension keeps OpenGL relevant by standardizing a capability already proven through vendor-specific experimentation.
- Impact: Engine and mod developers gain a cross-vendor path to GPU-driven geometry without immediately migrating APIs.
- Watch next: Track RadeonSI, Zink, NVIDIA, conformance, Minecraft adoption, tooling, and performance across realistic mesh workloads.
