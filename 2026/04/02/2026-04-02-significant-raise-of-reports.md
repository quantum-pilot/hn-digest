# Significant raise of reports

- Score: 272 | [HN](https://news.ycombinator.com/item?id=47611921) | Link: https://lwn.net/Articles/1065620/

### TL;DR
Linux kernel security maintainers report a step-change in valid bug reports—now 5–10 per day—driven largely by automated/AI tools. Many issues are duplicates, suggesting multiple scanners converging on the same long‑standing bugs and flushing a backlog faster than new bugs are written. This volume is forcing triage-only workflows, weakening the case for embargoes, and reinforcing the view that “security bugs are just bugs” and users must regularly update. HN debates practicality of constant updating, effects on embedded/IoT, and whether pre‑2000 software was genuinely higher quality or just simpler and better tested.

### Comment pulse
- Treat security bugs as normal bugs → AI makes exploitability classification hard; LTS mitigates upgrade risk — counterpoint: users reasonably prioritize only remote-code-execution‑class issues.  
- Current surge in findings → seen as backlog flush from decades-old code; strong push to use similar tools pre‑merge and to relax embargoes.  
- For offline appliances, release‑and‑forget remains valid; but internet‑connected, complex software needs sustained maintenance, unlike the CD era despite stronger QA then.

### LLM perspective
- View: AI scanners turning security into an operations and triage problem, eroding reliance on secrecy and one-off heroic patch cycles.  
- Impact: Large projects will normalize “always updating,” shorter support horizons, and mandatory automated analysis in contribution pipelines.  
- Watch next: Data on embargo reductions, duplicate-report rates, AI-found vs human-found exploit chains, and practices that embedded vendors adopt or resist.
