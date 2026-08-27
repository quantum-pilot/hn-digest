# Apple releases open-source model that instantly turns 2D photos into 3D views

- Score: 357 | [HN](https://news.ycombinator.com/item?id=46401539) | Link: https://github.com/apple/ml-sharp

### TL;DR

Apple’s SHARP turns a single photograph into a metric 3D Gaussian-splat scene in under a second on a standard GPU, then renders nearby photorealistic views in real time. The released Python tooling supports CPU, CUDA, and Apple MPS for prediction, though trajectory rendering still requires CUDA. Apple reports 25–34% lower LPIPS, 21–43% lower DISTS, and roughly 1,000-fold faster synthesis than prior models. HN readers liked the demos but disputed “open source”: model weights are licensed for research only.

### Comment pulse

- Licensing concern → code and model licenses differ, making the submission’s “open-source” label misleading.
- Practical limits → 768-pixel, narrow-baseline output and rendering constraints temper excitement despite unusually fast inference.

### LLM perspective

- View: Speed, not unrestricted reuse, is SHARP’s clearest advance for monocular view synthesis.
- Impact: Researchers gain rapid 3DGS prototyping; commercial developers must find differently licensed models.
- Watch next: Independent benchmarks should test geometry, scale, artifacts, and MPS rendering beyond curated examples.
