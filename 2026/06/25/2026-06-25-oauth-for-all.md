# OAuth for all

- Score: 360 | [HN](https://news.ycombinator.com/item?id=48668033) | Link: https://blog.cloudflare.com/oauth-for-all/

### TL;DR

Cloudflare opened self-managed OAuth applications to every customer, replacing manually approved integrations and awkward API tokens with scoped consent and dashboard revocation for SaaS, internal tools, and agents. Enabling this required staged upgrades of Ory Hydra: customized nonblocking 1.x migrations, then a three-hour blue-green 2.x migration with queued revocations. A migration bug corrupted some valid sessions and caused 403s, but restoration stabilized traffic; API P95 fell 45%, from 185 to 101 ms. HN praised Hydra’s efficiency while raising centralization, broader IAM, and dynamic-client-registration phishing concerns.

### Comment pulse

- OAuth can be operationally routine at scale → one practitioner handled billions of monthly requests with three people, yet juniors often struggle conceptually.
- The upstream migration deserves scrutiny → a former Hydra contributor asked whether the session-corrupting open-source migration has been fixed.
- Agent authorization remains underspecified → dynamic client registration can permit malicious callbacks — counterpoint: allowlists help but depart from standard vendor behavior.

### LLM perspective

- **View:** The migration’s hardest invariant was preserving revocation semantics across concurrent databases, not merely moving rows or binaries.
- **Impact:** Integration developers gain safer delegated access; Cloudflare assumes greater ecosystem power and responsibility for consent clarity and abuse prevention.
- **Watch next:** Verify the Hydra fix upstream, publish lost-write counts, and define secure registration, redirect, multitenancy, SAML, and identity roadmaps.
