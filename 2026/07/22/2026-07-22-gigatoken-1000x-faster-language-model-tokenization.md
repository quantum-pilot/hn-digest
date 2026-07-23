# GigaToken: ~1000x faster Language model tokenization

- Score: 332 | [HN](https://news.ycombinator.com/item?id=49010167) | Link: https://github.com/marcelroed/gigatoken/

## TL;DR

Gigatoken is a highly optimized Rust tokenizer that hits gigabytes per second on modern CPUs, often ~100–1000× faster than HuggingFace tokenizers and tiktoken on common LLM vocabularies. It achieves this via SIMD-based pretokenization (instead of regex), aggressive cache hierarchies for repeated words, minimal branching, and reduced Python/thread interaction. It can act as a drop-in replacement for HF/tiktoken or via its own fastest API. HN discussion debates practical impact, highlighting offline data prep, routing, and latency-sensitive workloads.

---

## Comment pulse

- Tokenization is often <0.1% of inference time → but 1000× faster still reduces time-to-first-token and saves real money at hyperscale — counterpoint: many apps won’t notice.

- Some celebrate the “over-optimization” as pure engineering craft → others note specific workflows (routing, rate limiting, small SLMs) where tokenization dominates CPU time.

- Training pipelines benefit most → GB/s tokenization makes multi-terabyte corpus prep substantially cheaper and shortens iteration cycles when tweaking datasets.

---

## LLM perspective

- View: Tokenization was a neglected bottleneck; this proves substantial headroom still exists in CPU-bound parts of AI stacks.

- Impact: Infra providers, dataset engineers, and any system doing heavy pretokenization or routing on CPUs gain the clearest wins.

- Watch next: Wider SentencePiece/WordPiece support, integration into HF/sglang stacks, and independent benchmarks on real-world mixed workloads and cache hit patterns.
