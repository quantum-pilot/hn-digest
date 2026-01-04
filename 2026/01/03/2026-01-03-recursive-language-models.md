# Recursive Language Models

- Score: 106 | [HN](https://news.ycombinator.com/item?id=46475395) | Link: https://arxiv.org/abs/2512.24601

## TL;DR
Recursive Language Models (RLMs) treat very long inputs as an external environment instead of a single giant prompt. The model plans how to inspect, decompose, and recursively call itself over relevant snippets, building a tree of sub-queries that fits within its native context window. Experiments show large quality gains and 100× longer effective contexts at similar or lower cost than standard long-context tricks. HN readers like the formalization but debate how novel it is versus existing subagent, RAG, and agentic workflows.

## Comment pulse
- RLMs are just subagents → Existing systems already spawn helper LLMs on files or tasks; recursion and shared context feel incremental, not fundamentally new.  
- Different from RAG/workflows → Here the model decides what to read, how many calls to make, and when to answer, enabling fully recursive search.  
- Practical wishlists → Developers want compaction/recursion exposed as swappable hooks in tools like Claude Code — counterpoint: today’s implementations are often just one summarization prompt.

## LLM perspective
- View: Treating context as an environment with LM-driven recursive access is a clean unifying abstraction for many existing agent patterns.  
- Impact: Makes smaller-context models more competitive for codebases, logs, and large corpora, reducing dependence on ultra-long-context proprietary models.  
- Watch next: Robustness to planning errors, adversarial documents, and whether end-to-end training can learn better recursive strategies than hand-designed scaffolds.
