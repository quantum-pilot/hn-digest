# Did you read the quarter-million-line license for your Slack app?

- Score: 103 | [HN](https://news.ycombinator.com/item?id=45308503) | Link: https://mastodon.mit.edu/@Eggfreckles/114825126857396420

- TL;DR
  - The scary quarter‑million‑line license tied to Slack is mostly the concatenated open‑source licenses bundled with Chromium inside its Electron app, not Slack’s ToS. The bulk comes from hundreds of dependencies repeating standard licenses. HN debates software bloat and developer convenience, questions why licenses are not deduplicated, and calls the title misleading. Others argue for owning software and self‑hosting chat, citing Matrix/Element, Zulip, and Once’s Campfire, and warn about entrusting business data to opaque, ever‑changing SaaS.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - It’s third-party OSS licenses, not Slack’s ToS → Electron/Chromium bundles hundreds of deps with repeated texts, creating huge notices — counterpoint: deduplication tooling could shrink it.
  - Modern Electron apps are wasteful → past 10MB PCs did office, dev, games; developer convenience prioritized over efficiency — counterpoint: cross‑platform frameworks accelerate features.
  - Prefer owning/self‑hosting chat → control data and uptime; options cited: Matrix/Element, Zulip, Once’s Campfire — counterpoint: personal cloud ownership is ambiguous.

- LLM perspective
  - View: Debate mixes license-notice confusion with broader frustration at Electron bloat and SaaS control.
  - Impact: Enterprises and teams reassess chat stacks; some shift to self-hosted or lighter clients; vendors clarify licensing files.
  - Watch next: SBOM standards, license-text dedup tools, Electron alternatives (Tauri, native wrappers), and one-time-purchase SaaS experiments gaining or losing traction.
