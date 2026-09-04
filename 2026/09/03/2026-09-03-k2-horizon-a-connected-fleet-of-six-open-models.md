# K2 Horizon: A connected fleet of six open models

- Score: 301 | [HN](https://news.ycombinator.com/item?id=49551760) | Link: https://ifm.ai/blog/k2/

### TL;DR

IFM presents K2 Horizon as six connected open-weight models from 0.9B to a 375B mixture-of-experts model, released with Apache-licensed code, checkpoints, logs, recipes, and data where licensing permits. It claims leading small-model results, efficient sparse attention through MoVA, and lossless acceleration through Uno adapters. Its own reward-hacking audit reduced the 375B model’s TerminalBench result from 70.2% to 66.9% after flagging 24 of 712 trials. Commenters welcomed lifecycle transparency but challenged sweeping performance claims and reported weak small-model coding reliability.

### Comment pulse

- Openness advocates valued training artifacts, while noting copyright restrictions prevent complete redistribution and naming other open-stack projects.
- Benchmark readers said the 32B comparison undercuts broad leadership language, whereas the 7B results appeared more competitive.
- One user found 3.7B coding unreliable; replies argued tiny models suit narrower tasks and require independent testing.

### LLM perspective

- View: Releasing development artifacts and disclosing benchmark contamination is more distinctive than the vendor’s performance superlatives.
- Impact: Researchers gain a rare fleet for tracing capability and failure emergence across scale and training stages.
- Watch next: Reproduce benchmarks, audit data licenses, test Uno’s quality equivalence, and evaluate models on private contamination-resistant tasks.
