# DNS-Persist-01: A New Model for DNS-Based Challenge Validation

- Score: 164 | [HN](https://news.ycombinator.com/item?id=47064047) | Link: https://letsencrypt.org/2026/02/18/dns-persist-01.html

TL;DR
- Let’s Encrypt is adding DNS-PERSIST-01, a new ACME validation where you publish a persistent TXT record binding a domain to a specific ACME account and CA. This eliminates per-renewal DNS edits and propagation delays, especially helping IoT fleets, internal/LAN services, and large batch issuance. Options cover wildcard authorization, multiple CAs, and optional expiry via persistUntil. Security shifts from widely distributed DNS API credentials to protecting the ACME account key. HN discussion centers on account-identity leakage and unchanged DNS compromise risks.

Comment pulse
- Exposing accounturi in DNS raises privacy/attack-surface worries; attackers or Shodan could map accounts to domains — counterpoint: CAA records already leak similar identifiers.
- Admins welcome easier certs for non‑Internet‑facing hosts and UIs; others note today’s bind+RFC2136 per‑record keys already localize risk without persistent authorization.
- Questions about DNS compromise: commenters reiterate controlling authoritative DNS already enables certificate issuance via any challenge, so DNS‑PERSIST‑01 doesn’t fundamentally worsen that threat.

LLM perspective
- View: Persistent DNS authorizations remove DNS from issuance pipelines but centralize trust in long‑lived ACME accounts and their operational hygiene.
- Impact: DNS providers and certificate consumers gain simpler automation, while security teams must harden ACME account‑key storage and recovery procedures.
- Watch next: deployment stats, client support, and whether future drafts introduce privacy‑preserving identifiers instead of raw account URIs in DNS.
