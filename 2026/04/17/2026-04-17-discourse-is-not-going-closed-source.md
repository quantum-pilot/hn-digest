# Discourse Is Not Going Closed Source

- Score: 206 | [HN](https://news.ycombinator.com/item?id=47802233) | Link: https://blog.discourse.org/2026/04/discourse-is-not-going-closed-source/

### TL;DR

Discourse responds to Cal.com’s move from open source to closed source, rejecting the idea that AI-driven vulnerability discovery makes openness too dangerous. They argue SaaS apps already expose large attack surfaces via JavaScript, APIs, and behavior, so closing the repo mainly weakens defenders, not attackers. Discourse instead embraces AI as a security tool, running full‑code scans with modern models, validating issues via tests, and patching quickly. They frame Cal.com’s move as a business, not security, decision and recommit to GPLv2 openness.

---

### Comment pulse

- Openness as discipline → Public code creates pressure to fix issues early and rigorously—counterpoint: that mentality should exist even in closed-source shops.  
- Cal.com’s motives → Many read the “security” framing as cover for competitive/governance concerns—counterpoint: bad outcomes don’t always imply bad-faith intent.  
- Security-through-obscurity is brittle → Attackers already brute-force endpoints and reverse-engineer binaries; AI just scales that, so hiding source adds little real protection.

---

### LLM perspective

- View: AI makes vulnerability discovery cheap for everyone; net benefit goes to teams that systematize scanning and fast patch pipelines.  
- Impact: Open-source projects that integrate AI security tooling and strong governance gain trust versus SaaS competitors retreating behind closed code.  
- Watch next: Standardized AI-powered code audits, shared open benchmarks for “secure-by-default” frameworks, and licenses clarifying expectations when projects later try to close.
