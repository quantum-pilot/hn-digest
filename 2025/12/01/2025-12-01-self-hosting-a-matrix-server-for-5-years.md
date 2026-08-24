# Self-hosting a Matrix server for 5 years

- Score: 232 | [HN](https://news.ycombinator.com/item?id=46106132) | Link: https://yaky.dev/2025-11-30-self-hosting-matrix/

### TL;DR

After five years running Synapse for fewer than ten active users, the author finds messaging and a WhatsApp bridge reliable but administration disproportionately burdensome. PostgreSQL is effectively required; attachments, departed rooms, append-only state, and undeletable accounts accumulate; federation is awkward to disable; and Element clients bring notification, verification, calling-compatibility, and onboarding problems. The seven-service, Kubernetes-based community suite feels excessive for a household, so the author favors Snikket. Discussion showed that configuration and software generation strongly shape whether the same ecosystem feels durable or untenable.

### Comment pulse

- Long-running operators converge on lifecycle gaps → media deletion, database growth, user management, and simple auditing still demand manual knowledge.
- Client generations fractured calling → legacy one-to-one VoIP and MatrixRTC lack interoperability because maintainers prioritized the newer system under limited resources.
- Experiences vary with configuration → counterpoint: newer encryption and sliding sync reportedly fix major failures, while some small servers run reliably.

### LLM perspective

- View: Federation’s ambition is undermined when basic household administration requires specialist cleanup and migration knowledge.
- Impact: Small operators may consolidate on suites, remain on aging clients, or switch to simpler XMPP deployments.
- Watch next: Element administration coverage, media retention defaults, VoIP interoperability, local-account onboarding, and ESS resource requirements.
