# Show HN: How I Topped the HuggingFace Open LLM Leaderboard on Two Gaming GPUs

- Score: 260 | [HN](https://news.ycombinator.com/item?id=47322887) | Link: https://dnhkng.github.io/posts/rys/

## TL;DR

A hobbyist systematically “re-layered” big open LLMs and found that duplicating a *contiguous block* of ~7 **middle** layers—without changing any weights—boosted performance across HuggingFace’s Open LLM Leaderboard, taking Qwen2‑72B from 72B to 78B effective parameters and hitting #1. Single-layer repeats or misaligned blocks usually hurt. Using hard-math and emotional-intelligence probes to scan all (start, end) layer pairs, he observed consistent “circuits” in the middle: multi-layer reasoning units that only work as intact blocks, suggesting a genuine “neuroanatomy” of transformers and a cheap test-time way to scale depth on gaming GPUs.

---

## Comment pulse

- Layer circuits feel intuitive → readers see evidence for latent-space reasoning and dream of modular, pluggable “knowledge banks” instead of monolithic, fully-retrained models.  
- Community/academia lagged → Goliath-style Frankenstein models already showed layer interchangeability but were treated as toys; only recent papers formalize duplicated/recurrent blocks.  
- Methodology inspires → people ask for tools to auto-find circuits and for better numeric scoring; suggest grammar-constrained outputs and diagnostics like WeightWatcher.

---

## LLM perspective

- View: This is structured test-time depth scaling via reusing trained circuits, hinting that transformers self-organize into modular cognitive “organs.”  
- Impact: Lets small teams enhance reasoning on existing checkpoints, and informs where to add recurrence or surgery in future model designs.  
- Watch next: Public circuit-scanning code, partial fine-tuning at junction “seams,” and head-to-head benchmarks vs MoE and standard deeper variants.
