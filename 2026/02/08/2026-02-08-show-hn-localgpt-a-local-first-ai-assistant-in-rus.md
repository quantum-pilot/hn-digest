# Show HN: LocalGPT – A local-first AI assistant in Rust with persistent memory

- Score: 311 | [HN](https://news.ycombinator.com/item?id=46930391) | Link: https://github.com/localgpt-app/localgpt

### TL;DR

LocalGPT packages an OpenClaw-compatible assistant into a 27MB Rust binary requiring no Node.js, Python, or Docker. It stores MEMORY, SOUL, HEARTBEAT, and knowledge files locally as Markdown; SQLite FTS5, vector search, and local embeddings provide recall, while a daemon runs autonomous tasks. Users get CLI, web, desktop, and HTTP interfaces plus Anthropic, OpenAI, Ollama, and compatible endpoints. Commenters liked the smaller stack and persistent memory but disputed the name: state stays local, yet inference may be remote unless a local provider is configured. Others questioned differentiation, security, and LLM-written documentation.

### Comment pulse

- “Local” split readers: the sample uses Anthropic—counterpoint: Ollama or any compatible endpoint can keep inference on the user’s machine.
- OpenClaw already offers broader messaging and automation; replies valued a small non-Node core and saw feature sprawl without security boundaries as a liability.
- LLM-authored documentation drew criticism for low effort—counterpoint: maintainers argued generated docs are worthwhile when accurate and kept synchronized with code.

### LLM perspective

- View: Its contribution is a compact, inspectable local state layer; model locality remains a deployment choice, not an invariant.
- Impact: Users can own portable memory and interfaces while choosing model cost, privacy, latency, and quality independently.
- Watch next: Threat model, permission boundaries, encrypted memory, provider fallbacks, search quality, migration compatibility, resource use, and autonomous-task safety.
