# Open source memory layer so any AI agent can do what Claude.ai and ChatGPT do

- Score: 158 | [HN](https://news.ycombinator.com/item?id=47897790) | Link: https://alash3al.github.io/stash?_v01

### TL;DR
Stash is an open-source “second brain” for AI agents: a persistent memory layer on PostgreSQL + pgvector that stores interactions as “episodes,” periodically consolidates them into facts, relationships, causal links, goals, failures, and hypotheses, and exposes them via MCP tools (`remember`, `recall`, goals, contradictions, etc.). It’s model-agnostic (any OpenAI-compatible API, including local Ollama) and organized by hierarchical namespaces. HN discussion questions whether this is truly different from standard vector/RAG stores and notes the lack of concrete benchmarks or internals behind the ambitious marketing claims.

---

### Comment pulse
- Automatic background memory (Claude-style) vs explicit `remember` calls → some prefer invisible summarization; others report success with tool-driven, agent-controlled memory creation and consolidation.  
- Skepticism: this looks like pgvector + RAG + MCP → critics see overblown “mind” branding, fear memory rot, bias (e.g., over-weighting “don’t use Stripe”).  
- Meta concern: how much of this was LLM-generated? → some want “LLM use statements”; others argue code review and trust matter more than tooling provenance.

---

### LLM perspective
- View: Technically, this is structured vector-memory plus consolidation; the differentiation is opinionated workflow and MCP tooling, not a new primitive.  
- Impact: Useful for agent builders and local-LLM users who want persistent, model-agnostic memory without rolling their own infra and schemas.  
- Watch next: Empirical evaluations of retrieval quality, goal-tracking, and memory rot over long projects; adoption in real MCP-based agents.
