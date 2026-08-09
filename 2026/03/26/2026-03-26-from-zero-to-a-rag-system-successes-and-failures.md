# From zero to a RAG system: successes and failures

- Score: 274 | [HN](https://news.ycombinator.com/item?id=47499356) | Link: https://en.andros.dev/blog/aa31d744/from-zero-to-a-rag-system-successes-and-failures/

### TL;DR

An engineer built a confidential RAG assistant over 451GB of company documents. Filtering useless formats cut file count 54%; batches of 150 files written into ChromaDB avoided LlamaIndex memory crashes and enabled checkpoints. An RTX 4000 SFF Ada VM finished indexing in two to three weeks for €184, producing 738,470 vectors and a 54GB index. Ollama generates answers with document references, while originals remain in Azure behind generated SAS links. HN praises the scale but says production quality needs structured preprocessing, evaluation, and authoritative databases—not vector search alone.

### Comment pulse

- €184 of compute is trivial beside several engineer-weeks → optimization effort and data preparation dominate total cost.
- Ingestion determines quality → conversion, metadata, temporal labels, failure handling, and user feedback matter more than a turnkey vector store.
- Similarity is not universal retrieval → exact prices or current facts belong in authoritative databases, potentially combined with agentic search.

### LLM perspective

- **View:** This is a strong ingestion case study, but no measured answer-quality evaluation supports its reliability claim.
- **Impact:** Small corpora can start simply; large archives need resumability, observability, tiered storage, and schema-aware retrieval.
- **Watch next:** Retrieval benchmarks, citation correctness, stale-document handling, permissions, incremental updates, and failed-file coverage.
