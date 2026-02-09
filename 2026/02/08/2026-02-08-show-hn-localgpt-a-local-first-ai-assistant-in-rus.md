# Show HN: LocalGPT – A local-first AI assistant in Rust with persistent memory

- Score: 311 | [HN](https://news.ycombinator.com/item?id=46930391) | Link: https://github.com/localgpt-app/localgpt

### TL;DR
LocalGPT is a Rust-based, “local-first” AI assistant packaged as a ~27 MB single binary with CLI, web, and desktop UIs. It stores long-term memory, tasks, and personality in Markdown files indexed via SQLite FTS5 plus local embeddings for semantic search, and exposes an HTTP API and background “heartbeat” for autonomous work. It talks to any OpenAI/Anthropic-compatible endpoint, including local Ollama, but the default Anthropic example triggered debate about the name “LocalGPT” being misleading and overlap with the more feature-rich OpenClaw project.

---

### Comment pulse
- Name and scope criticism → Not truly “local” or a GPT; depends on external LLMs by default, and overlaps heavily with OpenClaw’s architecture and formats. — counterpoint: Can point at localhost Ollama or LAN models; remote keys are optional.

- Docs authenticity debate → Some dislike obvious LLM-written docs as lazy and low-effort; others argue LLMs are ideal for accurate, maintainable documentation and don’t see a problem.

- OpenClaw vs LocalGPT → Critics see “me too” clone; supporters value a smaller, non-Node, Rust binary and call for tighter security boundaries than OpenClaw’s powerful, sprawling setup.

---

### LLM perspective
- View: The real innovation is a clean, file-based memory layer plus Rust tooling around any LLM backend, not the model itself.

- Impact: Appeals to developers wanting lightweight, scriptable agents and organizations needing on-disk auditability and easier data-locality control.

- Watch next: Clear benchmarks on local vs cloud backends, stronger sandboxing/credential isolation, and a more accurate name/positioning relative to OpenClaw.
