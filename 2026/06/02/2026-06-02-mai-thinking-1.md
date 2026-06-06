# MAI-Thinking-1

- Score: 167 | [HN](https://news.ycombinator.com/item?id=48374362) | Link: https://microsoft.ai/news/introducing-mai-thinking-1/

### TL;DR
Microsoft’s MAI-Thinking-1 is a 35B-active, ~1T-parameter sparse Mixture-of-Experts reasoning model aimed at coding and STEM tasks. It’s trained “from scratch” on clean, licensed, non-synthetic, non-distilled data, and is part of a broader “Hill-Climbing Machine” stack for continuously improving models and infrastructure together. On internal and public benchmarks it competes with larger models on SWE-Bench Pro and AIME math, and human raters prefer it to Claude Sonnet 4.6. Hacker News debates the licensing claims, benchmark competitiveness, and real-world value versus distillation-heavy rivals.

---

### Comment pulse
- Clean, “appropriately licensed” data claim → curiosity and skepticism about whether this just means scraping GitHub; tension with earlier Phi synthetic-data messaging.  
- Benchmarks vs DeepSeek/GLM/Kimi → looks weaker per parameter; some argue that non‑distilled, from-scratch training is strategically valuable despite lower scores.  
- Positioning → 256k context feels small amid 1M-token marketing; mixed views on whether this is a frontier step or polished benchmark-chaser.

---

### LLM perspective
- View: A strong non-distilled model is strategically important; it proves Microsoft can escape dependence on other labs’ outputs.  
- Impact: Most immediate for enterprises prioritizing provenance, control, and integration with Microsoft’s stack over absolute leaderboard wins.  
- Watch next: Third-party evals on coding agents, legal clarity on “licensed” data, and whether follow-on models close the gap to distilled peers.
