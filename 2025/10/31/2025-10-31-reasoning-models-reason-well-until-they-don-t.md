# Reasoning models reason well, until they don't

- Score: 200 | [HN](https://news.ycombinator.com/item?id=45769971) | Link: https://arxiv.org/abs/2510.22371

### TL;DR

The paper introduces DeepRD, a generator for graph-connectivity and natural-language proof-planning tasks whose complexity can scale beyond existing benchmarks. Its authors report that current large reasoning models perform well until a threshold, then decline abruptly and fail to generalize; most surveyed real-world cases sit within the success region, but long tails remain risky. HN discussion debates whether larger models, more reinforcement learning, or tool-using harnesses merely move that boundary, and questions how broadly these formal tasks represent reasoning outside mathematics.

### Comment pulse

- The result bounds current systems → it does not prove future scaling or tool use cannot extend their reliable complexity range.
- Failure recognition matters → commenters distinguish reaching a limit from confidently inventing an answer beyond it.
- Definitions remain narrow → graph traversal and proof planning are measurable, but may not represent reasoning about ambiguous physical-world questions.

### LLM perspective

- View: A sharp capability boundary is operationally dangerous when models do not reliably signal crossing it.
- Impact: High-stakes workflows need complexity-aware routing, verification, or decomposition rather than benchmark-average confidence.
- Watch next: Replicate DeepRD with agents, tools, larger models, and calibrated abstention across complexity levels.
