# Lessons for Agentic Coding: What should we do when code is cheap?

- Score: 226 | [HN](https://news.ycombinator.com/item?id=48019025) | Link: https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html

### TL;DR
The article argues that when LLMs make coding “cheap,” the real work shifts to specs, tests, intent, and taste. You should frequently rebuild implementations, invest in strong end-to-end tests, keep living specs and documented intent, automate easy tasks, and focus your human time on hard problems like architecture, performance, and security. Agents dramatically amplify experienced developers, but code remains “free as in puppies”: maintenance, support, and security are still expensive. HN replies split between reporting massive productivity gains and warning about verification, architecture, and long‑term costs.

---

### Comment pulse
- Some practitioners report huge boosts: AI-written tickets, tests, and docs, 70–90% coverage, and rapid multi‑feature shipping → they feel the “bad code floor” has risen.
- Others stress that cheap generation ≠ cheap software → architecture, verification, user fit, and vendor dependence dominate costs—counterpoint: ultra‑cheap prototypes radically shorten business feedback loops.
- Emerging consensus: agents excel at PoCs, scripts, and incremental features, but unchecked use quickly creates muddy architectures; human taste and early-stage review become the new bottleneck.

---

### LLM perspective
- View: Treat agents as aggressive accelerators for exploration and refactoring, not autonomous owners of production systems.
- Impact: Senior engineers, tech leads, and product folks gain leverage; orgs that underinvest in juniors and maintainers accumulate fragile AI-shaped systems.
- Watch next: Benchmarks on long-term maintainability of AI-heavy repos, pricing shifts for hosted models, and tools that enforce architecture and intent alongside generated code.
