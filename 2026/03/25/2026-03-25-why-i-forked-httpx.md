# Why I forked httpx

- Score: 231 | [HN](https://news.ycombinator.com/item?id=47514603) | Link: https://tildeweb.nl/~michiel/httpxyz.html

### TL;DR
The author forked the popular Python HTTP client httpx into httpxyz after their zstd bugfix sat unreleased for over a year amid stalled maintenance, hidden GitHub issues, and long‑promised but disruptive 1.0 plans. With major users like OpenAI and Anthropic pinning httpx <1.0, they argue a stable, conservative fork is needed: frequent patch releases, no large rewrites, and a focus on compatibility. httpxyz lives on Codeberg to avoid GitHub monoculture; migration is optional and largely drop‑in, though plugins may lag.

---

### Comment pulse
- Ecosystem churn → People recommend alternatives like pyreqwest, niquests, and aiohttp; trade‑offs include Trio support, performance, and trust in project governance.  
- Forking norms → Some say hinting at a fork feels like a threat; better to quietly fork than argue over stewardship—counterpoint: signaling intent can pressure for maintenance.  
- Fragmentation vs stdlib → Debate over Python’s many HTTP clients; others note most languages ship awkward HTTP APIs because getting “simple and complete” right is inherently hard.

---

### LLM perspective
- View: httpxyz formalizes what many already do informally: pin versions and rely on de‑facto “LTS” behavior from community forks.  
- Impact: Teams depending on httpx gain a clearer risk‑management option, but must track yet another HTTP client in evaluations.  
- Watch next: Whether httpxyz gains plugin ecosystem, CI adoption by big libs, and documented migration benchmarks versus niquests, aiohttp, and pyreqwest.
