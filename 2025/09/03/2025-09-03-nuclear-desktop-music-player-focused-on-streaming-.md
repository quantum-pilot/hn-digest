# Nuclear: Desktop music player focused on streaming from free sources

- Score: 383 | [HN](https://news.ycombinator.com/item?id=45117230) | Link: https://github.com/nukeop/nuclear

- TL;DR
  - Nuclear is an AGPL desktop player that streams music from free sources (YouTube, SoundCloud, Jamendo, Audius) with playlists, scrobbling, lyrics, and SponsorBlock, no accounts/ads. The current Electron app is largely unmaintained; a rewrite (nuclear-xrd) switches to Tauri and Rust, adds auto‑updates, theming, and a plugin system. HN reactions mix amusement at edgy testimonials/LLM jokes with concerns: high RAM use, playback failures, and JavaScript errors. Some report success via different providers/playlists. Several want an open-source client that fronts major paid services.

- Comment pulse
  - Anti-artist vibe hurts project → homepage highlights a musician condemning it; README includes LLM gag—counterpoint: some find the irreverence funny and on-brand.
  - Electron bloat is real → users report ~300MB at startup; others say acceptable and rewrite to Tauri/Rust should cut footprint.
  - Unreliable playback → many songs fail with JS errors; some succeed by switching providers or using playlists, highlighting brittle scrapers.

- LLM perspective
  - View: The rewrite’s Tauri+Rust+plugins path is sensible to reduce resource use and isolate fragile provider integrations.
  - Impact: Lower memory and auto-updates could revive desktop adoption; plugin ecosystem attracts contributors; legal friction with YouTube-like sources may persist.
  - Watch next: nuclear-xrd alpha builds, playback reliability metrics, CPU/RAM benchmarks versus Electron, provider coverage breadth, and moderation/governance choices.
