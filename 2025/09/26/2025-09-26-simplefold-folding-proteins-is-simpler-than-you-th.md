# SimpleFold: Folding proteins is simpler than you think

- Score: 232 | [HN](https://news.ycombinator.com/item?id=45389267) | Link: https://github.com/apple/ml-simplefold

- TL;DR
  - Apple’s SimpleFold swaps AlphaFold-style bespoke modules for plain transformers trained with flow-matching, scaled to 3B parameters and 8.6M+ distilled structures. It reports competitive CASP/CAMEO accuracy, strong ensembles, and fast local inference via PyTorch/MLX, targeting Macs. HN applauds the simplification and potential scaling, but flags that most training labels come from MSA-heavy models—so “simplicity” piggybacks on upstream complexity. Skeptics say it trails SOTA; others see Apple’s aims as enabling local workflows and showcasing hardware/research.

- Comment pulse
  - Simplicity piggybacks on AF/ESM labels → MSA biases baked in; test on orphan proteins to rule out leakage/rote memorization — counterpoint: scale often closes gaps.
  - ML vs physics → statistical folding is cheap and fast for similar sequences; simulations still needed for dynamics and validation.
  - Apple’s angle → local inference on Macs via MLX lowers barriers for labs; also serves chip marketing and research brand-building.

- LLM perspective
  - View: Distills complex MSA pipelines into a plain transformer with flow-matching; architecture minimalism plus vast distillation, not pure from-scratch learning.
  - Impact: Cheaper, faster local folding; simplifies stacks without MSA preprocessing; may democratize iterative design and ensemble sampling on commodity hardware.
  - Watch next: Head-to-head on orphan proteins, de novo folds, multimers; open weights; Mac benchmarks vs ESMFold/AF; physics-guided refinement and dynamics coupling.
