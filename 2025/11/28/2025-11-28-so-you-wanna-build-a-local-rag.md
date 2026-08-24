# So you wanna build a local RAG?

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46080364) | Link: https://blog.yakkomajuri.com/blog/local-rag

### TL;DR

Skald replaced each cloud component in its retrieval pipeline with local software: Postgres plus pgvector, configurable Sentence Transformers embeddings and rerankers, Docling parsing, and GPT-OSS 20B through llama.cpp. On eleven PostHog questions, cloud Voyage and Claude averaged 9.45, while fully local English models scored 7.10 and multilingual models 8.63. Point lookups worked; multilingual queries and evidence scattered across many documents exposed weaknesses. Commenters urged stronger evals, contextual chunking, and comparisons with lexical or hybrid search.

### Comment pulse

- Plain-text search can simplify RAG → agent-driven BM25 or ripgrep avoids embeddings and chunk indexes — counterpoint: repeated searches increase latency.
- Hybrid retrieval often balances strengths → lexical matching preserves exact terms while embeddings recover semantically related passages.
- The benchmark is directional, not definitive → eleven author-scored questions cannot establish general model or database superiority.

### LLM perspective

- View: Local RAG is viable, but retrieval design matters more than merely replacing each hosted API.
- Impact: Privacy-sensitive organizations gain deployable options while accepting model hosting, evaluation, and multi-document recall work.
- Watch next: Larger held-out datasets, citation recall, latency, semantic-context chunking, hybrid baselines, and alternative embedding models.
