# Don't classify, hallucinate

- Score: 230 | [HN](https://news.ycombinator.com/item?id=49249523) | Link: https://softwaredoug.com/blog/2026/08/10/hypothetical-classifications

### TL;DR

For classification against hundreds of labels, the author proposes omitting the full schema from every prompt. A cheap model invents a plausible taxonomy-style label, which is embedded and matched by dot product to precomputed embeddings of the real vocabulary. For a Wayfair query, “Furniture / Living Room / Tables / Coffee” resolves to the correct coffee-table category. The method cuts prompt cost but is slightly less accurate than sending vocabulary to a larger model. Commenters questioned whether directly embedding the query or reranking nearby real labels would be simpler.

### Comment pulse

- Supporters compare the method to forming a human approximation before locating the official term; related clustering workflows still need review.
- Critics see an unnecessary error stage—counterpoint: label-shaped generation can align better than raw queries, especially when separating attributes from item types.

### LLM perspective

- View: This is retrieval-oriented candidate generation, not unconstrained classification; the invented label translates intent into taxonomy-like language.
- Impact: Large-schema systems can reduce prompt tokens and use smaller models, accepting another measurable source of error.
- Watch next: Compare query embeddings, hypothetical labels, top-N reranking, latency, cost, rare-category recall, taxonomy drift, and human escalation.
