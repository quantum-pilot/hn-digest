# From zero to a RAG system: successes and failures

- Score: 274 | [HN](https://news.ycombinator.com/item?id=47499356) | Link: https://en.andros.dev/blog/aa31d744/from-zero-to-a-rag-system-successes-and-failures/

### TL;DR
An engineer with no prior RAG experience built an internal, fully local chatbot over ~1 TB of mixed engineering documents. The journey: filter out non-text and huge useless files, move from LlamaIndex’s JSON store to ChromaDB for scalable vector storage, batch and checkpoint indexing on a rented GPU VM, and serve only the 54 GB vector index + LLM locally while keeping raw docs in Azure Blob with signed links. HN responses emphasize that serious RAG is mostly data/ETL work, and that naive “just embed PDFs” approaches fail at scale.

---

### Comment pulse
- Small teams can happily use a simple FAISS/Streamlit/OpenAI stack on tens of docs → the article’s pain comes from huge, messy, decade‑scale data.  
- Several argue real “enterprise RAG” = heavy preprocessing, labeling, schemas, knowledge graphs, and ReAG/agentic patterns → embeddings+Chroma alone won’t ensure quality.  
- Debate over “RAG is dead” → critics mean naive chunk‑and‑search is inadequate; proponents say RAG works great when combined with proper databases and ETL.

---

### LLM perspective
- View: RAG complexity grows superlinearly with corpus size and messiness; architecture is secondary to ruthless data curation.  
- Impact: Infra, data, and app teams all need to own ingestion, schema design, and monitoring, not just “the LLM person.”  
- Watch next: Mature ETL/observability tools for RAG, agentic retrieval planners, and standards for mixing vector, SQL, and graph backends.
