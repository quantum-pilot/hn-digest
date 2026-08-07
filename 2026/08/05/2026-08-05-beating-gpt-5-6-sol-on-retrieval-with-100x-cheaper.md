# Beating GPT-5.6 Sol on retrieval with 100x cheaper open models

- Score: 425 | [HN](https://news.ycombinator.com/item?id=49186762) | Link: https://neon.com/blog/how-castform-neon-beats-frontier-models-on-price-and-efficiency

### TL;DR

Castform argues that reinforcement-learning post-training can turn cheap open-weight models into specialized agentic retrievers that outperform costly frontier models. Its pipeline stores source documents in Neon Postgres, synthesizes question-answer tasks, lets training rollouts query hybrid BM25/vector search, and rewards correct retrieval, citations, and answers. Neon supplies burst-friendly autoscaling plus database branches for isolated stateful rollouts; Castform manages training and observability. The company claims a typical frontier-model search costs about $0.03 and takes over 10 seconds, while smaller models can be roughly 100 times cheaper.

### Comment pulse

- Commenters placed the approach among trained retrieval models, alongside dedicated retrievers and generator-evaluator harnesses.
- Specialized models drew enthusiasm, but skeptics questioned whether benchmarks test buried or linked evidence in truly large corpora.
- The founder said frontier models should retain general-purpose leadership while tuned models serve long-tail applications.

### LLM perspective

- View: Task-specific post-training is most compelling when queries, tools, and rewards are stable.
- Impact: Lower inference cost could make iterative retrieval economically viable at production scale.
- Watch next: Independent evaluation on larger corpora, multi-hop questions, and reward-hacking resistance.
