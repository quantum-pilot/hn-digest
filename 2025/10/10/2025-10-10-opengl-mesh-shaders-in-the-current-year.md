# OpenGL: Mesh shaders in the current year

- Score: 115 | [HN](https://news.ycombinator.com/item?id=45537890) | Link: https://www.supergoodcode.com/mesh-shaders-in-the-current-year/

- TL;DR
    - Khronos approved GL_EXT_mesh_shader, bringing mesh/task shaders to OpenGL. AMD led spec and Mesa work (Qiang Yu; CTS by Shihao Wang). Mesa groundwork exists; Zink enablement is queued, with RadeonSI likely to advertise first. The nvidium Minecraft mod, previously tied to NVIDIA’s GL_NV_mesh_shader, helped push cross-vendor support. HN explains mesh shaders as a vertex/geometry replacement enabling meshlets, culling, and fewer draw calls; gains vary by workload. Discussion also covers line rendering via mesh shaders/instancing and requests NV_shader_buffer_load-style buffer addresses.

- Comment pulse
    - Mesh shaders modernize GL and cut CPU overhead → meshlets enable culling/compaction and fewer draws; replace geometry/hull. — counterpoint: simple triangle workloads see modest gains.
    - Line rendering via mesh shaders is viable → output lines directly or extrude quads; alternatives include instancing and VK_EXT_line_rasterization on Vulkan.
    - Add NV_shader_buffer_load-like features next → pointer-style buffer access simplifies vertex fetch and scene-wide draws without binds; SSBOs approximate but lack raw device addresses.

- LLM perspective
    - View: OpenGL gains a modern pipeline path, delaying mandatory Vulkan rewrites for engines and mods still tied to GL.
    - Impact: Driver teams and Mesa downstreams ship support; Minecraft modders get vendor-neutral mesh shaders; Zink extends mesh shaders over Vulkan.
    - Watch next: RadeonSI enabling first, Zink MR merge timing, CTS coverage, perf comparisons on complex scenes, and any Buffer Device Address-style extension.
