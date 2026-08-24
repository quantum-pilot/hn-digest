# DeepSeek-v3.2: Pushing the frontier of open large language models [pdf]

- Score: 491 | [HN](https://news.ycombinator.com/item?id=46108780) | Link: https://huggingface.co/deepseek-ai/DeepSeek-V3.2/resolve/main/assets/paper.pdf

### TL;DR

DeepSeek’s new model combines sparse attention, heavier reinforcement learning, and synthesized agent tasks to narrow the gap with proprietary systems. Its selector attends to 2048 tokens per query, reducing core attention complexity while preserving 128K-context performance. Post-training consumed more than 10% of pretraining compute and used 1827 synthetic environments alongside real code, search, and notebook tools. Reported reasoning results approach GPT-5; the unconstrained Speciale variant scores higher but consumes substantially more tokens. Discussion focused on what strong public models mean for industry economics and concentration.

### Comment pulse

- Open access attracted support → competitive models may constrain corporate concentration — counterpoint: skeptics questioned strategic motives behind continued publication.
- Commercial durability remained plausible → hosting, trust, integration, and cheap infrastructure can monetize models even without a unique capability moat.
- Cost-effectiveness claims met skepticism → benchmark efficiency omits company finances and most users still cannot run the full model locally.

### LLM perspective

- View: Sparse long-context inference and agent-data synthesis are more consequential than any single leaderboard comparison.
- Impact: Open-model operators gain stronger reasoning and tool use but still need substantial serving infrastructure.
- Watch next: Independent cost benchmarks, consumer-sized variants, tool-format interoperability, and token-efficiency improvements.
