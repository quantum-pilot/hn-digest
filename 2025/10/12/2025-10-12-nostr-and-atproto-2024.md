# Nostr and ATProto (2024)

- Score: 114 | [HN](https://news.ycombinator.com/item?id=45556763) | Link: https://shreyanjain.net/2024/07/05/nostr-and-atproto.html

- TL;DR
  - Longform comparison of Nostr and ATProto: both borrow from Scuttlebutt to decentralize “Twitter,” but diverge in philosophy. Nostr maximizes censorship‑resistance with client-held keys, dumb relays, immutable signed events, and powerful relay-side filtering; deletes and privacy are hard. ATProto optimizes usability: PDS-hosted repos, DID-based identity, edits/deletes, and AppViews that aggregate the global firehose—introducing trust and complexity. ActivityPub centers communities but ties identity to servers. HN discusses developer ergonomics, moderation realities, and whether Mastodon’s email-like model already solves most needs.

- Comment pulse
  - Nostr is simple to hack on → just signed JSON over WebSockets; fast to prototype. — counterpoint: AT’s complexity avoids ambiguous “mix-and-match” specs.
  - Tech isn’t decisive → success hinges on users, norms, and moderation workflows for spam/abuse.
  - Mastodon/email model is enough → don’t reinvent portability; — counterpoint: Nostr key-ownership and AT’s global views enable features Mastodon can’t.

- LLM perspective
  - View: Convergence likely: AT adopts finer relay-style filtering; Nostr standardizes moderation/queries beyond NIPs.
  - Impact: Dev choices crystallize: key custody vs recoverability; client filtering vs AppViews; moderation marketplaces emerge.
  - Watch next: Decentralizing did:plc; independent AppView/Relay benchmarks and audits; standardized Nostr key-recovery and account-rotation proposals; real usage metrics beyond anecdotes.
