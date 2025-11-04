# Why Nextcloud feels slow to use

- Score: 428 | [HN](https://news.ycombinator.com/item?id=45798681) | Link: https://ounapuu.ee/posts/2025/11/03/nextcloud-slow/

- TL;DR
  - HN discussion says Nextcloud’s “slow” feel is less about JS bundle size and more about many per-resource REST calls that serialize work and amplify network latency, especially on mobile. Users report unreliable iOS photo backup (disconnects, locked WebDAV, stalled/resets) and calendar UX regressions. Maintainers cite architectural accretion and plugin silos that resist cohesive data loading. Alternatives for photos (Immich) or uploads (FolderSync, Copyparty) are suggested. Proposed fixes: batch requests, persistent connections/WebSockets, better caching, and performance budgets; server stability is fine, but clients feel flaky.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Calendar load: 124 requests (31 uncached); per-calendar/resource calls serialize; 33s on 4G. Prefer bundling, WebSockets, bulk changefeeds. — counterpoint: 15MB JS parse also hurts.
  - Mobile sync unreliable: iOS disconnects, locked WebDAV, stalled uploads; family backups fail; users switch to Immich, FolderSync, Copyparty.
  - Architecture debt: layered plugins, Redis/config detours; hosting market benefits from complexity; ownCloud rewrote core in Go; consider SSO-linked tools over monolith.

- LLM perspective
  - View: Treat Nextcloud as a latency-bound SPA; audit N+1 patterns and enforce batched endpoints and persistent connections.
  - Impact: Biggest gains for mobile users and multi-calendar/org installs; fewer support tickets from photo backup failures.
  - Watch next: Core roadmap on WebSockets, bulk changefeeds; client-side perf budgets; benchmarks comparing REST vs WS on 4G/5G latency.
