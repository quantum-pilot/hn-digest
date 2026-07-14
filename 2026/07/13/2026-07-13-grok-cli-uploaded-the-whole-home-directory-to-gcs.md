# Grok CLI uploaded the whole home directory to GCS

- Score: 373 | [HN](https://news.ycombinator.com/item?id=48892468) | Link: https://twitter.com/a_green_being/status/2076598897779020159

### TL;DR
A user discovered the Grok CLI was automatically uploading their entire home directory to a Google Cloud Storage bucket. Comments clarify this was not the LLM “deciding” to read files, but a deliberate client design that bulk-uploads the current repo/directory, likely for semantic indexing. HN is broadly outraged: people argue this is indistinguishable from spyware, that “please-don’t-read” markdown files are meaningless for security, and that robust sandboxing or OS‑level controls are the only sane protection.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Grok CLI behavior is deterministic: it uploads the whole repo/home for vector indexing, not an emergent agent choice → seen as intentionally invasive design.  
- Markdown-based “do not read” instructions are security theater → use OS permissions, sandboxes, or containers; never trust in-band hints to constrain an agent.  
- Responsibility split: some say users must sandbox; others insist non-expert targets mean defaults must be safe and uploads opt‑in, not hidden—counterpoint: people will still ignore precautions.

---

### LLM perspective
- View: Treat AI dev tools like remote backup clients with code execution, not like text editors; demand explicit data-flow visibility.  
- Impact: Developer machines, corporate source code, and secrets become high-risk if tools auto-sync or scan directories without strict scoping.  
- Watch next: OS/IDE-native agent sandboxes, standardized “allowed paths” policies, and vendor transparency on what’s uploaded, when, and for what duration.
