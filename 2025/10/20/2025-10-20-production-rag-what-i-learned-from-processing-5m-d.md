# Production RAG: what I learned from processing 5M+ documents

- Score: 278 | [HN](https://news.ycombinator.com/item?id=45645349) | Link: https://blog.abdellatif.io/production-rag-processing-5m-documents

- TL;DR
  - After scaling RAG from 100-doc prototypes to 5M+ docs, the biggest wins were: multi-query generation per thread, aggressive reranking (50→15), domain-aware chunking, injecting metadata, and routing non-RAG asks to APIs. Stack evolved to Turbopuffer, text-embedding-large-3, and Zerank; open-sourced the approach. HN debates “self-hosted” vs third‑party dependencies, endorses multi-query + hybrid BM25/RRF (or SPLADE), notes LLM rerankers’ cost, and urges search‑centric UIs and measurable business outcomes.

- Comment pulse
  - “Self-hosted” ≠ zero dependencies → running your code while using third‑party services is acceptable; air‑gapped orgs need offline stacks — counterpoint: OSS needn’t support that.
  - Multi-query + hybrid retrieval + RRF → fixes poor user queries and technical terms; consider SPLADE; show users the interpreted intent — counterpoint: cloud RAG vendors should handle this.
  - LLM rerankers excel but are costly → inject metadata; route non‑RAG tasks; favor search‑oriented UIs; ask for proof of efficiency gains.

- LLM perspective
  - View: Treat RAG as retrieval engineering; prioritize query generation, reranking, chunking. Swapping DBs/LLMs rarely rescues quality.
  - Impact: Enterprise teams cut errors but increase latency/cost; product shifts from chat to transparent search improve trust.
  - Watch next: Reranker/chunking benchmarks, SPLADE vs hybrid head‑to‑head, S3 Vectors/Bedrock KB GA, agentset adoption metrics.
