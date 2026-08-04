# How LLMs work

- Score: 837 | [HN](https://news.ycombinator.com/item?id=48389360) | Link: https://www.0xkato.xyz/how-llms-actually-work/

### TL;DR

The explainer traces modern LLMs: subword tokens become embeddings; RoPE encodes relative position by rotating query and key vectors; multi-head attention exchanges context; feed-forward layers transform tokens; residual connections and normalization stabilize deep stacks; logits drive autoregressive next-token sampling. It also covers grouped-query attention, KV caches, mixture-of-experts, speculative decoding, and how weights, scale, data, and post-training differentiate models. HN admired the architecture’s simplicity relative to its capabilities, while stressing that datasets, reinforcement learning, experiments, and compute are the real moat—and that forward-only generation creates path-dependent errors.

### Comment pulse

- Scaling is the breakthrough → the core decoder transformer is conceptually simple, but enormous dimensions unlock emergent behavior.
- Autoregression creates commitment → emitted text cannot be internally revised, encouraging coherent rationalization — counterpoint: reasoning scratchpads, tool edits, and text diffusion create recovery paths.
- Explanatory order matters → introducing RoPE before Q/K/V invited confusion, even though position rotates queries and keys rather than semantic embeddings.

### LLM perspective

- **View:** Knowing components explains mechanism, not capability; emergent behavior depends on learned representations and training dynamics across scale.
- **Impact:** Educational materials should sequence prerequisites and label intuitions as approximations, because small geometric errors compound into false mental models.
- **Watch next:** Compare autoregressive, tool-editing, and diffusion systems on planning, self-correction, factuality, latency, and compute at matched quality.
