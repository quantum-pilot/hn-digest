# Are we decentralized yet?

- Score: 492 | [HN](https://news.ycombinator.com/item?id=45077291) | Link: https://arewedecentralizedyet.online/

- TL;DR
  - A dashboard measures how concentrated user data is across the Fediverse, Bluesky’s ATProto “Atmosphere,” and public git forges using HHI and Shannon entropy. It aggregates servers run by the same entity and focuses on active users, while inviting broader decentralization metrics. HN debates HHI edge cases and contrasts architectures: ATProto’s global firehose favors centralized AppViews/Relays despite cheap personal hosting; ActivityPub’s follow-based delivery is cheaper but fragmented. Claims that “everything centralizes” face nuanced counterexamples from Git, BitTorrent, SMTP, and Bitcoin.

- Comment pulse
  - HHI >10,000 can occur if market “shares” include negative returns → squares inflate. — counterpoint: that’s sales-share misuse; true market share stays 0–100%.
  - ATProto: cheap PDS; Relay ≈ $30/mo; full AppView ≈ $300/mo for global view. ActivityPub: cheaper servers, but partial, follow-based synchronization by design.
  - “Everything centralizes” claim challenged: Git remains decentralized in workflow; BitTorrent uses many trackers; SMTP deliverability depends on configuration, not size; Coinbase doesn’t centralize Bitcoin.

- LLM perspective
  - View: Data-location indices omit governance, moderation, infra providers, and protocol power—add multi-dimensional “control surface” metrics.
  - Impact: ATProto’s cohesive feed nudges centralization at AppView/Relay layers; ActivityPub emphasizes per-instance autonomy at usability cost.
  - Watch next: Add Nostr and Matrix; publish time-series HHI/entropy; standardize “active user” definition; track entity consolidation across hosting providers.
