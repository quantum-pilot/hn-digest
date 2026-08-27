# NanoChat – The best ChatGPT that $100 can buy

- Score: 821 | [HN](https://news.ycombinator.com/item?id=45569350) | Link: https://github.com/karpathy/nanochat

### TL;DR

NanoChat is Andrej Karpathy's minimal, dependency-light implementation of an entire chat-model pipeline: tokenization, pretraining, fine-tuning, evaluation, inference, and web serving. Its advertised $100 tier runs about four hours on eight H100 GPUs and produces a deliberately weak, kindergarten-like model; larger $300 and $1,000 tiers remain incomplete. The project prioritizes readable, hackable education over framework flexibility. HN users began reproducing runs, discussed its nanoGPT lineage and optimizer ideas, and noted Karpathy found coding agents unhelpful on this unusual codebase.

### Comment pulse

- Educational completeness is the attraction → one compact repository exposes stages normally hidden across frameworks and services.
- Reproduction varies → one commenter trained and shared a weaker result, illustrating seed and pipeline sensitivity at small scale.
- Coding-agent usefulness appears distribution-dependent → familiar web tasks fare better than novel algorithmic model work.

### LLM perspective

- View: NanoChat's value is inspectability, not competitiveness with commercial assistants or frontier training systems.
- Impact: Learners can modify an end-to-end baseline while seeing exactly what a constrained compute budget buys.
- Watch next: Track reproducibility, larger tiers, hardware portability, tests, and improvements that preserve the repository's simplicity.
