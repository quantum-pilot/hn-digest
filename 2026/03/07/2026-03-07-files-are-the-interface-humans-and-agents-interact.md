# Files are the interface humans and agents interact with

- Score: 167 | [HN](https://news.ycombinator.com/item?id=47286408) | Link: https://madalitso.me/notes/why-everyone-is-talking-about-filesystems/

### TL;DR
The piece argues that AI agents are converging on the filesystem as their main interface: instead of dozens of bespoke tools and APIs, agents read and write ordinary files (code, markdown, CSV) on your machine, using them as persistent memory and shared context. Standards like SKILL.md and simple files like `aboutme.md` or `CLAUDE.md` become the real “API” between tools. Databases still matter as scalable substrates, but files win as the human/agent boundary and as a portable, user-owned format for personal computing.

---

### Comment pulse
- Durable, boring file formats → safeguard data across decades and tools; SaaS that traps meaning in proprietary schemas creates catastrophic technical debt.  
- Plan 9 nostalgia → its “everything is a file” and 9P ideas match agent orchestration needs; also, filesystems are graphs, not trees.  
- Filesystems excel for code-like, curated data → messy corpora still need search/indices; UIs may go multimodal, but text input remains crucial for clear thinking.

---

### LLM perspective
- View: Treat files as contracts: short, precise constraints and skills, not bloated onboarding documents that mislead agents.  
- Impact: Developer tooling, CLIs, and agent frameworks can interoperate cheaply by converging on a few markdown-based conventions.  
- Watch next: Benchmarks comparing “filesystem-only + light indices” vs classic RAG stacks across codebases, docs, and truly messy enterprise data.
