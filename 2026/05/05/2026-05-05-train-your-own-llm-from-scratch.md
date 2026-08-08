# Train Your Own LLM from Scratch

- Score: 419 | [HN](https://news.ycombinator.com/item?id=48017948) | Link: https://github.com/angelos-p/llm-from-scratch

### TL;DR

This workshop teaches GPT fundamentals by having participants write the entire pipeline—character tokenizer, transformer blocks, training loop, optimizer schedule, and autoregressive sampling—rather than assemble a prebuilt framework. Its default six-layer, six-head model has about 10 million parameters, trains on roughly 1 MB of Shakespeare in about 45 minutes on an M3 Pro, and generates imitation verse. Smaller configurations run in five or twenty minutes, with CPU, CUDA, MPS, and Colab support. HN welcomed the approachable scope while recommending deeper Stanford and Sebastian Raschka materials for theory and systems work.

### Comment pulse

- Character tokenization fits tiny datasets → GPT-2’s 50,257-token BPE vocabulary needs much more data for recurring subword patterns.
- Laptop-scale training makes internals tangible → participants connect embeddings, attention, loss, backpropagation, scheduling, and sampling in one session.
- Larger historical experiments expose hidden costs → commenters found distributed hyperparameter searches educational but ad hoc and compute-intensive.

### LLM perspective

- **View:** The project optimizes understanding, not capability; a deliberately small model makes every component inspectable and affordable.
- **Impact:** Python developers can build intuition before adopting large training stacks or pretrained models.
- **Watch next:** Learner completion, cross-hardware reproducibility, and added exercises on profiling, scaling laws, evaluation, and BPE datasets.
