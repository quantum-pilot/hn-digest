# We replaced RAG with a virtual filesystem for our AI documentation assistant

- Score: 203 | [HN](https://news.ycombinator.com/item?id=47618223) | Link: https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant

## TL;DR
Mintlify’s docs assistant originally used RAG over embeddings plus sandboxed containers with a real filesystem, which was slow (~46s boot) and expensive. They built ChromaFs: a virtual, read‑only filesystem backed by their existing Chroma DB, exposed through a TypeScript bash emulator. Shell commands (`ls`, `cat`, `grep`, etc.) become DB queries, with a precomputed path tree, per-user access filtering, page reassembly from chunks, and a two-stage grep (DB coarse filter + in‑memory fine filter), cutting startup to ~100ms and near-zero marginal cost. HN debates whether this is clever pragmatism or a reinvention of decades-old search/database ideas.

---

## Comment pulse
- Filesystem hierarchies as semantic structure → directory trees are human-curated knowledge graphs agents can traverse, often beating noisy embedding-based RAG on large codebases and docs.  
- This is old-school IR with lipstick → databases and search engines already support hierarchy, ACLs, full-text and vector search—counterpoint: agents empirically behave better with familiar file/CLI metaphors.  
- Architecture debate → some see overengineering and multi-step latency; others propose FUSE-backed VFS, while the author argues FUSE was slower and added infra overhead.

---

## LLM perspective
- View: Letting agents “think” in familiar shells/filesystems reduces tool-use confusion versus bespoke APIs or opaque vector-only retrieval.  
- Impact: Lower latency, cheaper infra, and better multi-file reasoning for docs and code assistants; weaker benefits for highly unstructured corpora.  
- Watch next: Benchmarks comparing agent task success on vector-RAG vs filesystem/DB hybrids; generalized “agentic search” APIs beyond POSIX metaphors.
