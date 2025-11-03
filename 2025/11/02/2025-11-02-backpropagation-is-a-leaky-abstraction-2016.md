# Backpropagation is a leaky abstraction (2016)

- Score: 280 | [HN](https://news.ycombinator.com/item?id=45787993) | Link: https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b

- TL;DR
    - Karpathy argues you must understand backprop because the abstraction leaks: saturating sigmoids vanish gradients, ReLUs die, RNNs explode/vanish through time, and naive value clipping (e.g., DQN) zeros gradients—use Huber loss or gradient clipping instead. Autograd won’t save you from bad activations, initialization, or optimizer settings. HN largely agrees, with a nit that “backprop” is gradient computation while the failures stem from modeling/optimization choices; practitioners praise hands-on implementations, and note that although frameworks improved since 2016, training still demands gradient-aware debugging.

- Comment pulse
    - Backprop ≠ optimization failures → pathologies come from model/activation/optimizer choices; reverse-mode AD just computes gradients — counterpoint: abstraction still leaks when using gradient descent.
    - Implementing forward/backward yourself → reveals vanishing/exploding signals, shapes intuition, and equips you to debug dead ReLUs, bad inits, and masking/clipping bugs.
    - 2016-era tricks vs now → frameworks expose clipping/normalization and recipes, yet gradient pathologies persist; LLM training remains sensitive to precision, activations, and hyperparameters.

- LLM perspective
    - View: Treat autograd as instrumentation, not magic; monitor gradient stats per layer and time-step during training.
    - Impact: Better diagnostics reduce training instability, especially in RNNs and RL; fewer silent failures from clipping or dead activations.
    - Watch next: Bench gradient-health dashboards across PyTorch/TF; compare Huber vs clipping; test dtype effects (bf16/fp16/fp32) on stability.
