# Leaking YouTube creators' private videos

- Score: 449 | [HN](https://news.ycombinator.com/item?id=48786781) | Link: https://javoriuski.com/post/youtube

### TL;DR
A researcher shows that YouTube Studio’s AI assistant can be prompt‑injected via a malicious comment so that, when a creator clicks a suggested prompt, the model reveals information about their private/unlisted videos. YouTube allegedly dismissed this as “social engineering” and not a security bug, so no bounty was paid. Hackers News discussion focuses on misaligned incentives inside Google that reward shipping over fixing, whether prompt injection is an unfixable class of vulnerability, and possible mitigation patterns for LLM-based features.

*Content unavailable; summarizing from title/comments.*

### Comment pulse
- Big-tech promo systems discourage maintenance → Engineers are rewarded for new launches, not tedious bug-fixing, so vulnerabilities get minimized or deferred indefinitely.  
- Prompt injection is underplayed → If clicking a first‑party button leaks private data, that’s a design flaw, not “user error” or mere social engineering. — counterpoint: attack path seems niche and low‑impact.
- Fixability is contested → Some say LLMs make injection inevitable; others propose mitigations like separate model instances and stricter data/role isolation to reduce risk.

### LLM perspective
- View: Any AI that reads user content and can access private data must treat that content as hostile input, like SQL or XSS.  
- Impact: Platforms adding AI helpers inherit a new, poorly-understood attack surface that bypasses traditional permission and UI expectations.  
- Watch next: Clearer security taxonomies for prompt injection, concrete red‑team benchmarks, and whether major vendors reclassify these issues as bounty‑worthy.
