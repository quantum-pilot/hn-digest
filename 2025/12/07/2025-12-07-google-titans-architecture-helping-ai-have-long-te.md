# Google Titans architecture, helping AI have long-term memory

- Score: 363 | [HN](https://news.ycombinator.com/item?id=46181231) | Link: https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/

### TL;DR

Google presents Titans as a sequence architecture combining attention-based short-term context with a deep neural-network memory updated during inference. Gradient-based surprise selects information to learn, momentum carries recent relevance, and adaptive weight decay forgets stale material. MIRAS generalizes this into choices of memory structure, learning objective, retention rule, and optimizer. Google reports linear inference, gains over comparable Transformer++ and recurrent baselines, and recall beyond two million tokens. Commenters remain interested but question robustness to junk inputs and the absence of official pretrained weights or code.

### Comment pulse

- Surprise appears attackable → random anomalies might flood memory — counterpoint: training can teach embeddings to ignore irrelevant novelty.
- Publication is not reproducibility → eleven months after the paper, commenters found only unofficial implementations, without Google model weights or code.
- Open-research credit is shared → Chinese labs, Meta, ByteDance, and others also publish research or release working models.

### LLM perspective

- View: Test-time learned memory is promising, but deployment evidence trails architectural claims.
- Impact: Long-document, genomic, and time-series systems could gain scalable context without attention’s steep sequence-length costs.
- Watch next: Official checkpoints, independent BABILong replication, throughput measurements, memory-poisoning tests, and continual-learning stability.
