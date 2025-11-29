# So you wanna build a local RAG?

- Score: 175 | [HN](https://news.ycombinator.com/item?id=46080364) | Link: https://blog.yakkomajuri.com/blog/local-rag

### TL;DR
Skald describes how they built a fully local, privacy‑preserving RAG stack using open‑source components (pgvector, sentence‑transformers, Docling, GPT‑OSS) and compare it to a cloud setup using Voyage + Claude. On a small but realistic PostHog docs benchmark, semi‑local and fully local systems come within ~1–2 points of the cloud baseline, mainly struggling with multilingual queries and answers requiring aggregation across many documents. HN discussion focuses on when semantic search actually beats lexical, hybrid search strategies, and better retrieval/eval practices.

---

### Comment pulse
- Lexical search + an LLM “search agent” can avoid vectors and chunking, staying cheaper and simpler — counterpoint: multiple search rounds can hurt latency badly.  
- Semantic isn’t automatically better; user queries differ from dev tests. Hybrid BM25 + embeddings often wins when users don’t know the exact terminology.  
- Retrieval quality hinges on chunking and contextualization; commenters seek standard eval datasets and experiment with other embeddings (nomic, Qwen) and light vector stores like sqlite‑vec.

---

### LLM perspective
- View: Many teams should start with hosted RAG, then progressively replace individual components with local/open‑source ones as needs and skills grow.  
- Impact: Small, domain‑specific eval sets will be crucial for choosing between “good enough” local models versus expensive frontier APIs.  
- Watch next: Packaged contextual retrieval and multi‑document aggregation techniques will likely ship as defaults, reducing today’s gap for complex queries in local stacks.
