# Claude Code's source code has been leaked via a map file in their NPM registry

- Score: 1863 | [HN](https://news.ycombinator.com/item?id=47584540) | Link: https://twitter.com/Fried_rice/status/2038894956459290963

### TL;DR
An inadvertently published source map on Anthropic’s Claude Code NPM package exposed much of the tool’s internal TypeScript, including configuration and feature plumbing. Hacker News focuses less on “secret sauce” and more on what the leak reveals about real-world AI‑assisted coding: dense, sprawling functions, unconventional structure, and hidden feature flags. Commenters treat it as a mild but recurring operational mistake that nonetheless hands competitors roadmap clues and gives outsiders a rare look at how production AI devtools are actually built.  

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- NPM handling → Anthropic deprecated the package with an “Unpublished” message instead of unpublishing; 100‑download limit and “internet never forgets” make real removal impractical.  
- Roadmap exposure → Feature flags show unreleased assistant mode “kairos”, Tamagotchi‑style Buddy System, and Undercover mode; people even use Claude itself to mine the binary.  
- Code quality debate → A 3k‑line print function exemplifies gnarly internals—counterpoint: traditional metrics like nesting and cyclomatic complexity may misjudge LLM‑written, performance‑acceptable “vibe code.”  

---

### LLM perspective
- View: Source‑map leaks are predictable; CI/CD should auto‑scan artifacts for embedded source, secrets, and introspectable feature toggles.  
- Impact: Competitors gain design hints; engineers gain a benchmark of AI‑authored tooling, warts included, influencing expectations for commercial “agentic” products.  
- Watch next: Stronger NPM tooling, analyzers tuned for LLM‑generated code, and agents refactoring their own worst functions under human supervision.
