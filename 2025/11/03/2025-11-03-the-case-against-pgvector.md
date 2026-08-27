# The Case Against PGVector

- Score: 345 | [HN](https://news.ycombinator.com/item?id=45798479) | Link: https://alex-jacobs.com/posts/the-case-against-pgvector/

### TL;DR

The author argues that pgvector’s apparent simplicity conceals production tradeoffs: IVFFlat needs tuning and periodic rebalancing, HNSW can impose heavy build and insertion costs, and filtered nearest-neighbor queries complicate planning and recall. Hybrid search and operational strategies may also require custom work. The recommendation is to consider a managed vector database when those costs exceed the benefit of keeping data in PostgreSQL. Commenters strongly contested the generalization, citing large production deployments, iterative scans, concurrent reindexing, memory controls, quantization, and newer PostgreSQL extensions.

### Comment pulse

- Discourse reported pgvector use across thousands of databases and said version 0.8 iterative scans address an important filtering complaint.
- Others stressed that separate vector services introduce synchronization, consistency, joining, and operational costs of their own.

### LLM perspective

- View: The useful conclusion is workload-specific evaluation, not that either PostgreSQL or specialized databases universally win.
- Impact: Teams can incur hidden costs through premature specialization or by stretching PostgreSQL beyond their expertise.
- Watch next: Benchmarks using actual filters, update rates, recall targets, scale, and managed-service constraints.
