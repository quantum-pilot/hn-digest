# I trained a small transformer in 1.5hrs and it beats many LLMs

- Score: 611 | [HN](https://news.ycombinator.com/item?id=49519939) | Link: https://mvakde.github.io/blog/44-on-arc-1/

### TL;DR

An independent researcher reports training a small autoregressive transformer from scratch on one RTX 5090 in 1.5 hours for $0.67, reaching 44% on the public ARC-AGI-1 evaluation and 7% on ARC-2. The approach jointly learns across puzzles, uses per-task embeddings, 3D positional encoding, controlled augmentations, and output-only supervised loss; architecture, data diversity, and eight-layer scaling drove gains. The author filtered overlapping ARC-2 tasks and now compares only with similar test-time-training systems. Commenters praised sample efficiency but questioned public-set overfitting and evaluation conventions.

### Comment pulse

- The author stressed this is a task-specific small transformer, not an LLM, designed to probe sample efficiency under low compute.
- Critics requested private holdout results because architecture choices can indirectly overfit a public evaluation set.
- Readers debated training on unlabeled evaluation inputs; metalearning permits transduction, but batching all tasks complicates real-world and cost comparisons.

### LLM perspective

- View: The compelling result is inexpensive iteration, not evidence that a specialized ARC solver surpasses general-purpose models broadly.
- Impact: Low-cost ablations make representation and optimizer hypotheses accessible to researchers without large clusters.
- Watch next: Private-test performance, variance across runs, no-augmentation ablations, and strictly matched lifetime-compute comparisons.
