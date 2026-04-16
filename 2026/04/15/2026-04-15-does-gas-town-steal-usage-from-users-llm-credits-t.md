# Does Gas Town 'steal' usage from users' LLM credits to improve itself?

- Score: 193 | [HN](https://news.ycombinator.com/item?id=47785053) | Link: https://github.com/gastownhall/gastown/issues/3649

### TL;DR
Gas Town, Steve Yegge’s AI “agent town,” appears to ship formulas that can use your LLM credits and GitHub credentials to triage issues, fix bugs, and cut releases on the upstream Gas Town repo—without clear disclosure or opt‑in. A user discovered their Claude credits and GitHub account were quietly funding and submitting PRs to Gas Town itself. The GitHub issue calls for making this behavior opt‑in; discussion spans “on‑brand but needs consent,” accusations of unethical/possibly illegal conduct, and claims it’s actually a misfired internal release tool.

---

### Comment pulse
- “Fits Gas Town’s chaotic ethos” → if contribution is clearly disclosed, making it part of the social contract is fine — counterpoint: disclosure alone doesn’t legitimize bitcoin‑miner‑style resource hijacking.  
- Critiques of Yegge’s approach → philosophy is “burn tokens fast, 24/7”; some compare hype to NFTs and call Gas Town a vibe‑coded mess with low real‑world rigor.  
- Nuance and future pattern → some say this was a bug triggering an internal release formula; others see a possible OSS model where agents auto‑contribute, but only with consent and cost caps.

---

### LLM perspective
- View: Any tool that can spend a user’s API money or act as them online must get explicit consent per capability, not hide behind vibes or blog posts.  
- Impact: OSS AI orchestration frameworks will face higher scrutiny from security teams, cloud providers, and possibly regulators over undisclosed resource use.  
- Watch next: Whether Gas Town ships an opt‑in toggle, hard spending limits, and transparent logs; cloud LLMs may add policies for third‑party “self‑updating” agent systems.
