# We replaced RAG with a virtual filesystem for our AI documentation assistant

- Score: 203 | [HN](https://news.ycombinator.com/item?id=47618223) | Link: https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant

### TL;DR

Mintlify did not discard its vector database so much as replace one-shot top-K retrieval with an agent-browsable virtual filesystem over Chroma. ChromaFs uses just-bash to expose `ls`, `find`, `cat`, and optimized `grep`; it keeps the directory tree in memory, reconstructs pages from stored chunks, applies per-user path filtering, and remains read-only. This cut p90 session startup from roughly 46 seconds for cloned sandboxes to about 100 milliseconds, with claimed zero marginal compute. HN liked familiar hierarchy but disputed the “RAG replacement” framing and warned each browsing step adds model latency.

### Comment pulse

- Directory structure acts as a human-curated knowledge graph, helping agents navigate by concepts learned from code and shell-heavy training data.
- Databases can already combine hierarchy, keywords, BM25, vectors, and filters; commenters framed agent-controlled ad hoc querying as the real advance.
- FUSE seemed more natural — counterpoint: the author found it slow, unnecessary for limited read-only commands, and dependent on added sandbox infrastructure.

### LLM perspective

- **View:** This is an interface and control-loop redesign atop existing retrieval storage, not the elimination of retrieval augmentation.
- **Impact:** Documentation agents gain exact lookup, whole-page context, and RBAC-aware exploration without per-session machines.
- **Watch next:** End-to-end answer accuracy, time-to-first-answer, tool-call counts, cache invalidation, authorization leakage tests, and hybrid-search comparisons.
