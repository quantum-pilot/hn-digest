# Yt-dlp: External JavaScript runtime now required for full YouTube support

- Score: 824 | [HN](https://news.ycombinator.com/item?id=45898407) | Link: https://github.com/yt-dlp/yt-dlp/issues/15012

- TL;DR
  - yt-dlp’s 2025.11.12 release adds a hard dependency on an external JS runtime for full YouTube support. Deno is enabled and recommended by default; Node 20+ (25+ for sandboxing), QuickJS, and Bun are optional alternatives. The separate yt-dlp-ejs component drives challenge solving and is bundled in official builds. Without a runtime, YouTube extraction is deprecated and will degrade. HN reports smooth adoption (Arch packages, faster starts), requests offline solver prefetching, and notes YouTube’s growing restrictions (embed Referer enforcement), fueling renewed interest in personal archiving.

- Comment pulse
  - External runtime improves speed → deno solves challenges; solver auto-fetched. Packagers want prefetch — counterpoint: copy from cache, use AUR yt-dlp-ejs, or make yt-dlp-extra.
  - YouTube now enforces Referer for embeds → direct /embed fails with error 153; trend toward stricter tracking/DRM — counterpoint: trivial redirectors still bypass some checks.
  - Archiving is common → users hoard liked/ephemeral videos due to removals; others question value versus time, storage, and endless new content.

- LLM perspective
  - View: Aligns with YouTube’s JS-first checks; sandboxed runtimes keep capabilities without ballooning yt-dlp’s scope.
  - Impact: Packagers, GUIs, and distros must ship Deno/Node options; air‑gapped setups need prefetch workflows and pinned ejs versions.
  - Watch next: Track challenge changes, Node restricted-mode hardening, QuickJS performance; measure logged-in format failures; watch expansion beyond YouTube.
