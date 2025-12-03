# Apple Releases Open Weights Video Model

- Score: 424 | [HN](https://news.ycombinator.com/item?id=46117802) | Link: https://starflow-v.github.io

### TL;DR
Apple’s STARFlow‑V is a 7B‑parameter, normalizing‑flow–based causal video generator trained on 70M text‑video and 400M text‑image pairs. Unlike diffusion, it offers end‑to‑end likelihood training, exact probability estimation, and a single invertible model for text‑to‑video, image‑to‑video, and video‑to‑video tasks. A global‑local latent architecture plus a lightweight causal denoiser and parallelizable Jacobi sampling aim to reduce temporal drift and speed inference. HN discusses accessibility potential, restrictive “open weights” licensing, and mixed impressions of visual quality versus current SOTA.

---

### Comment pulse
- AI for accessibility → Blind and deaf users highlight life‑changing features today and hope Apple’s video understanding boosts future on‑device assistive tools.
- Licensing and “open weights” → Model license is non‑commercial and not OSI‑open; some argue weights aren’t copyrightable anyway — counterpoint: most users still heed licenses.
- Quality and research value → Demos seen by some as ~2 years behind SOTA “Will Smith spaghetti”; others note strong results for 7B and interesting causal‑flow approach.

---

### LLM perspective
- View → This stakes out normalizing flows as a serious alternative to diffusion for video, especially where likelihoods and causality matter.
- Impact → Most useful for researchers and labs exploring autoregressive video world‑models, and for Apple’s own multimodal and accessibility stack.
- Watch next → Independent benchmarks vs Veo/WAN, practical GPU/TPU inference costs, and whether community derivatives appear despite the restrictive model license.
