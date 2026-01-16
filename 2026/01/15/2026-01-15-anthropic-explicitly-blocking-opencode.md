# Anthropic Explicitly Blocking OpenCode

- Score: 164 | [HN](https://news.ycombinator.com/item?id=46625918) | Link: https://gist.github.com/R44VC0RP/bd391f6a23185c0fed6c6b5fb2bac50e

### TL;DR
A script using Claude’s OAuth flow shows Anthropic’s private Claude Code endpoint rejects system prompts containing “You are OpenCode/opencode” while allowing similar identities like “You are Cursor/Pi/Droid.” This suggests name-based blocking of the open-source OpenCode assistant on a subsidized, non-public API. HN splits: some say Anthropic is just enforcing ToS on a reverse‑engineered private endpoint; others see selective, anti-competitive behavior and a worrying move toward lock-in, prompting calls for adversarial interoperability and even subscription cancellations.

---

### Comment pulse
- This only affects a private Claude Code endpoint → reverse‑engineered, metered differently, never sold for 3rd‑party clients — counterpoint: keyword targeting makes “any tool would be blocked” dubious.  
- Supporters: Anthropic must protect investment, stop arbitrage on discounted access → critics: preferential pricing for their own client looks anti-competitive and legally questionable.  
- Hackers: adversarial interoperability is legitimate, OpenCode did nothing wrong → others: private APIs as moat are industry standard; condemning Anthropic means condemning Apple/Google too.

---

### LLM perspective
- View: Name-based blocking of a specific open-source client is a bad look, regardless of formal ToS justification.  
- Impact: Open-source tool authors, power users, and Anthropic’s “trustworthy” brand positioning are all strained by opaque, selective restrictions.  
- Watch next: Whether Anthropic publishes clear client-agnostic billing, relaxes blocks, or doubles down—and whether rivals market “open coding endpoints” in response.
