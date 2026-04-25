# Show HN: How LLMs Work – Interactive visual guide based on Karpathy's lecture

- Score: 231 | [HN](https://news.ycombinator.com/item?id=47886517) | Link: https://ynarwal.github.io/how-llms-work/

### TL;DR
- Explains end‑to‑end how modern LLMs like GPT‑4 are built: massive web crawls are aggressively filtered into ~44TB of high‑quality text, tokenized into ~15T subword tokens, then used to train a 100B+ parameter Transformer to predict the next token.  
- The pre‑trained “internet simulator” is turned into a helpful assistant via supervised chat fine‑tuning and RLHF.  
- It clarifies quirks (hallucinations, knowledge cutoff, no persistent self) and how RAG and tools ground and extend models.

---

### LLM perspective
- View: This guide is an accurate, approachable systems overview that demystifies LLMs without hand‑waving “magic intelligence” narratives.  
- Impact: Especially useful for engineers, PMs, and policymakers needing intuition about risks, limits, and where interventions (data, RLHF, RAG) matter.  
- Watch next: Better public visualizations of attention, training dynamics, and failure modes; more transparent data/compute reporting from major labs.
