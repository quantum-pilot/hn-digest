# The RSS feed reader landscape

- Score: 227 | [HN](https://news.ycombinator.com/item?id=45517134) | Link: https://lighthouseapp.io/blog/feed-reader-deep-dive

TL;DR
The article maps RSS readers by deployment (on-device, browser extension, self-hosted, hosted) and business model (free, one-time, SaaS), then explains trade-offs: self-hosted for control, on-device for offline speed, hosted for polished features like newsletters, AI, and continuous fetching. APIs enable third‑party apps and offline sync; email‑to‑RSS bridges newsletters. Tiny Tiny RSS is sunsetting; Folo is free for now. Recommended path: pick a category, trial a few, and migrate via OPML. HN debates lost social discovery and extension-based setups.

Comment pulse
- Bring back Reader-like sharing → platforms down-rank external links; propose OPML discovery + federated rating posts — counterpoint: social networks killed Reader, not vice versa.
- NetNewsWire favored on Apple → fast, simple, sync via iCloud or aggregators; many pair with FreshRSS for cross-device state.
- Extension users persist → Brief and new Brook praised for in-browser, on-device control; interest in Chrome port and mobile compatibility.

LLM perspective
- View: Clear taxonomy simplifies choice; biggest gap is discovery/social layer beyond subscriptions.
- Impact: Hosted services differentiate via AI, newsletter ingestion, and teams; self-hosted may absorb users after Tiny Tiny RSS shutdown.
- Watch next: Standardize OPML discovery, experiment with ActivityPub-like signals; track Folo monetization and TTRSS forks; publish fetch-latency/offline benchmarks.
