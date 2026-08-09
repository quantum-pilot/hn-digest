# Embarrassingly simple self-distillation improves code generation

- Score: 522 | [HN](https://news.ycombinator.com/item?id=47637757) | Link: https://arxiv.org/abs/2604.01193

### TL;DR

A preprint proposes simple self-distillation: sample a model’s own code solutions under selected temperature and truncation settings, then apply ordinary supervised fine-tuning without a teacher, verifier, or reinforcement learning. Qwen3-30B-Instruct rose from 42.4% to 55.3% pass@1 on LiveCodeBench v6, with reported gains across Qwen and Llama models from 4B to 30B. The authors attribute gains to balancing exploratory fork points with precise lock points. Commenters connected this to adaptive decoding and earlier self-distillation work, while asking about naming, credit, and broader generalization.

### Comment pulse

- Training reshapes distributions contextually without labeling fork or lock tokens → the mechanism remains a hypothesis requiring deeper causal tests.
- Code offers objective benchmarks for evaluating gains → analogous improvements in open-ended generation may be harder to measure.
- Better local models could reduce provider dependence → frontier systems may retain advantages from tools, memory, and continual improvement.

### LLM perspective

- **View:** The practical appeal is a low-complexity post-training recipe, but one benchmark jump should not establish robustness.
- **Impact:** Open-model builders can trade generation and fine-tuning compute for stronger code performance without external labels.
- **Watch next:** Independent replication, training cost, contamination controls, multilingual code, non-code tasks, and comparisons with SDFT and adaptive decoding.
