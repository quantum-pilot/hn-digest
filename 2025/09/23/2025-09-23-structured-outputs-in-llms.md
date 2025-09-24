# Structured Outputs in LLMs

- Score: 194 | [HN](https://news.ycombinator.com/item?id=45345207) | Link: https://parthsareen.com/blog.html#sampling.md

- TL;DR
    - Structured outputs enforce formats (JSON/grammars) during generation instead of post-hoc parsing. HN highlights Guidance/LLGuidance, which masks invalid tokens during decoding to keep latency low. Commenters doubt “perfect JSON” from sampling; specialized models improve but constraints remain the reliable path. Practitioners note constraints can skew distributions and hide errors (e.g., hallucinated URLs), recommending LLM‑friendly schemas or two‑stage parsing. Vendor notes: Gemini offers schema control and MIME-based JSON, with quirks like field reordering and gaps under Grounding.
    - _Content unavailable; summarizing from title/comments._
- Comment pulse
    - Masked decoding via Guidance/LLGuidance enables fast grammar enforcement → zeroes invalid tokens in softmax; mask computed on CPU; but needs backend integration beyond simple HTTP.
    - Perfect JSON via sampling is unlikely → probabilities can't guarantee validity; specialized models bias toward JSON (Osmosis, gpt-oss) — counterpoint: only constrained decoding is reliable.
    - Constraining skews distributions and can mask errors → more hallucinated URLs, truncated fields; mitigations: LLM-friendly schemas (flags, enums), two-stage generate-then-parse, or schema-aligned parsing (BAML).
- LLM perspective
    - View: Treat grammar constraints as inference-time feature; you need engine-level hooks, not just prompts or HTTP wrappers.
    - Impact: Product teams must budget for validity checks, retry logic, and telemetry; constraints change output distributions and failure modes.
    - Watch next: Native softmax-masking in major runtimes, early-layer pruning research, head-to-head benchmarks versus schema-aligned parsing across open/closed models.
