# Show HN: s@: decentralized social networking over static sites

- Score: 394 | [HN](https://news.ycombinator.com/item?id=47344548) | Link: http://satproto.org/

### TL;DR

s@ sketches social networking with no application servers or relays: each person’s domain hosts encrypted static JSON, and browser clients fetch friends’ sites, decrypt posts, merge feeds, and publish updates. Mutual follows deliberately limit it to small groups. X25519 keys wrap a shared content key per follower; unfollowing rotates that key and re-encrypts every post, while identities rely on domains and TLS. Commenters admire the experiment but question localStorage key custody, recovery, setup burden, metadata leakage, and whether a network without discovery or dopamine offers enough benefit for nontechnical friends.

### Comment pulse

- Self-reliance shifts costs to users → a lost private key can strand a feed unless exports and backups actually happen.
- Static hosting keeps architecture legible → GitHub Pages is only an example; any CORS-enabled host can carry the encrypted files.
- Mass adoption is not the stated goal → counterpoint: even small communities need onboarding and recurring value to sustain participation.

### LLM perspective

- **View:** The design trades intermediary trust for key-management and availability duties, a reasonable experiment with a deliberately narrow audience.
- **Impact:** Technical friend groups gain portable domain identities; family-scale adoption still depends on managed recovery.
- **Watch next:** Multi-device keys, revocation costs, metadata protections, host portability, and client interoperability.
