# The web does not need gatekeepers: Cloudflare’s new “signed agents” pitch

- Score: 454 | [HN](https://news.ycombinator.com/item?id=45066258) | Link: https://positiveblue.substack.com/p/the-web-does-not-need-gatekeepers

- TL;DR
    - The author argues Cloudflare’s “signed agents” effectively create a centralized allowlist for bots, undermining the open web. Instead, authenticate agents via decentralized, verifiable chains of delegation and per-request signatures (keys discoverable via DNS); authorize via short‑lived, task‑scoped, attenuated tokens that can be delegated (e.g., macaroons/biscuit-style). Agents will proliferate; protocols must remain open. HN discussion splits between curbing aggressive AI crawlers draining resources and avoiding gatekeepers that also block privacy users; proposals range from regulation to clearer separation of user-initiated agents vs training scrapers.

- Comment pulse
    - Open vs protection: small sites overwhelmed by AI scraping; some call for regulating robots.txt with fines — counterpoint: blocking bots conflicts with “free and open” access.
    - Differentiate bots: user-initiated agent reads acceptable; training scrapers not. Cloudflare allegedly blurs both to toll traffic and centralize control.
    - Anti-gatekeeper: bot defenses punish privacy/VPN users; central whitelists echo email’s blacklist maze; CA analogy contested after Let’s Encrypt’s democratization.

- LLM perspective
     - View: Decentralized agent identity via DNS-published keys plus task-scoped, attenuated tokens beats vendor “bot passports.”
	   - Impact: CDNs, LLM providers, and sites interoperate on open proofs; operators get fine-grained control; privacy browsers face fewer false blocks.
	   - Watch next: Concrete IETF/W3C drafts, reference libs, adoption by major CDNs; crawler cost audits; any robots.txt enforcement or attestation legislation.
