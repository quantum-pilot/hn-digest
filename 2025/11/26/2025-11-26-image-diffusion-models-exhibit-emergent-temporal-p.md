# Image Diffusion Models Exhibit Emergent Temporal Propagation in Videos

- Score: 110 | [HN](https://news.ycombinator.com/item?id=46055177) | Link: https://arxiv.org/abs/2511.19936

### TL;DR

This preprint reports that self-attention in a pretrained image-diffusion model can act as a pixel-correspondence kernel for semantic label propagation. Extending those correspondences between adjacent frames enables video object tracking from an initial segmentation without task-specific model fine-tuning. The proposed DRIFT framework combines this mechanism with DDIM inversion, textual inversion, adaptive attention-head weighting, and SAM-guided mask refinement. Its authors claim state-of-the-art zero-shot results on standard video-segmentation benchmarks, but the supplied source contains only the abstract, so methods and comparisons cannot be independently assessed here.

### Comment pulse

- Readers highlighted older diffusion models as useful research playgrounds whose learned representations support tasks beyond generation.
- A commenter questioned the chosen soft-IoU formulation and urged deliberate treatment of fuzzy intersection semantics.

### LLM perspective

- View: Reusing generative attention as correspondence suggests model capability is broader than its training interface.
- Impact: Effective tracking without fine-tuning could reduce task-specific training, though test-time optimization still adds complexity.
- Watch next: Full benchmark details, compute cost, failure modes, ablations, and performance on distribution shifts.
