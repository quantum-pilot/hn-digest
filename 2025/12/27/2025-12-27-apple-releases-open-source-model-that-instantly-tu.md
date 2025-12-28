# Apple releases open-source model that instantly turns 2D photos into 3D views

- Score: 357 | [HN](https://news.ycombinator.com/item?id=46401539) | Link: https://github.com/apple/ml-sharp

### TL;DR
Apple’s SHARP model takes a single 2D photo and predicts a full 3D Gaussian-splat representation that can be rendered from new viewpoints in real time. It dramatically outperforms prior monocular view-synthesis systems on perceptual quality metrics while being roughly three orders of magnitude faster, and ships with a simple CLI and pretrained checkpoint. Hacker News discussion centers on setup friction, Apple’s “research only” license for the weights, more compelling third‑party demos, and speculative porn/VR applications.

---

### Comment pulse
- Tooling friction → Many AI GitHub repos, including this, assume CUDA/MPS and ML tooling already configured; one fork adds working MPS-based rendering for Macs.  
- Licensing confusion → Code license looks permissive, but the model file is explicitly “research only”; commenters debate Meta’s influence on “open source” semantics and weights’ copyrightability.  
- Use cases vs reality → Jokes about VR porn dominance meet technical pushback: limited motion, 768‑pixel cap, single-axis parallax, and artifacts mean speed gains don’t transform that niche.

---

### LLM perspective
- View → Fast monocular 3D from a single frame is a key building block for AR, robotics, and interactive media pipelines.  
- Impact → Individual developers can experiment with near-SOTA view synthesis locally; serious commercial products are constrained by the noncommercial model license.  
- Watch next → Track permissively-licensed replications, mobile/embedded ports, and benchmarks on occlusion handling, large camera moves, and integration into live AR/VR engines.
