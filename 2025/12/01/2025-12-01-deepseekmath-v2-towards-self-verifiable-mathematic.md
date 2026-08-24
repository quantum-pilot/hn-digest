# DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning

- Score: 252 | [HN](https://news.ycombinator.com/item?id=46105079) | Link: https://huggingface.co/deepseek-ai/DeepSeek-Math-V2

### TL;DR

This 685-billion-parameter model targets proof generation rather than rewarding only correct final answers. It trains an LLM verifier, uses that verifier as the generator’s reward model, and asks the generator to identify and repair weaknesses before finalizing proofs. Verification compute is scaled to label difficult examples as generation improves. The Apache-2.0 weights reportedly reach gold-level performance on the 2025 IMO and 2024 CMO and 118/120 on Putnam 2024. Discussion focused on whether the release is genuinely open and its scores trustworthy.

### Comment pulse

- Apache licensing impressed readers → competing Olympiad-grade systems remain proprietary — counterpoint: weights without training code or data are not fully open.
- Benchmark credibility drew skepticism → the model reportedly crawled online problems without documenting decontamination of recent competitions.
- Specialized math progress prompted curiosity → commenters wondered whether proof skill transfers to debugging and algorithm generation.

### LLM perspective

- View: Self-verification addresses proof validity more directly than final-answer rewards, but evaluator errors remain a central risk.
- Impact: Researchers can inspect and adapt a powerful proof model without relying on a hosted API.
- Watch next: Contamination audits, independent proof checking, verifier calibration, and performance on genuinely unseen mathematics.
