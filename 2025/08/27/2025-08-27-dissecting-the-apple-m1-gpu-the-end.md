# Dissecting the Apple M1 GPU, the end

- Score: 845 | [HN](https://news.ycombinator.com/item?id=45034537) | Link: https://rosenzweig.io/blog/asahi-gpu-part-n.html

- TL;DR
    - Alyssa Rosenzweig recounts reverse‑engineering Apple’s M1/M2 GPU for Asahi Linux from first triangle to upstream, conformant OpenGL 4.6, Vulkan 1.4, and OpenCL 3.0. She built geometry/tessellation emulation to support Direct3D via Proton, enabling AAA gaming and sparse textures, and helped dispel the “Vulkan can’t run on Apple” myth—now informing LunarG’s KosmicKrisp for macOS. With drivers upstream and Linux on Apple Silicon broadly working, she’s stepping away, reportedly to Intel Xe‑HPG. HN praises the achievement and notes virtio‑GPU/venus benefits for Apple virtualization.

- Comment pulse
    - Open drivers on M1 unlock gaming and VMs → Proton with D3D 12, and virtio‑GPU/venus help guests since Apple VZ blocks GPU passthrough.
    - Career move speculated → blog links Xe‑HPG; commenters cite her resume showing she joined Intel’s open‑source graphics team this month.
    - Impact lauded → community hails rare focus and output from student-to-pro; inspires others—counterpoint: attributes include compensation, lifestyle tradeoffs, and “10x engineer” framing.

- LLM perspective
    - View: This caps a flagship reverse‑engineering effort and validates Mesa’s approach on unconventional GPUs.
    - Impact: Mesa now has reusable geometry/tessellation emulation, benefiting other GPUs lacking legacy features and improving D3D-on-Vulkan paths.
    - Watch next: Intel Xe‑HPG contributions; KosmicKrisp’s Vulkan-on-macOS maturity; sustained performance/feature parity across Apple Silicon generations.
