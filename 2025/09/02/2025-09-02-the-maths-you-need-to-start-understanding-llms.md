# The maths you need to start understanding LLMs

- Score: 609 | [HN](https://news.ycombinator.com/item?id=45110311) | Link: https://www.gilesthomas.com/2025/09/maths-for-llms

- TL;DR
  - The post demystifies the math needed to grasp LLM inference—not training—using high‑school tools: vectors in high dimensions; logits→softmax over vocabulary; embeddings compared via dot/cosine; and matrix multiplication as projections. A linear layer is a projection plus bias; activations provide nonlinearity. HN discussion points to practical study paths and notes that while these basics are necessary, understanding behavior in very large transformers and how uncertainty compounds across tool/agent chains remains challenging.

- Comment pulse
  - Math backgrounds now useful → linear algebra, optimization, even differential geometry; suggestions: Geometric Deep Learning, diffusion/flow models, and computer graphics.
  - Karpathy’s tutorials and Raschka’s book/code help newcomers → implement small transformers step‑by‑step; reading alternatives to videos requested.
  - Scope caution: embeddings/dot products start you off → trillion‑parameter transformers remain matrices+activations, yet internal representations and agent‑chain uncertainty hard to interpret — counterpoint: human‑in‑loop/orchestrators mitigate.

- LLM perspective
  - View: Ground LLM intuition in vectors, softmax, projections; treat layers as dimensionality transforms plus nonlinearities.
  - Impact: Helps engineers debug logits, sampling, and embedding similarity; informs orchestrators to limit cascades and insert human checks.
  - Watch next: Study gradients, cross-entropy, Adam, and scaling laws; benchmark chain uncertainty; follow interpretability results on attention heads and circuits.
