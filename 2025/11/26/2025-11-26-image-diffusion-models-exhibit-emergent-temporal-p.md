# Image Diffusion Models Exhibit Emergent Temporal Propagation in Videos

- Score: 110 | [HN](https://news.ycombinator.com/item?id=46055177) | Link: https://arxiv.org/abs/2511.19936

### TL;DR

Researchers show that a pretrained image diffusion model contains self-attention patterns that can serve as semantic label propagation kernels. Linking those correspondences across consecutive frames turns an image generator into a zero-shot video object tracker without task-specific fine-tuning. Their DRIFT framework combines DDIM inversion, textual inversion, adaptive attention-head weighting, and SAM-guided mask refinement, reporting leading results on standard segmentation benchmarks. Commenters highlighted both the practical repurposing and the continuing research value of older, compact diffusion checkpoints.

### Comment pulse

- Image models can track video without retraining → self-attention links semantically corresponding regions across consecutive frames.
- Test-time adaptation matters → inversion, learned text, and attention-head weighting stabilize propagation before SAM refines masks.
- Older diffusion checkpoints remain research platforms → compact, familiar models expose reusable representations to hobbyists and academics.

### LLM perspective

- View: The novelty is reuse of latent correspondence, not a new video-specific foundation model.
- Impact: Zero-shot tracking could reduce annotation and task-specific training costs for video segmentation pipelines.
- Watch next: Independent benchmark replication, occlusion failures, compute overhead, and sensitivity to first-frame masks.
