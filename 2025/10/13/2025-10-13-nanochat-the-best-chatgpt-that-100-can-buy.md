# NanoChat – The best ChatGPT that $100 can buy

- Score: 821 | [HN](https://news.ycombinator.com/item?id=45569350) | Link: https://github.com/karpathy/nanochat

- TL;DR
  - Karpathy’s nanochat is a minimal, full-stack ChatGPT-like pipeline you can train end-to-end for ~$100 in ~4 hours on a single 8×H100. One script handles tokenization, pretrain, SFT, RL, eval, and a web UI; the $100 model (~4e19 FLOPs) is toy-level, with larger $300 d26 and ~$1000 tiers planned. HN highlights limits of AI coding tools on novel code, lineage via modded‑nanoGPT/Muon speedups, community repros and metrics like bits-per-byte, plus cost/compute questions.

- Comment pulse
  - AI coding tools falter on novel repos → Karpathy hand-wrote most; temper AGI hype — counterpoint: superb on web tasks with rich training coverage.
  - Lineage and speed → nanoGPT → modded‑nanoGPT; Muon optimizer credited for faster small-model training, reportedly seeing rapid adoption.
  - Repro attempts → community trained and published models; outcomes vary by seed; bits‑per‑byte preferred over CE for tokenizer‑invariant tracking.

- LLM perspective
  - View: A clean, end-to-end baseline demystifies LLM pipelines and invites modification over framework-driven complexity.
  - Impact: Lowers entry cost for coursework, indie labs, and product teams to prototype, eval, and serve small assistants.
  - Watch next: d26/$1000 recipes, reproducible eval dashboards, Muon vs AdamW ablations, sub‑80GB GPU configs, and CPU/MPS backends.
