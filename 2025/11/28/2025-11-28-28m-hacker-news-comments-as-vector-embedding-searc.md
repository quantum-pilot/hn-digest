# 28M Hacker News comments as vector embedding search dataset

- Score: 295 | [HN](https://news.ycombinator.com/item?id=46081053) | Link: https://clickhouse.com/docs/getting-started/example-datasets/hackernews-vector-search-dataset

## TL;DR
ClickHouse released a ready-made vector-search dataset of ~28.7M Hacker News posts/comments with 384‑dim embeddings (all-MiniLM-L6-v2), plus full docs: create a MergeTree table, load from S3 Parquet, build an HNSW-based `vector_similarity` index, and run cosine-distance ANN queries. They also show a simple RAG demo: retrieve semantically relevant HN text and summarize it with LangChain + OpenAI. HN discussion centers on better modern embedding models, legal/privacy issues under YC’s terms, and ideas for HN-native semantic search features.

---

## Comment pulse
- MiniLM is viewed as legacy; commenters suggest newer open embedding models with longer context, but note license landmines, larger sizes, and mixed benchmark experiences.  
- YC’s terms are cited as forbidding scraping, commercial use, and derivative works of HN content, implying embeddings may violate policy — counterpoint: personal “memory prostheses” feel justifiable.  
- People want HN features like “similar sentences” or semantic threads; others mention existing third-party semantic search and risks of deanonymization via stylometric embeddings.

---

## LLM perspective
- View: Pre-embedded community forums are becoming standard playgrounds for RAG/vector-search, but consent, licensing, and user control are unresolved.  
- Impact: Engineers gain realistic, large-scale data to tune ANN indices, query plans, and end-to-end RAG stacks without building pipelines from scratch.  
- Watch next: More clearly licensed text corpora with opt-out mechanisms, plus empirical UX studies comparing BM25 vs semantic retrieval for discussion forums.
