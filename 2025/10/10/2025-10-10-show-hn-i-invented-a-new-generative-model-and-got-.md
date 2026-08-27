# Show HN: I invented a new generative model and got accepted to ICLR

- Score: 488 | [HN](https://news.ycombinator.com/item?id=45536694) | Link: https://discrete-distribution-networks.github.io/

### TL;DR

Discrete Distribution Networks approximate continuous data through hierarchical layers that each produce K discrete candidate samples, select the candidate nearest the training target, and refine it in later layers. A Split-and-Prune optimizer addresses dead nodes and density shifts. The ICLR 2025 paper reports reconstruction, image generation, tree-structured one-dimensional latents, and zero-shot conditional generation without gradients, but describes its experiments as preliminary. HN readers praised the single-author novelty and open reviews while questioning overfitting, compute interpretation, and philosophical branding.

### Comment pulse

- Open reviews aid evaluation → public acceptance debate gives outsiders context and authors reusable explanations of perceived novelty.
- Sample quality prompted leakage questions → striking correspondences may reflect generalization, dataset bias, cherry-picking, overfitting, or coincidence.
- Inference cost was clarified → random branch choices can be made before computation, avoiding K-minus-one discarded outputs at generation time.

### LLM perspective

- View: DDN is an intriguing alternative representation, but acceptance and demonstrations do not establish competitive scaling.
- Impact: Researchers gain a debuggable hierarchical model for conditional generation, clustering, compression, and uncertainty experiments.
- Watch next: Demand independent reproduction, held-out tests, compute comparisons, scaling results, ablations, and high-dimensional failure analysis.
