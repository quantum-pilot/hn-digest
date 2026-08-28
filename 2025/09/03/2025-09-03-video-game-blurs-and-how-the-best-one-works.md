# Video Game Blurs (and how the best one works)

- Score: 277 | [HN](https://news.ycombinator.com/item?id=45114498) | Link: https://blog.frost.kiwi/dual-kawase/

### TL;DR

This interactive WebGL tutorial develops real-time blur from first principles, beginning with box and Gaussian kernels and previewing Dual Kawase blur. It explains texture taps, UV coordinates, kernel normalization, edge handling, sampling distance, and the artifacts created when sparse samples cover too much image area. Performance is central: naive large kernels can quickly overwhelm GPUs. However, the captured article truncates during its Gaussian section, so the promised Dual Kawase implementation is represented only by the introduction and subsequent comment discussion.

### Comment pulse

- Readers praised the interactive comparisons; one noted that small-radius Gaussian kernels need integrated rather than point-sampled weights.
- Discussion contrasted Kawase with more natural bokeh and explored compute-shader variants that keep intermediate data in shared memory.

### LLM perspective

- View: The tutorial’s real contribution is connecting visual artifacts directly to sampling and memory costs.
- Impact: Interactive side-by-side tests make graphics tradeoffs legible to readers without prior shader experience.
- Watch next: Compute-shader approaches that preserve Kawase efficiency while avoiding off-chip intermediate writes.
