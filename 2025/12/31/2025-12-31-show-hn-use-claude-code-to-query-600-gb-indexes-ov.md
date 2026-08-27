# Show HN: Use Claude Code to Query 600 GB Indexes over Hacker News, ArXiv, etc.

- Score: 287 | [HN](https://news.ycombinator.com/item?id=46442245) | Link: https://exopriors.com/scry

### TL;DR

Alignment Scry exposes SQL, BM25 search, embeddings, and vector algebra over roughly 60 million documents and 600GB of indexes spanning arXiv, Hacker News, LessWrong, and other research sources. Claude translates nuanced questions into inspectable queries, with public access, estimates, limits, and semantic operations such as debiasing and centroids. HN users praised the auditable query-language interface and reported useful discoveries, but warned that recommending unrestricted Claude execution against internet-derived text invites prompt injection and that completeness, terminology drift, and marketing claims need scrutiny.

### Comment pulse

- SQL makes agent research inspectable → rigid queries expose filters and joins instead of treating the model as a database.
- Early users found relevant niche papers → practical friction included shell escaping, latency, and the default 100-result cap.
- Unrestricted execution is unsafe → ingested documents can contain prompt injections, demanding isolation despite stronger models.

### LLM perspective

- View: Constrained language translation is a stronger research pattern than opaque answer generation.
- Impact: Researchers can explore large corpora conversationally while retaining query-level reproducibility.
- Watch next: Measure retrieval completeness, cross-domain embedding leakage, sandboxing, and API abuse resistance.
