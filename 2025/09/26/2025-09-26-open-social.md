# Open Social

- Score: 383 | [HN](https://news.ycombinator.com/item?id=45388021) | Link: https://overreacted.io/open-social/

- TL;DR
    - Dan Abramov argues “open social” will do for social data what open source did for code. In AT Protocol, your posts/likes/follows live in a user‑controlled repository (addressable via a DID tied to your domain), and apps aggregate over that signed data via relays/appviews. You can migrate providers without breaking links or losing reach; products can be forked/remixed because the data persists. HN debates ATProto versus ActivityPub trade‑offs, Bluesky’s influence, and schema/interop nuances.

- Comment pulse
    - User‑owned repos → real portability; handles bind to DIDs via DNS; replies/likes live in the author’s repo, not the target’s.
    - Critique: global relays/appviews centralize processing and hinder privacy (e.g., private likes) → AP’s inbox model scales subscriptions better — counterpoint: signed commits and third‑party relays reduce trust/lock‑in.
    - Bluesky dominance risk → stewards could tilt standards; defenders cite CAR backups, host‑independent migration, and layered infra to minimize capture.

- LLM perspective
    - View: Per‑user repos and typed schemas enable remixable social graphs; success hinges on migration UX and non‑Bluesky flagship apps.
    - Impact: Moats shift from data custody to indexing, moderation, and ranking; startups can bootstrap on existing follows/content.
    - Watch next: Independent appviews/relays at scale, shared lexicons, private/DM models, abuse tooling, and one‑click moves for mainstream users.
