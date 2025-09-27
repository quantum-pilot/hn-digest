# Modular Manifolds

- Score: 119 | [HN](https://news.ycombinator.com/item?id=45388728) | Link: https://thinkingmachines.ai/blog/modular-manifolds/

- TL;DR
  - The post proposes constraining neural-network weights to manifolds and optimizing in their tangent spaces with task-appropriate norms. Concretely, it derives “manifold Muon”: steepest descent on the Stiefel manifold (orthonormal columns) under a spectral-norm step, solved via dual ascent and retracted with the matrix sign. A tiny CIFAR‑10 MLP beats AdamW but with higher per-step cost; singular values stay near 1. It then generalizes to “modular manifolds,” composing layers via product manifolds and a max-norm to budget learning rates. HN debates novelty, practicality, and scale.

- Comment pulse
  - Not new → Manifold optimization is classical; PyManopt exists. Replies: novelty is in scale and optimizer combo; incremental glue matters.
  - Modest gains, more compute → Plot shows small accuracy lift and regularization; may help online RL. — counterpoint: learning rate alone doesn’t imply overfitting.
  - Theory gap claim → Skepticism that SLT captures LLM macro-behavior; readers ask for concrete elaboration.

- LLM perspective
  - View: Stiefel constraints with spectral steps can stabilize training and decouple LR from weight scale drift.
  - Impact: If overhead drops, could supplant weight decay/orthogonal init in transformer blocks.
  - Watch next: Large-model benchmarks, dual-ascent iteration ablations, GPU-fast matrix sign (e.g., Polar Express) in training loops.
