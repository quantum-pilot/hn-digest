# Self-hosting a Matrix server for 5 years

- Score: 232 | [HN](https://news.ycombinator.com/item?id=46106132) | Link: https://yaky.dev/2025-11-30-self-hosting-matrix/

### TL;DR

After five years running Synapse for relatives and friends, the author finds Matrix reliable and its WhatsApp bridge useful, but maintenance remains awkward. Postgres is effectively required, cleanup leaves orphaned rooms or media, state data grows, federation is hard to disable, and user deletion is incomplete. Element clients add notification, onboarding, synchronization, and calling friction; the author considers switching to Snikket. Commenters reported both stable long-running servers and similar cleanup problems, while a Matrix representative described recent administration and encryption improvements.

### Comment pulse

- Small Matrix deployments can run reliably → operators nevertheless encounter persistent media, state, and calling maintenance gaps.
- Newer Element work addresses administration and synchronization → counterpoint: client transitions and incompatible calling still disrupt users.
- Federation complicates permanent deletion → participants disagreed whether this is an inherent tradeoff or insufficient local tooling.

### LLM perspective

- View: Reliability alone is insufficient when routine lifecycle operations remain difficult for a small administrator.
- Impact: Families and small groups may prefer simpler XMPP packaging despite Matrix's bridges and federation.
- Watch next: Evaluate cleanup tooling, Element interoperability, resource use, and migration effort against Snikket on identical hardware.
