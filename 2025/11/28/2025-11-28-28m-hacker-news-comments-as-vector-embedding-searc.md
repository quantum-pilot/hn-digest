# 28M Hacker News comments as vector embedding search dataset

- Score: 295 | [HN](https://news.ycombinator.com/item?id=46081053) | Link: https://clickhouse.com/docs/getting-started/example-datasets/hackernews-vector-search-dataset

### TL;DR

ClickHouse offers 28.74 million Hacker News posts and comments in one Parquet file, each paired with a 384-dimensional all-MiniLM-L6-v2 embedding. Its guide covers loading the rows, building an HNSW cosine-similarity index, querying with locally generated vectors, and feeding retrieved text into a summarizer. HN readers welcomed semantic discovery but questioned the aging 512-token model, licensing and commercial-use terms, deletion rights, and privacy risks from identifying authors or alternate accounts through writing style.

### Comment pulse

- Newer embedders promise better retrieval → commenters favored EmbeddingGemma, Qwen3, BGE, or Nomic, while noting license, speed, and download-size tradeoffs.
- Semantic links could surface repeated debates → readers suggested similar-sentence and thread views might improve context — counterpoint: stylistic matching can expose pseudonymous accounts.
- Dataset reuse may violate site terms → readers cited derivative-work and scraping restrictions — counterpoint: others defended personal semantic archives as memory aids.

### LLM perspective

- View: Search quality depends as much on corpus governance as index performance.
- Impact: Researchers can prototype large-scale retrieval without funding a new embedding run.
- Watch next: Modern-model benchmarks, BM25 hybrids, removal workflows, license analysis, and deanonymization tests.
