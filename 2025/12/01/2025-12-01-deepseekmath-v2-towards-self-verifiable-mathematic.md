# DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning

- Score: 252 | [HN](https://news.ycombinator.com/item?id=46105079) | Link: https://huggingface.co/deepseek-ai/DeepSeek-Math-V2

### TL;DR

DeepSeekMath-V2 trains a mathematical proof generator alongside an LLM verifier, using verification as reward and encouraging the generator to find and repair flaws before finalizing proofs. As generation improves, additional verification compute labels harder examples to preserve the verifier’s advantage. Built on DeepSeek-V3.2-Exp-Base, the 685-billion-parameter model is released under Apache 2.0. DeepSeek reports gold-level IMO 2025 and CMO 2024 results plus 118/120 on Putnam 2024, but commenters question whether online competition problems contaminated training or evaluation.

### Comment pulse

- Open weights drew praise compared with proprietary math systems — counterpoint: absent training code and data limit reproducibility.
- Specialized math strength may aid logic and coding, but commenters supplied no direct cross-domain evaluation.
- Benchmark skepticism centers on decontamination because the claimed competition problems were available online.

### LLM perspective

- View: Rewarding proof verification targets correctness of reasoning rather than only matching final numerical answers.
- Impact: Researchers can inspect and adapt the weights, but cannot fully audit training provenance from this release.
- Watch next: Evaluate on unseen proofs with independent graders, explicit contamination controls, and verifier-error analysis.
