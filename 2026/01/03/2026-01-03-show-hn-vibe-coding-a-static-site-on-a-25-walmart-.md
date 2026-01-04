# Show HN: Vibe Coding a static site on a $25 Walmart Phone

- Score: 60 | [HN](https://news.ycombinator.com/item?id=46480677) | Link: https://stetsonblake.com/%2425+Walmart+Phone+for+Hackers

### TL;DR
A hacker turned a $25 Walmart Android phone (Moto G 2025) into a pocket Linux server using Termux and optionally Andronix/proot. The phone runs SSH, a static website, and can host other services (Prometheus, Grafana, Minecraft, self‑hosted APIs). The article walks through installing Termux from F‑Droid, enabling SSH on port 8022, auto‑starting services with Termux:Boot, and running a full Linux distro in proot. HN discussion focuses less on the tech and more on LLM‑authorship, title accuracy, and simpler alternatives.

---

### Comment pulse
- Main work done by Claude Code → author logged real steps, quirks, then had Claude reorganize and expand the write‑up.  
- Some see “vibe coding”/“$25 Walmart phone” as hype → actually just a cheap Android hosting a static site.  
- Critics: Termux or simple HTTP‑server apps would suffice → fans: full proot Linux is more flexible and fun — counterpoint: LLM chose many design decisions, not the human.

---

### LLM perspective
- View: This is really a workflow demo for pairing Termux-style tinkering with an LLM as sysadmin/copywriter.  
- Impact: Low-cost always‑on “microservers” become accessible to beginners who can lean on LLMs for setup.  
- Watch next: Benchmarks of reliability, long‑term uptime, and clearer norms for disclosing LLM-generated technical content.
