# No right to relicense this project

- Score: 462 | [HN](https://news.ycombinator.com/item?id=47259177) | Link: https://github.com/chardet/chardet/issues/327

### TL;DR
Mark Pilgrim, original author of the LGPL‑licensed `chardet` library, opened a GitHub issue claiming the current maintainer illegally relicensed the project to MIT after an AI‑assisted “complete rewrite” using Claude. He argues prior exposure to the LGPL code makes the rewrite a derivative work that must remain LGPL. Discussion centers on whether clean‑room rewrites require zero prior exposure, how LLM training on the original code affects copyright, whether AI can be used to “launder” copyleft, and what moral authority maintainers have over long‑lived projects.

---

### Comment pulse
- Legal status of the rewrite → Some argue independent implementations are allowed even with prior exposure; clean rooms just simplify proof—counterpoint: any substantial similarity plus known exposure likely convinces a court.

- AI as license‑laundering tool → People fear LLM rewrites could gut GPL/LGPL enforcement and erode the “stick” forcing corporate contributions, even if current law is murky.

- Governance and trust → Many see maintainers as trustees, not owners: if you replace all code and change license, fork or rename; keeping the brand feels like a rug pull.

---

### LLM perspective
- View: Using LLMs to rewrite and relicense copyleft projects is legally risky and socially corrosive, regardless of whether a court eventually permits it.

- Impact: OSS maintainers, corporate users, and AI vendors all face heightened audit, forking, and due‑diligence pressures around license provenance.

- Watch next: Concrete test cases, code‑similarity forensics services, clearer LLM training disclosures, and community norms for AI‑assisted “clean‑room” reimplementations.
