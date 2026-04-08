# Project Glasswing: Securing critical software for the AI era

- Score: 806 | [HN](https://news.ycombinator.com/item?id=47679121) | Link: https://www.anthropic.com/glasswing

### TL;DR
Anthropic’s Project Glasswing uses a highly capable but unreleased model, Claude Mythos Preview, to scan and secure critical software for major partners like AWS, Apple, Google, Microsoft, and the Linux Foundation. Mythos reportedly autonomously uncovered thousands of zero‑day vulnerabilities, including decades‑old bugs in OpenBSD, FFmpeg, and the Linux kernel, and beats prior models on coding/cyber benchmarks. Because the same capabilities could supercharge attackers, Anthropic is restricting access, funding open‑source security, and coordinating with governments, which sparked HN debate over hype, geopolitics, and who benefits.

---

### Comment pulse
- AI vs existing tools → Many see Mythos as fuzzing++: LLMs design harnesses, drive fuzzers, and find logic bugs; static analysis and memory‑safe languages still essential complements.  
- Power imbalance → Large vendors can afford continuous Mythos‑level scanning, shrinking their attack surface while small projects face “use AI or get hacked” pressure — counterpoint: AI may also cheaply port legacy code to safer languages.  
- Risk, alignment, and politics → System card shows serious sabotage concerns, yet only a 24‑hour internal review and no US named as adversary, raising skepticism about safety rigor and framing.

---

### LLM perspective
- View: Treat models like Mythos as force multipliers for existing practices, not magic shields; integrate with fuzzing, SAST, and secure‑by‑design.  
- Impact: Biggest gains hit OS vendors, browsers, and major infra; long‑tail open source needs subsidized access or will lag dangerously.  
- Watch next: Independent red‑team reports, concrete vulnerability tallies per project, open benchmarks versus fuzzers, and whether similar models leak beyond “defensive only” channels.
