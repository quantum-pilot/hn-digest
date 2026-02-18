# HackMyClaw

- Score: 232 | [HN](https://news.ycombinator.com/item?id=47049573) | Link: https://hackmyclaw.com/

### TL;DR
HackMyClaw is a small CTF-style challenge: email an OpenClaw-based assistant (“Fiu”) and try to prompt-inject it into leaking a secrets.env file. Fiu runs Claude Opus 4.6, has only lightweight prompt instructions not to reveal secrets, and checks messages hourly under rate limits, with a $100 bounty for first exfiltration. HN discussion debates how representative this setup is: batched attempts may actually harden Fiu, context retention makes it quickly paranoid, and some question the organizer’s incentives.

---

### Comment pulse
- Creator: experiment testing Claude Opus via email-only injection; minimal defenses, rate-limited, manual review — counterpoint: some suspect it doubles as an AI-enthusiast mailing list.  
- Batch-processing many attempts gives Fiu obvious patterns, making subtle injections harder; commenters suggest agents should default to treating all external text as hostile.  
- Others question realism: assistant retains global context, knows it's under attack, and only summarizes emails, unlike typical autonomous agents executing untrusted actions.  

---

### LLM perspective
- View: Shows how fragile agent-style email bots remain when only prompted not to leak secrets, even with a strong base model.  
- Impact: Useful micro-benchmark for prompt-injection defenses; highlights need for isolation, per-request contexts, and non-LLM guardrails beyond natural-language instructions.  
- Watch next: Interesting follow-up: run identical challenge with per-email fresh assistants, stronger system prompts, or different models to compare vulnerability profiles.
