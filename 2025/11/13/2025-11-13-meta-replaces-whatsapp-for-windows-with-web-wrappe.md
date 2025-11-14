# Meta replaces WhatsApp for Windows with web wrapper

- Score: 405 | [HN](https://news.ycombinator.com/item?id=45910347) | Link: https://www.windowslatest.com/2025/11/12/meta-just-killed-native-whatsapp-on-windows-11-now-it-opens-webview-uses-1gb-ram-all-the-time/

- TL;DR
  - Meta replaced WhatsApp’s Windows 11 app with a WebView2 wrapper that simply loads WhatsApp Web. Benchmarks in the article show 300MB at login, ~1.2GB idle, spiking to ~2–3GB when syncing, plus sluggish UI and unreliable notifications. The switch (v2.2584.3.0) will log users out of the native UWP client and force migration. HN threads blame big‑company coordination and Windows’ unstable native frameworks; others note the UWP client was buggy anyway. Debate centers on performance regressions, feature parity, and incentives favoring web rewrites.

- Comment pulse
  - Coordination cost at scale → One codebase accelerates feature rollout; Windows lacks a consistent “native feel”. — counterpoint: Small teams routinely ship performant cross‑platform natives.
  - Usage incentives → Desktop WhatsApp is low priority; previous Facebook Windows apps saw <1% usage versus web, so native investment doesn’t justify coordination overhead.
  - Quality/perf tradeoff → Old UWP was crashy with input/accents bugs; web wrapper feels smoother for some but introduces sluggishness and Windows notification inconsistencies.

- LLM perspective
  - View: This is a classic consolidation move: prioritize web parity and experimentation speed over platform integration and efficiency on lower-end PCs.
  - Impact: Heavy RAM/CPU hits affect corporate fleets, battery life, and multitasking; some users will switch to browser tabs or third-party clients.
  - Watch next: Memory fixes, WebView2 optimizations, restored call integration, or a PWA option; ratings and enterprise feedback may push Meta to adjust.
