# Show HN: Homebrew 6.0.0

- Score: 1463 | [HN](https://news.ycombinator.com/item?id=48490024) | Link: https://brew.sh/2026/06/11/homebrew-6.0.0/

### TL;DR

Homebrew 6.0.0 focuses on security and speed: third-party taps now require explicit trust before arbitrary Ruby executes, an internal JSON API becomes default, and Linux gains Bubblewrap sandboxing. Brew Bundle installs formulae in parallel and expands npm, krew, cleanup, and Windows winget support; startup and upgrade paths are faster, while macOS 27 support begins. Intel Macs lose bottle/CI support in September 2026 and all support in September 2027. Hacker News praised the volunteer project’s longevity and Linux usefulness, while debating Mise as a lighter developer-tool alternative, cooldowns, and funding.

### Comment pulse

- Homebrew fills Linux’s userspace gap → commenters valued fresh, user-owned packages on immutable distributions without entangling system-package state.

- Mise excels at project-scoped tools → direct registries and multiple versions reduce packaging friction — counterpoint: dependencies and system-wide coverage remain uneven.

- Supply-chain delay deserves controls → users wanted minimum release ages; maintainers said cooldowns already cover riskier npm, PyPI, and RubyGems updates.

### LLM perspective

- **View:** Version 6.0 treats package metadata and third-party execution as distinct trust boundaries, reducing unnecessary code evaluation.

- **Impact:** Linux and WSL users gain a stronger cross-platform bootstrap layer; Intel Mac users face a firm migration clock.

- **Watch next:** Monitor tap-trust friction, sandbox compatibility, API speed, cooldown effectiveness, Intel fallout, and BrewUI readiness.
