# Why language models hallucinate

- Score: 275 | [HN](https://news.ycombinator.com/item?id=45147385) | Link: https://openai.com/index/why-language-models-hallucinate/

### TL;DR

OpenAI argues hallucinations originate partly in next-token pretraining, where rare arbitrary facts are not reliably inferable, and persist because accuracy-only evaluations reward guessing over abstention. Its SimpleQA example shows GPT-5-thinking-mini with lower accuracy than o4-mini but far fewer wrong answers because it abstains more. The proposed remedy is to penalize confident errors and reward calibrated uncertainty across mainstream evaluations. Commenters agreed incentives matter but disputed whether this explains errors such as reversed causality, invented APIs, or failures grounded in supplied text.

### Comment pulse

- Supporters valued a precise definition separating plausible false claims from all stochastic generation.
- Critics said language modeling predicts fluent text rather than truth, so calibration reduces but cannot eliminate factual failure.
- Fiction and factual answering need different behaviors, though both still require consistency with the prompt and established context.

### LLM perspective

- View: Better abstention addresses avoidable guessing, but not every hallucination is simply uncertainty about a missing fact.
- Impact: Leaderboards that price errors explicitly could shift models toward safer behavior in high-stakes information tasks.
- Watch next: Calibration across domains, performance on context-grounded contradictions, and scoring rules that balance usefulness against refusal.
