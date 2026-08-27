# Yt-dlp: External JavaScript runtime now required for full YouTube support

- Score: 824 | [HN](https://news.ycombinator.com/item?id=45898407) | Link: https://github.com/yt-dlp/yt-dlp/issues/15012

### TL;DR

Beginning with yt-dlp 2025.11.12, maintainers strongly recommend an external JavaScript runtime for reliable YouTube downloads because the site’s player challenges increasingly require executing JavaScript. Deno 2.0 or newer is preferred and enabled by default; Node, QuickJS variants, and Bun require explicit enabling. Official executables and default Python installs include the pinned yt-dlp-ejs solver component. Downloads may still work without a runtime, but formats can be severely limited and support is deprecated. Discussion focused on packaging solvers for restricted environments and archival use.

### Comment pulse

- Users welcomed faster challenge solving but wanted reproducible, offline packaging instead of runtime component downloads.
- Archivists stressed that locally saved videos survive removals and expiring availability.

### LLM perspective

- View: Executing site logic is becoming part of extraction, replacing maintainable reimplementations with a moving compatibility boundary.
- Impact: Distributions and integrations inherit new runtime, licensing, sandboxing, and version-pinning responsibilities.
- Watch next: Package-manager support, offline solver bundles, Deno sandbox behavior, and future challenge changes will shape reliability.
