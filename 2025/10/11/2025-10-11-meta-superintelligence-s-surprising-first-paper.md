# Meta Superintelligence's surprising first paper

- Score: 222 | [HN](https://news.ycombinator.com/item?id=45553577) | Link: https://paddedinputs.substack.com/p/meta-superintelligences-surprising

### TL;DR

The reviewed REFRAG paper proposes reducing retrieval-augmented generation costs by representing most retrieved 128-token chunks as single projected embeddings that a modified language model can consume directly. A lightweight policy, trained under an expansion budget, selects the few chunks restored to full tokens. The paper reportedly preserves benchmark perplexity and task accuracy while cutting attention and KV-cache work, with claims of up to 30-fold faster time to first token. Production adoption would require model adaptation, encoder and policy training, embedding refresh pipelines, and careful testing for precision-sensitive tasks.

### Comment pulse

- Readers debated whether the paper reflects Meta’s new lab direction or merely research completed before its reorganization.
- Discussion questioned institutional incentives, research autonomy, and pressure for near-term business returns.

### LLM perspective

- View: REFRAG treats retrieved text as an inefficient interchange format when models can consume aligned representations directly.
- Impact: Successful deployment could improve RAG latency and capacity without buying more inference hardware.
- Watch next: Reproducible implementations, quality under aggressive compression, changing corpora, and exact-quotation workloads.
