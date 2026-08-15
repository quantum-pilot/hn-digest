# Introducing Toast 1

- Score: 197 | [HN](https://news.ycombinator.com/item?id=49299746) | Link: https://www.mixedbread.com/blog/toast-1

### TL;DR

Mixedbread launched Toast 1, a specialized retrieval agent that decomposes questions, iterates over search, inspects sources, and returns curated evidence to a general model. It works with any backend but is optimized for Mixedbread Search. Company evaluations report GPT-5.6 Sol plus Toast reaching 70% on OfficeQA Pro V2 for about $1.15 per task, and matching legal-benchmark quality with 3.5 times fewer tokens than vanilla search. Standalone queries reportedly cost $0.016–$0.023 with eight-second median latency. Commenters welcomed specialization but requested broader comparisons and open weights.

### Comment pulse

- Supporters see multi-round search as an obvious specialized-model role, especially over difficult internal knowledge collections.
- Skeptics ask when it beats smaller models or conventional RAG—counterpoint: Mixedbread says index quality plus specialization drives substantial uplift.

### LLM perspective

- View: Separating evidence gathering from synthesis can conserve frontier-model context while making retrieval behavior independently measurable.
- Impact: Legal, financial, and enterprise-search teams could lower agent costs without migrating existing indexes.
- Watch next: Independent benchmarks, backend-agnostic results, source-quality errors, competing search-agent comparisons, and post-launch pricing will test the claims.
