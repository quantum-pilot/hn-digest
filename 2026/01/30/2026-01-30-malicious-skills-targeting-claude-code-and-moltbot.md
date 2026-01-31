# Malicious skills targeting Claude Code and Moltbot users

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46827731) | Link: https://opensourcemalware.com/blog/clawdbot-skills-ganked-your-crypto

### TL;DR
Researchers documented malicious third‑party “skills” for AI coding agents like Claude Code and Moltbot that request wallet/API credentials and then exfiltrate them, often via Telegram bots. A community security platform is beginning to catalog these as a new class of open‑source malware. Hacker News discussion centers less on technical novelty and more on why users hand over keys to unvetted agents, likening this to classic low‑effort scams and warning against running unsandboxed LLM agents with real‑world permissions.

### Comment pulse
- Original blog title exaggerated an “all my crypto was ganked” story → Readers emphasize HN’s guideline: keep accurate, non‑sensational titles.

- Malicious AI skills target credulous users → Like typo‑filled phishing, demanding full credentials pre‑filters victims — counterpoint: this erodes ecosystem trust, not just “gullible” users.

- Skeptics avoid giving agents real permissions → Seeing LLMs as fallible text predictors, they allow only narrow tasks (e.g., calendar); everything else stays sandboxed.

### LLM perspective
- View: Treat AI “skills” like unvetted browser extensions; default should be zero‑trust plus granular, revocable permissions and mandatory code review.  

- Impact: Crypto, finance, and dev‑tool users remain prime targets; vendors must harden marketplaces and detection, not blame user error.  

- Watch next: Standardized signing, permission manifests, and shared threat‑intel feeds for AI agents, similar to app stores and package registries.
