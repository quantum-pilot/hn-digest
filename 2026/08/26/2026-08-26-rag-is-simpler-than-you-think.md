# RAG Is Simpler Than You Think

- Score: 427 | [HN](https://news.ycombinator.com/item?id=49445727) | Link: https://www.lighthousenewsletter.com/p/rag-is-simpler-than-you-think

### TL;DR

The article argues retrieval-augmented generation should begin with BM25 or database full-text search, then add LLM query rewriting, sparse-plus-dense reranking, on-demand embeddings, hot/cold caches, or complete vector indexes only when measured needs justify them. Freshness, churn, query semantics, traffic, latency, and team skills determine the rung. HN practitioners largely agreed that embeddings are overestimated: exact search remains portable, debuggable, and effective, while ingestion quality, structured data, evaluation, query construction, and document design often matter more than fashionable vector infrastructure.

### Comment pulse

- Full-text search covers most practical retrieval → exact terms, SQL, synonyms, and tuned indexes scale with less operational burden than vectors.
- RAG remains information retrieval with an LLM participant → good extraction, structure, recall, precision, benchmarks, and documentation determine whether context is useful.
- Optimization often yields diminishing returns → corpus-specific pipelines can become elaborate — counterpoint: regulated or mixed factual systems genuinely need modular routing.

### LLM perspective

- View: Retrieval quality improves fastest when teams treat embeddings as one ranking component, not an automatic replacement for search engineering.
- Impact: Smaller teams can ship maintainable systems sooner while preserving freshness, observability, and straightforward failure diagnosis.
- Watch next: Establish query-level evals before adding semantic reranking, then measure quality, latency, reindexing cost, and model-switching risk.
