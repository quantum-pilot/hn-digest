# Extract-0: A specialized language model for document information extraction

- Score: 181 | [HN](https://news.ycombinator.com/item?id=45427634) | Link: https://arxiv.org/abs/2509.22906

### TL;DR

An arXiv paper presents Extract-0, a 7.66-billion-parameter document-extraction model trained on 280,128 synthetic examples using LoRA and GRPO. It reports a 0.573 mean reward across 1,000 tasks, above several much larger general models, while modifying only 0.53% of weights. HN reviewers identified a potentially decisive evaluation flaw: code appears to train and test from the same dataset and split by chunk rather than source document. That leakage makes the headline comparison unreliable until tested on genuinely unseen documents and benchmarks.

### Comment pulse

- Narrow models remain promising → task-specific fine-tuning can reduce inference cost and beat general systems within a stable distribution.
- Evaluation undermines the claim → source documents may cross train-test boundaries, allowing familiarity with test material despite different chunks.
- Generalization is unknown → commenters requested real contracts, degraded scans, presentations, standard benchmarks, weights, and unfamiliar formats.

### LLM perspective

- View: The training recipe is interesting, but an invalid holdout can turn specialization into measured memorization.
- Impact: Teams should not replace production extractors based on these reported scores alone.
- Watch next: Document-level splits, external benchmarks, independent replication, robustness tests, released weights, and cost-quality comparisons.
