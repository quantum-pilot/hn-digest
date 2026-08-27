# Modular Manifolds

- Score: 119 | [HN](https://news.ycombinator.com/item?id=45388728) | Link: https://thinkingmachines.ai/blog/modular-manifolds/

### TL;DR

Thinking Machines proposes constraining neural-network weights to manifolds and co-designing optimizers around that geometry. Its manifold Muon keeps matrices on the Stiefel manifold, giving unit condition number, while “modular manifolds” compose per-layer constraints and norms to budget learning rates according to output sensitivity. A small CIFAR-10 multilayer-perceptron experiment beat AdamW modestly in train and test accuracy but increased wall-clock time per step. The post frames this as a research program, with open questions in scaling, numerics, convergence, regularization, and efficient GPU operations.

### Comment pulse

- Readers found the presentation sensible but questioned practical benefit given marginal accuracy gains and higher per-step cost.
- Some called manifold optimization established—counterpoint: commenters suggested the Muon combination, compositional abstraction, and scale could still matter.

### LLM perspective

- View: The contribution is optimizer-architecture composition more than the old idea of projecting weights onto manifolds.
- Impact: Better-conditioned weights could simplify tuning and robustness, but added optimization work may erase training gains.
- Watch next: Large-model experiments, ablations, convergence proofs, GPU kernels, low-precision effects, and comparisons with simpler normalization.
