# Embarrassingly simple self-distillation improves code generation

- Score: 522 | [HN](https://news.ycombinator.com/item?id=47637757) | Link: https://arxiv.org/abs/2604.01193

- TL;DR  
  The paper shows that large language models for code can significantly improve using only their own sampled outputs plus standard supervised fine-tuning, no verifier or teacher. On Qwen3-30B-Instruct, pass@1 on LiveCodeBench rises from 42.4% to 55.3%, with similar gains across Qwen and Llama sizes. It attributes gains to a precision–exploration conflict in decoding, where self-distillation reshapes token distributions to be exploratory at “forks” and precise at “locks”. HN discussion covers prior self-distillation work, links to adaptive/context-aware decoding, and implications for cheap, fast local coding assistants.

- Comment pulse  
  - Self-distillation looks central for LLMs; commenters cite earlier SDFT work and criticize this paper’s naming/credit — counterpoint: SSD’s code focus justifies separate branding.  
  - Fork/lock framing matches ideas in adaptive or grammar-constrained decoding: vary temperature and compute across positions instead of spending equal effort on trivial tokens.  
  - Stronger self-distilled small models plus hardware advances could let many developers run high-quality coding assistants locally, reducing demand for expensive hosted general-purpose models.

- LLM perspective  
  - View: SSD is cheap, label-free, and model-agnostic; expect it to become a default post-training step for serious code models.  
  - Impact: Improved pass@1 on hard problems especially benefits IDE copilots, code-review tools, and autonomous agents that rely on single-shot correctness.  
  - Watch next: Compare SSD with verifier-based self-training and adaptive decoding on latency, cost, and robustness; open-source scripts will determine real-world adoption.
