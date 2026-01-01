# Show HN: Use Claude Code to Query 600 GB Indexes over Hacker News, ArXiv, etc.

- Score: 287 | [HN](https://news.ycombinator.com/item?id=46442245) | Link: https://exopriors.com/scry

- TL;DR  
  - A public ExoPriors/“Scry” API lets Claude generate and run SQL + vector-search queries over ~600 GB of AI-alignment–adjacent text (HN, arXiv, LessWrong, etc.).  
  - Users interact in natural language; Claude turns this into BM25 and pgvector queries, with named embeddings and vector algebra (mixing, debiasing, centroids) for nuanced concept search.  
  - Early adopters report real research wins (e.g., string-theory literature review), while HN discusses security (prompt injection, permissions), semantic drift, and hype vs. substance in the marketing.

- Comment pulse  
  - NL→SQL via LLM is praised as the right pattern: LLM as query compiler, not knowledge base—counterpoint: vector meaning varies by domain and model quality.  
  - Real-world test: a physics project quickly surfaced key arXiv papers, built topic indexes, but hit 100-result caps and mildly slow (5–15s) responses.  
  - Pushback on suggesting `--dangerously-skip-permissions` to non-devs; commenters stress sandboxing against prompt injection and untrusted remote content.

- LLM perspective  
  - View: Treating LLMs as programmable query planners over rich indices looks robust and composable compared to opaque chatbot-style RAG.  
  - Impact: Researchers and power users gain “literature IDEs” where complex, cross-source questions become reproducible SQL/vector workflows.  
  - Watch next: Better permission models, per-domain embeddings, and expansion into under-indexed domains like biomedical supplements and private corpora.
