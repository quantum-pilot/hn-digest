# Apple Releases Open Weights Video Model

- Score: 424 | [HN](https://news.ycombinator.com/item?id=46117802) | Link: https://starflow-v.github.io

### TL;DR

Apple researchers present STARFlow-V, a 7-billion-parameter causal video generator based on normalizing flows rather than diffusion. Trained on 70 million text-video and 400 million text-image pairs, it generates 480p video at 16 fps and natively supports text-to-video, image-to-video, and video-to-video tasks. The team claims its global-local architecture, flow-score denoising, and parallelizable Jacobi iteration improve consistency and sampling. Commenters disputed the “open weights” framing, citing unavailable weights and a noncommercial research license, while disagreeing over output quality.

### Comment pulse

- Research contribution → normalizing flows offer likelihood estimation and one architecture for multiple video tasks.
- Openness challenged → commenters say weights were not yet posted and the model license restricts commercial use.
- Quality divided → some saw dated artifacts; others considered results respectable for a 7B research model.

### LLM perspective

- View: The architectural alternative is more consequential than claims of immediate visual leadership.
- Impact: Researchers gain a potential diffusion alternative, but licensing and availability constrain practical adoption.
- Watch next: Verify weight publication, license terms, independent benchmarks, temporal coherence, and real sampling costs.
