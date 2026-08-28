# Defeating Nondeterminism in LLM Inference

- Score: 178 | [HN](https://news.ycombinator.com/item?id=45200925) | Link: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/

### TL;DR

Thinking Machines Lab argues that temperature-zero LLM variability primarily comes from kernels lacking batch invariance, not inherently random GPU execution. Changing server load changes batch size, selecting different reduction orders or kernel strategies; floating-point non-associativity then alters logits enough to change greedy tokens. The team built batch-invariant RMSNorm, matrix multiplication, and attention operations for vLLM. Its Qwen experiment produced 80 outputs normally versus one deterministic output, with a substantial speed penalty. Commenters debated practical scope but highlighted bug reproduction and regulated uses.

### Comment pulse

- Determinism is narrower than semantic stability → identical execution does not make paraphrases or changed contexts behave equivalently.
- Reproducibility still matters → stable outputs simplify debugging, auditing, evaluation, and reconstruction of regulated decisions.
- The mechanism was familiar to some → JAX users said batch-dependent numerics had been documented previously.

### LLM perspective

- View: Separating batch invariance from run-to-run kernel determinism turns a vague problem into an engineering target.
- Impact: Researchers can align sampling and training numerics, while serving operators must trade throughput for reproducibility.
- Watch next: Optimized kernels, broader model tests, hardware portability, distributed reductions, and independent reproduction of RL gains.
