# Building a Simple Search Engine That Works

- Score: 250 | [HN](https://news.ycombinator.com/item?id=45950720) | Link: https://karboosx.net/post/4eZxhBon/building-a-simple-search-engine-that-actually-works

### TL;DR

The author builds application search inside an existing relational database by tokenizing documents and queries identically. Exact words, prefixes, and character n-grams receive different weights; field importance and token length further shape scores. Two tables connect weighted tokens to documents, batch inserts rebuild changed entries, and SQL ranking rewards diverse matches while penalizing long documents. A minimum-weight filter suppresses results based only on noisy n-grams, with a lower-threshold fallback. The design is controllable and dependency-light, but comments stress that scale, ambiguous intent, and adversarial content quickly exceed this approach.

### Comment pulse

- Practitioners considered database-backed search suitable for a site corpus but warned it can fail far below web-scale collections.
- Ranking quality requires continual empirical tuning, while typo correction, taxonomy, and SEO resistance expand the problem substantially.

### LLM perspective

- View: This is a pragmatic search component, not evidence that general information retrieval is simple.
- Impact: Keeping ranking explicit and local can outperform an opaque dependency for bounded, stable corpora.
- Watch next: Corpus size, query logs, latency, relevance judgments, index growth, and adversarial documents.
