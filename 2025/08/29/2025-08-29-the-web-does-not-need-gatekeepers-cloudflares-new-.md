# The web does not need gatekeepers: Cloudflare’s new “signed agents” pitch

- Score: 454 | [HN](https://news.ycombinator.com/item?id=45066258) | Link: https://positiveblue.substack.com/p/the-web-does-not-need-gatekeepers

### TL;DR

The author rejects Cloudflare’s “signed agents” approach as a vendor-controlled allowlist rather than an open-web standard. They propose independently verifiable delegation chains, request-level signatures, DNS-published keys, and short-lived task-scoped authorization tokens instead of permanent agent credentials. The goal is to separate authentication from authorization while avoiding a central arbiter of valid agents. The proposal is conceptual and an initial implementation is promised. Commenters counter that site operators face severe crawler load and need workable protection, exposing tension between decentralized access and practical abuse control.

### Comment pulse

- Operators reported aggressive crawling, high request rates, invented URLs, and substantial bandwidth use.
- Privacy-focused users said bot defenses also block uncommon browsers and VPN traffic.
- Others argued website owners retain the right to gate access to keep services viable.

### LLM perspective

- View: Portable identity helps delegation, but it does not by itself solve abusive volume or content policy.
- Impact: A dominant vendor registry could turn bot mitigation into infrastructure-level permissioning.
- Watch next: Evaluate open implementations on revocation, rate limits, impersonation resistance, and operator choice.
