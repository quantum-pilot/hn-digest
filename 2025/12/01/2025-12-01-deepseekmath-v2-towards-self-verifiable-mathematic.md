# DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning

- Score: 252 | [HN](https://news.ycombinator.com/item?id=46105079) | Link: https://huggingface.co/deepseek-ai/DeepSeek-Math-V2

- TL;DR  
  DeepSeekMath‑V2 is a 685B‑parameter open‑weights math model that couples a proof generator with a learned verifier, rewarding step‑by‑step correctness instead of just final answers. Trained with scaled verification compute, it reportedly reaches near‑perfect scores on recent IMO, CMO, and Putnam proof benchmarks. HN likes the Apache‑2.0 release and rapid open‑model progress, but questions possible benchmark contamination and contrasts this openness with proprietary IMO‑gold systems from OpenAI/DeepMind that remain unreleased.

- Comment pulse  
  - Open Apache‑2.0 weights seen as a big win versus closed IMO‑gold models—counterpoint: without training data/code, some still view this as effectively proprietary.  
  - Many are impressed by open models nearing SOTA in math and wonder about spillover to coding; others note math‑specialized models may lag frontier code assistants.  
  - Skeptics highlight training contamination from crawled competition problems and absent decontamination; contrast with claims OpenAI/Google evaluated on unseen 2025 sets and withheld models for marketing.

- LLM perspective  
  - View: Verifier‑driven RL for proofs pushes beyond answer‑only rewards and could generalize to other structured reasoning tasks.  
  - Impact: Stronger open math models may democratize contest‑level problem solving and assist formalization in Lean, Coq, and similar systems.  
  - Watch next: Independent contamination audits, cross‑evals on held‑out competitions, and practical IDE/informal‑math integrations that expose real‑world robustness limits.
