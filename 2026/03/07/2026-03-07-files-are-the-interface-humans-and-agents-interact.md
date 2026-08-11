# Files are the interface humans and agents interact with

- Score: 167 | [HN](https://news.ycombinator.com/item?id=47286408) | Link: https://madalitso.me/notes/why-everyone-is-talking-about-filesystems/

### TL;DR

The essay argues that files are becoming the common interface for humans and agents: local, portable, auditable context that survives model windows and application churn. Markdown instructions and skills can interoperate without hundreds of specialized tools, while databases remain the substrate for concurrency, indexing, and semantic retrieval. This simplicity has limits: an ETH Zürich study found repository context files reduced success and raised inference costs over 20% when overloaded with requirements. HN favored boring open formats for durable ownership, but noted messy data still needs search, standards, and disciplined organization.

### Comment pulse

- Files preserve portability across short-lived SaaS products; sidecar edits and proprietary metadata still erase work during migrations.
- Plan 9 anticipated file-oriented composition and permissions — counterpoint: modern filesystems are graphs, not necessarily acyclic trees.
- Codebases are unusually curated; unstructured personal or business data lacks the discipline that makes agent traversal effective.

### LLM perspective

- **View:** Files win as a legible contract, while indexes and databases quietly supply scale underneath.
- **Impact:** Users can move memory and skills between agents; vendors lose lock-in unless formats deliberately diverge.
- **Watch next:** Minimal-context benchmarks, metadata portability, namespace conventions, permission models, and durable multi-agent write coordination.
