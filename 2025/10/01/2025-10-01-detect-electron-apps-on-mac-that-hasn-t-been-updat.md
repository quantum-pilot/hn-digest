# Detect Electron apps on Mac that hasn't been updated to fix the system wide lag

- Score: 152 | [HN](https://news.ycombinator.com/item?id=45437112) | Link: https://gist.github.com/tkafka/e3eb63a5ec448e9be6701bfd1f1b1e58

- TL;DR
  - A community script scans macOS apps to flag Electron builds that cause system-wide lag on Tahoe by checking Electron version and the _cornerMask symbol. It lists affected apps and suggests a CHROME_HEADLESS env var as a temporary workaround (disables window shadows). Fixes landed in 36.9.2, 37.6.0, 38.2.0, and 39.0.0+. HN reports many apps still laggy, with some fast updates (SiYuan, Obsidian). Discussion covers localization quirks in search, forked Electron builds, and more robust detectors.

- Comment pulse
  - Update cadence → Ollama GUI seemed outdated; others say latest mac app isn't laggy and fixes were backported — counterpoint: updater behavior remains inconsistent.
  - Detection method → Forked Electron builds may cherry-pick fixes; scanning for _cornerMask in binaries is more reliable than version checks.
  - Field reports → SiYuan updated; Obsidian fixed via full reinstall; many apps still affected, prompting some users to uninstall seldom-used ones.

- LLM perspective
  - View: Treat Electron as a fast-moving dependency; automate audits for problematic symbols across builds before shipping.
  - Impact: Dev teams must rebuild and notarize quickly; IT admins can script fleet-wide checks; users may switch to native alternatives.
  - Watch next: Vendor releases on fixed Electron lines, auto-update reliability, Apple-side patch reducing susceptibility to window-shadow regressions.
