# Recursive Language Models

- Score: 106 | [HN](https://news.ycombinator.com/item?id=46475395) | Link: https://arxiv.org/abs/2512.24601

### TL;DR

Recursive Language Models treat an oversized prompt as an external environment that a model can inspect programmatically, split into snippets, and process through recursive calls to itself. The authors report handling inputs up to 100 times beyond the model’s context window while outperforming common long-context scaffolds at comparable or lower query cost. HN discussion questions the novelty, comparing the method with subagents, RAG, and earlier agent loops; supporters distinguish it by letting the model choose context decomposition recursively rather than following a fixed retrieval workflow.

### Comment pulse

- Novelty is disputed → repeated model calls resemble subagents and earlier agents, without an end-to-end trained recursive model.
- Agency distinguishes it from conventional RAG → the model decides what to inspect, how to decompose, and when to stop.
- Shared external context is central → recursive calls operate over the same files or variables without filling the primary context.

### LLM perspective

- View: The contribution is adaptive context management, not a fundamentally new neural architecture.
- Impact: Long-document systems may trade one enormous inference for observable, task-specific recursive exploration.
- Watch next: Evaluate planning failures, recursion depth, cost variance, reproducibility, and comparisons against strong agentic RAG baselines.
