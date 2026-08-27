# Launch HN: Airweave (YC X25) – Let agents search any app

- Score: 127 | [HN](https://news.ycombinator.com/item?id=45427482) | Link: https://github.com/airweave-ai/airweave

### TL;DR

Airweave is an MIT-licensed platform that synchronizes more than 25 applications, databases, and document stores into semantically searchable knowledge bases for agents. It exposes search through REST or MCP and handles authentication, extraction, transformation, embeddings, incremental updates, and versioning. Users can run a managed service or self-host a stack built around FastAPI, PostgreSQL, Qdrant, React, and Docker. Airweave says it always indexes source data; current permission isolation generally relies on per-user syncs, with unified organization-level ACL synchronization planned.

### Comment pulse

- Permission mapping dominated discussion, especially public links, shared files, and context-dependent confidentiality.
- Airweave said per-user synchronization limits leakage today, accepting duplication until unified ACL support arrives.
- The team confirmed it indexes everything rather than choosing between cached search and live tool calls.

### LLM perspective

- View: Connector breadth is secondary to faithfully reproducing each source’s evolving access-control semantics.
- Impact: Central indexing improves agent recall but creates another persistent copy and a concentrated disclosure boundary.
- Watch next: Test revocation latency, ACL fidelity, audit trails, deletion, encryption, and cross-tenant isolation before sensitive use.
