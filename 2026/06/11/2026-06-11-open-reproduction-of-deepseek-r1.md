# Open Reproduction of DeepSeek-R1

- Score: 244 | [HN](https://news.ycombinator.com/item?id=48489917) | Link: https://github.com/huggingface/open-r1

- TL;DR  
  - Hugging Face’s Open-R1 project aims to fully reproduce DeepSeek-R1’s reasoning pipeline with openly licensed code, datasets, and evaluation recipes. Today it delivers step 1: high-quality distillation recipes and datasets (Mixture-of-Thoughts, math/code traces) plus GRPO-based RL infrastructure, code-execution rewards, and scripts to match DeepSeek’s reported scores on AIME24, MATH-500, GPQA, and LiveCodeBench. HN commenters welcome the openness but note that pure-RL “R1-Zero” and full base→RL training remain unfinished, pointing to OLMo, Nemotron, and OpenThoughts as more complete open pipelines.

- Comment pulse  
  - Open-R1 finishes distillation; RL “R1-Zero” remains undone, partly since DeepSeek’s report skips key pieces like rigorous validators — counterpoint: partial reproducibility still helps.  
  - For truly end-to-end open pipelines, commenters favor OLMo and Nemotron, which publish full training recipes and have at least one independent reproduction.  
  - Adjacent work like OpenThoughts offers strong reasoning models and datasets, but curating large, clean math/code corpora and affording compute (hundreds of thousands–millions) remain hard.

- LLM perspective  
  - View: Open-R1 turns DeepSeek’s vague description into runnable scripts, clarifying practical details of R1-style distillation and GRPO training.  
  - Impact: Helps academic and startup groups iterate on rewards, datasets, and evaluation without first building complex GRPO and evaluation tooling.  
  - Watch next: Whether they complete RL stages, publish full cost/compute breakdowns, and converge with OLMo-style efforts on shared open benchmarks.
