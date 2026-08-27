# RustGPT: A pure-Rust transformer LLM built from scratch

- Score: 355 | [HN](https://news.ycombinator.com/item?id=45247890) | Link: https://github.com/tekaratzas/RustGPT

### TL;DR

RustGPT is an educational transformer implementation written in Rust without a machine-learning framework, using ndarray for matrix operations. It includes custom tokenization, embeddings, three transformer blocks, forward and backward passes, Adam optimization, gradient clipping, basic pre-training and instruction tuning, greedy generation, tests, and an interactive mode. The repository explicitly lacks persistence, stronger sampling, evaluation metrics, and several advanced architectural features. Commenters liked its compact interfaces and simple Cargo workflow, but some saw redundant constants and vague comments as evidence of weak understanding.

### Comment pulse

- Discussion contrasted Rust’s straightforward build experience with Python packaging, though several said modern tools have reduced that pain.
- A related Rust-and-WebAssembly language-model project was shared as another learning reference.

### LLM perspective

- View: RustGPT is most valuable as inspectable teaching code, not as evidence of a competitive large-language model.
- Impact: Removing framework abstractions exposes implementation mechanics while also exposing correctness and performance burdens.
- Watch next: Look for persistence, evaluation, positional encoding, better sampling, code cleanup, and tests that verify gradients numerically.
