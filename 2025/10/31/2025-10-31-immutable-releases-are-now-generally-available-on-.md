# Immutable releases are now generally available on GitHub

- Score: 135 | [HN](https://news.ycombinator.com/item?id=45772064) | Link: https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available/

### TL;DR

GitHub now lets repositories or organizations make all new releases immutable: published assets cannot be added, changed, or deleted; associated tags cannot move or disappear; and Sigstore-format attestations support external verification. Existing releases stay mutable unless republished, and disabling the setting does not unlock prior immutable releases. Commenters welcome stronger supply-chain guarantees but debate legitimate mutation for nightlies and corrections, demand an explicit permanent revocation mechanism, and stress that consumers should still verify signatures or pin hashes independently.

### Comment pulse

- Immutability improves artifact identity → mutable tags and assets let compromised accounts silently replace what consumers download.
- Operational exceptions still matter → nightlies, broken releases, and illegal content need revocation or removal without permitting replacement.
- Host guarantees are insufficient → locally pinned hashes or externally held signing keys reduce dependence on GitHub itself.

### LLM perspective

- View: Immutability solves silent substitution, but trustworthy release management also requires visible, irreversible revocation.
- Impact: Maintainers must separate stable releases from mutable channels and design correction workflows before enabling the setting.
- Watch next: Look for GitHub’s revocation semantics, UI provenance indicators, and automated Sigstore policy adoption.
