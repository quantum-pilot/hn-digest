# My minute-by-minute response to the LiteLLM malware attack

- Score: 269 | [HN](https://news.ycombinator.com/item?id=47531967) | Link: https://futuresearch.ai/blog/litellm-attack-transcript/

### TL;DR
An ML engineer’s laptop locked up under an 11k‑process Python fork bomb, initially blamed on Claude Code. Using Claude itself to sift logs, inspect site‑packages, and reason about timelines, he traced the issue to a freshly published litellm 1.82.8 wheel on PyPI. A malicious `litellm_init.pth` auto‑executed on every Python start, stole credentials, attempted persistence and Kubernetes lateral movement, and caused runaway recursion. Within ~70 minutes he’d confirmed the supply‑chain compromise, notified PyPI and maintainers, and published a disclosure—showcasing how AI can turn non‑specialists into effective incident responders.

---

### Comment pulse
- AI‑assisted discovery by non‑security devs is positive → high‑quality reports get fast‑tracked and broaden coverage — counterpoint: security teams already drown in low‑quality “vuln” noise.  
- LLM agents are powerful but unsafe as operators → they lack responsibility; might execute malware despite warnings, so humans should perform risky commands themselves.  
- Package registries need better real‑time defenses → feeds, cooldowns, and mandated scanning could catch poisoned releases quickly and limit blast radius.

---

### LLM perspective
- View: This incident is an early template for AI‑driven incident response: human suspicion, AI log‑digging, and fast, structured disclosure.  
- Impact: More engineers can detect and report supply‑chain attacks, but security triage and tooling must evolve to handle higher report volume.  
- Watch next: Stronger sandboxed “secops copilots,” registry‑level malware scanning APIs, and model training on real attack chains without enabling offensive use.
