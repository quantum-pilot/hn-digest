# Backpropagation is a leaky abstraction (2016)

- Score: 280 | [HN](https://news.ycombinator.com/item?id=45787993) | Link: https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b

### TL;DR

Karpathy argues that automatic differentiation cannot safely hide the backward pass from neural-network practitioners. Sigmoids can saturate and erase gradients, ReLUs can die permanently, recurrent multiplication can make gradients vanish or explode, and clipping a forward error can accidentally produce zero gradient instead of robust optimization. Manually implementing derivatives builds intuition for initialization, activations, losses, and clipping. Commenters largely endorsed this teaching exercise, while some sharpened the terminology: backpropagation computes gradients; model geometry and gradient-based optimization create most cited failures.

### Comment pulse

- Practitioners praised implementing forward and backward passes as a high-value exercise that makes abstract derivative behavior tangible.
- Modern frameworks automate more remedies, but commenters argued LLM training still requires substantial optimization judgment.

### LLM perspective

- View: Automation removes derivative bookkeeping, not the need to understand which training signals an architecture creates.
- Impact: Engineers who inspect gradients can diagnose stalled training before blindly changing optimizers or scale.
- Watch next: Activation statistics, per-layer gradient norms, dead units, clipping frequency, and numerical precision.
