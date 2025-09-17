# RustGPT: A pure-Rust transformer LLM built from scratch

- Score: 355 | [HN](https://news.ycombinator.com/item?id=45247890) | Link: https://github.com/tekaratzas/RustGPT

- TL;DR
  - RustGPT is a pure-Rust transformer LLM built from scratch using ndarray—no ML frameworks. It demonstrates end-to-end training: tiny factual pretraining, instruction tuning, then an interactive chat loop. Architecture: embeddings + 3 transformer blocks + output projection (128-d embeddings, 256 hidden, max 80 tokens), greedy decoding, Adam + gradient clipping, and comprehensive tests. It’s positioned as an educational scaffold, not a competitive model. HN praised the clean interfaces and cargo simplicity, while debating code rigor and whether Python’s “dependency hell” still applies.

- Comment pulse
  - Educational demo, not production → hard-coded settings and comments raised rigor concerns — counterpoint: succinct interfaces suggest a teaching focus.
  - Tooling trade-off → cargo run simplicity lauded; others say uv/Poetry largely resolve Python packaging pain today.
  - Framework-free pain points → backprop debugging and no GPU acceleration cited; minimal dependency tree doesn’t guarantee efficiency.

- LLM perspective
  - View: Strong learning scaffold for transformer mechanics in Rust; clarity over performance or features.
  - Impact: Lowers entry for Rust devs into ML; may inspire pure-Rust training/inference tooling.
  - Watch next: Add persistence, benchmarks (perplexity), SIMD/parallelism, better decoding; positional encodings/RoPE; export formats; optional WASM demo.
