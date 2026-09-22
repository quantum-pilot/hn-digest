# Kev: Tiny Jev-like family of decision models built on top of Qwen3.5

- Score: 449 | [HN](https://news.ycombinator.com/item?id=49783999) | Link: https://github.com/jaredpalmer/kev/tree/main

### TL;DR

Kev is an Apache-licensed family of 0.8B, 4B, and 9B Qwen3.5-based decision models supporting yes/no, multiple-choice, and scored questions through a TypeSafe System One-compatible API. It returns calibrated probabilities, runs on CUDA, ROCm, or Apple Silicon, and includes training code, frozen evaluations, playgrounds, and fine-tuning recipes. Its own documentation says Kev trails Jev on external suites, remains sensitive to option order, handles one request at a time, and needs domain testing before automating decisions.

### Comment pulse

- Simpler classifiers may beat generative decision models → embedding-based logistic or SVM systems can be tiny, fast, private, and accurate with labeled data.
- Open local alternatives address data concerns → commenters valued self-hosting, but questioned project longevity and Jev comparisons.
- Benchmark choice remains contentious → users reported open alternatives behaving less consistently than public leaderboards suggested.

### LLM perspective

- View: Kev is most useful where probabilistic judgments exceed simple classification but still require local control.
- Impact: Teams can prototype System One workflows without sending inputs to a hosted third party.
- Watch next: Test domain calibration, option-order stability, concurrency, longer contexts, and maintenance commitment.
