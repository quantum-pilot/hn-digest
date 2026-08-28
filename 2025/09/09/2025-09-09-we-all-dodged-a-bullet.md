# We all dodged a bullet

- Score: 806 | [HN](https://news.ycombinator.com/item?id=45183029) | Link: https://xeiaso.net/notes/2025/we-dodged-a-bullet/

### TL;DR

A targeted phishing email compromised a maintainer of widely depended-upon npm packages, but the injected browser-focused malware reportedly only replaced cryptocurrency-payment destinations rather than stealing server credentials or API keys. The message used the maintainer's username, plausible two-factor-authentication urgency, a deadline, and the deceptive domain `npmjs.help`. The author avoids blaming the victim and argues any dependency can become hostile. Commenters note that pinned versions are not a complete defense and criticize ecosystems built around large, deeply transitive dependency trees.

### Comment pulse

- Some readers call the crypto-only payload narrowly opportunistic; others say irreversible transfers made it a rational attacker choice.
- Discussion cites a separate Nx incident to show development tools and local credentials remain exposed through other supply-chain paths.

### LLM perspective

- View: The lucky part was payload selection, not ecosystem resilience; trusted publication credentials still converted phishing into broad distribution.
- Impact: Even a narrow compromise forces downstream users to investigate transitive exposure they may not know they have.
- Watch next: Package-signing controls, publisher authentication, capability restrictions, incident timelines, and whether maintainers reduce dependency depth.
