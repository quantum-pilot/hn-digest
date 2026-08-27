# Production RAG: what I learned from processing 5M+ documents

- Score: 278 | [HN](https://news.ycombinator.com/item?id=45645349) | Link: https://blog.abdellatif.io/production-rag-processing-5m-documents

### TL;DR

A startup founder reports that production RAG improved after replacing tutorial-style defaults with multiple conversation-aware semantic and keyword queries, parallel retrieval followed by reranking, domain-specific chunking, metadata injection, and routing requests that should bypass retrieval. The lessons come from the author’s work on millions of pages, but the post also promotes an open-source product and supplies no controlled benchmark. Commenters add that hybrid dense and sparse search, explicit user context, and measurable business outcomes matter, while questioning the project’s “self-hosted” dependency footprint.

### Comment pulse

- Practitioners recommended query variants, BM25 plus dense retrieval, reciprocal-rank fusion, and reranking rather than one embedding search.
- Readers wanted evaluations tied to user success and clearer visibility into what context the system actually used.

### LLM perspective

- View: Retrieval quality is a pipeline and product-design problem, not a vector-database setting.
- Impact: Better routing and context visibility can prevent irrelevant retrieval while making failures easier to diagnose.
- Watch next: Demand reproducible evaluations, latency and cost data, and comparisons against simpler search baselines.
