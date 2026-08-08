# High Performance Git

- Score: 226 | [HN](https://news.ycombinator.com/item?id=47929035) | Link: https://gitperf.com/

### TL;DR

Ted Nyman’s free book treats Git as a content-addressed database, cache, graph walker, and transport system, then maps performance costs across those layers. Its 21 chapters cover objects, refs, history traversal, packfiles, indexes, commit graphs, maintenance, sparse checkouts, partial clones, large repositories, protocols, instrumentation, tuning, and recovery. The intended readers are monorepo, CI, build, and developer-experience engineers troubleshooting scale. The author released Edition 1.1 and plans practical adoption guidance. HN readers praised the internals-first approach, though some objected to prose they perceived as LLM-generated.

### Comment pulse

- Some recommend learning Git’s core objects and refs before porcelain commands because internals make behavior easier to reason about.
- A Windows user attributes chained-command slowness to Unix-tool process overhead; WSL reportedly avoids it.
- Critics called the writing synthetic — counterpoint: others found the technical explanations informative despite stylistic “LLMisms.”

### LLM perspective

- Instrument first, identify the slow layer, then select sparse, maintenance, storage, or transport remedies.
- Adoption chapters should include rollout safety, version requirements, and reversible defaults.
- Agent-generated commit volume will test ref scale, metadata hygiene, and maintenance scheduling.
