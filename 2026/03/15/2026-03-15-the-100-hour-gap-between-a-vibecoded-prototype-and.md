# The 100 hour gap between a vibecoded prototype and a working product

- Score: 224 | [HN](https://news.ycombinator.com/item?id=47386636) | Link: https://kanfa.macbudkowski.com/vibecoding-cryptosaurus

### TL;DR
An indie builder used “vibecoding” (LLM-driven coding with ChatGPT/Claude/Gemini) to ship Cryptosaurus, a Farcaster mini-app that mints personalized dino NFTs. A clickable prototype appeared in ~1 hour, but turning it into a production app took ~100: iterating UI/UX, hardening image prompts, wiring AWS/Vercel/Farcaster, fixing smart-contract and nonce bugs, and planning for load. HN discussion largely agrees: LLMs give 10x for prototypes but more like 2–3x for real systems, and you still need architecture, testing, and judgment—plus, NFTs in 2026 remain contentious.

---

### Comment pulse
- Practitioners: LLMs are magical for first PoC, but production demands code review, perf/security work, and better tooling (tests, CUE-style constraints) to avoid regressions.  
- Critics: author “learned DevOps” mostly by prompting; others deride $2 NFT dinos and manufactured virality as crypto-style gambling, not serious products.  
- Meta: last 20% is fixing compounded shortcuts from earlier AI steps; frontload design/architecture and use LLMs as thinking partners, not code monkeys.

---

### LLM perspective
- View: Vibecoding moves difficulty from syntax to specifying intent, edge cases, and systems behavior; this human thinking work doesn’t vanish.  
- Impact: Non-specialists can now ship small apps; experts gain leverage but must guard hot paths, infra, and security from naive agent changes.  
- Watch next: Tighter loops between design tools, static analyzers, and agents, plus domain-specific validators, to reduce that “hidden 100 hours” to tens.
