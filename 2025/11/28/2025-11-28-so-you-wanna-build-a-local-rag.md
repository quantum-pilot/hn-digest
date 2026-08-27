# So you wanna build a local RAG?

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46080364) | Link: https://blog.yakkomajuri.com/blog/local-rag

### TL;DR

Skald's local RAG stack replaces cloud services with Postgres plus pgvector, Sentence Transformers embeddings and reranking, Docling parsing, and a separately managed GPT-OSS 20B server. In a small, explicitly non-scientific PostHog test, cloud Voyage and Claude scored 9.45; default local retrieval scored 7.10; multilingual local models reached 8.63. Point queries worked well, while ambiguity, other languages, and multi-document aggregation exposed weaknesses. Commenters advocated lexical or hybrid search and representative retrieval evaluations before assuming embeddings win.

### Comment pulse

- Lexical search can be simpler and cheaper → counterpoint: repeated agent searches add latency and miss paraphrased concepts.
- Hybrid ranking combines exact terms with semantic recall → suitability depends on actual user language and corpus structure.
- Evaluation design dominates reported quality → developers who know the corpus may write unrealistically keyword-rich questions.

### LLM perspective

- View: Local RAG is operationally feasible, but retrieval design—not merely the chosen LLM—sets its failure envelope.
- Impact: Privacy-sensitive teams trade API dependence for model hosting, evaluation, parsing, indexing, and tuning responsibilities.
- Watch next: Publish larger blinded benchmarks covering retrieval recall, answer faithfulness, latency, languages, and multi-document synthesis.
