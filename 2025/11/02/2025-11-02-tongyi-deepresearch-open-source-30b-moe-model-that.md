# Tongyi DeepResearch – open-source 30B MoE Model that rivals OpenAI DeepResearch

- Score: 230 | [HN](https://news.ycombinator.com/item?id=45789602) | Link: https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/

### TL;DR

Alibaba's Tongyi team released Tongyi DeepResearch-30B-A3B and claims results competitive with proprietary research agents across HLE, BrowseComp, BrowseComp-ZH, and xbench-DeepSearch. Its pipeline combines agentic continual pretraining, synthetic question-and-trajectory generation, supervised fine-tuning, and on-policy reinforcement learning in stable tool environments. Native ReAct supports 128K context; Heavy Mode repeatedly compresses workspaces and can parallelize researchers before synthesis. The team acknowledges context, larger-model scaling, and RL-efficiency limits. Commenters debated specialized models, self-hosting hardware, and whether “deep research” reports add insight beyond source discovery.

### Comment pulse

- Some readers valued these agents mainly for finding sources and surveying unfamiliar markets, not producing final analysis.
- Others expect specialized smaller models to matter chiefly when cost and latency outweigh frontier-model capability.

### LLM perspective

- View: The durable contribution may be the synthetic training environment and context-management recipe, not benchmark leadership.
- Impact: Open weights let researchers test agent pipelines locally, though a 30B model still demands substantial hardware.
- Watch next: Independent evaluations, source faithfulness, real task quality, inference cost, larger-model scaling, and reproducible training details.
