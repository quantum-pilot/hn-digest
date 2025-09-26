# Electron-based apps cause system-wide lag on macOS 26 Tahoe

- Score: 235 | [HN](https://news.ycombinator.com/item?id=45376977) | Link: https://github.com/electron/electron/issues/48311

TL;DR
- macOS 26 Tahoe RC triggers severe system-wide stutter when any Electron app (e.g., Discord, VS Code) is merely open; minimizing restores smoothness. Electron maintainers suspect a macOS regression and request Feedback Assistant logs. HN sleuthing points to Electron overriding a private AppKit API for corner masking, likely colliding with Tahoe changes; similar lag appears in some non‑Electron apps. A per‑app workaround disables an Autofill heuristic but risks breaking autofill. A durable fix likely needs both Apple and Electron changes.

Comment pulse
- Not just Electron → Neovide, Zed, WezTerm also stutter on Tahoe; multiple regressions reported; GPU load and Autofill issues are distinct. Some projects shipped mitigations.
- Root cause → Electron’s private AppKit corner-masking hack collides with Tahoe changes — counterpoint: even so, macOS shouldn’t allow misbehaving apps to degrade system responsiveness.
- Workaround → Disable NSAutoFillHeuristicControllerEnabled per affected app; mitigates lag but may impair autofill. Expect Chrome/Chromium patches to propagate; file Feedback Assistant reports to Apple.

LLM perspective
- View: Likely macOS 26 regression exacerbated by Electron’s private AppKit usage; resolution needs Apple patch plus Electron removing fragile hooks.
- Impact: Slack, Discord, VS Code users on Tahoe see degraded UX; vendors must ship mitigations or pause macOS upgrades.
- Watch next: macOS 26.0.1 notes, Electron PRs removing private hooks, Chromium defaulting Autofill flag off, reproducible frame-pacing benchmarks.
