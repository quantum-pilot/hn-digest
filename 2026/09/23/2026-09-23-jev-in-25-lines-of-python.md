# Jev in 25 Lines of Python

- Score: 645 | [HN](https://news.ycombinator.com/item?id=49812769) | Link: https://www.nobodywho.ai/posts/jev-in-25-lines/

### TL;DR

This parody demonstrates a Jev-like interface by prompting a local 0.6B Qwen chat model with labeled choices, extracting the next-token logits for A, B, and C, and normalizing them into probabilities. The author concedes it lacks Jev’s synthetic training, reinforcement learning, and claimed calibration, and points readers to fuller open implementations. HN discussion stressed that this toy does not reproduce Jev: first-token wording, tokenization, option order, unconstrained prose, latency, accuracy, and probability calibration can all distort results.

### Comment pulse

- Raw next-token probabilities are fragile → chat models may prefer prose, letter positions, or token artifacts rather than the intended semantic choice.
- Robust classification needs controls → readers recommended dominant-mass checks, option permutations, constrained outputs, examples, and post-hoc calibration.
- The demo captures an interface, not equivalent performance → no benchmark compares its error rate, compute, latency, or calibration against Jev.

### LLM perspective

- View: Compact code can expose the mechanism while simultaneously hiding the evaluation work that makes probabilities operationally useful.
- Impact: Developers gain a local baseline, but unsafe confidence thresholds could turn prompt artifacts into automated decisions.
- Watch next: Benchmark Brier scores, option-order sensitivity, invalid outputs, throughput, and recalibration across representative datasets.
