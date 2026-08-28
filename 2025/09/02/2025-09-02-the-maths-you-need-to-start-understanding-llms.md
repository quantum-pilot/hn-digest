# The maths you need to start understanding LLMs

- Score: 609 | [HN](https://news.ycombinator.com/item?id=45110311) | Link: https://www.gilesthomas.com/2025/09/maths-for-llms

### TL;DR

This introduction covers mathematical foundations for LLM inference, not training or a complete explanation of transformer behavior. It treats vectors as points or directions in high-dimensional spaces: logits occupy vocabulary space, softmax converts them into probability distributions, and embeddings encode task-dependent similarity. Dot products compare vector direction, while matrix multiplication projects batches between spaces of different dimensions. A neural-network linear layer is such a projection plus bias; activation functions add essential nonlinearity. The operations are largely high-school mathematics, even when dimensions are enormous and difficult to visualize.

### Comment pulse

- Readers recommend actively implementing worked examples and models instead of only watching explanatory material.
- Critics stress that embeddings and projections are prerequisites, not explanations of behavior inside a huge trained transformer.

### LLM perspective

- View: The article usefully lowers the mathematical entry barrier while drawing a boundary around what those basics explain.
- Impact: Understanding logits, softmax, similarity, and projections makes model interfaces less mysterious without resolving interpretability.
- Watch next: The promised synthesis covering attention, token embeddings, context transformations, and training mathematics.
