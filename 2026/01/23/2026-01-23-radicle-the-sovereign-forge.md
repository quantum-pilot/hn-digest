# Radicle: The Sovereign Forge

- Score: 250 | [HN](https://news.ycombinator.com/item?id=46732213) | Link: https://radicle.xyz

### TL;DR

Radicle is a peer-to-peer code forge layering collaboration onto Git without a controlling host. Repositories replicate among nodes through gossip; cryptographic identities sign code and social artifacts so authorship remains verifiable when data comes from untrusted peers. Issues, discussions, and reviews are extensible Git objects, making work local-first and offline. Its stack provides command-line, desktop, web, and terminal interfaces over a node and HTTP daemon. Release 1.6.0 supports Linux, macOS, and BSD; private repositories use selective replication rather than encryption at rest.

### Comment pulse

- Stable identities preserve learned trust → signatures verify continuity after introduction — counterpoint: choosing the first trusted key or repository remains social.
- Replication complicates deletion → revocation and safer defaults remain unfinished, although exposed secrets are already hard to retract from central hosts.
- Architecture distinguishes Radicle → commenters contrast fully local replicated work with Tangled’s knots and central AppView.

### LLM perspective

- View: Sovereignty comes from signed local state and optional replication, not merely self-hosting Git.
- Impact: Teams gain offline resilience but inherit identity discovery, moderation, retention, and seed-availability duties.
- Watch next: Publication defaults, network revocation, group identities, private-repository ergonomics, and seed reliability.
