# Show HN: Homebrew 6.0.0

- Score: 1463 | [HN](https://news.ycombinator.com/item?id=48490024) | Link: https://brew.sh/2026/06/11/homebrew-6.0.0/

- TL;DR  
Homebrew 6.0 brings a new tap‑trust model, a faster internal JSON API, Linux sandboxing, safer “ask”‑by‑default installs, and many brew bundle and cask improvements. Security gets special focus: multiple installer vulnerabilities are fixed, high‑risk ecosystems gain release cooldowns, common install steps move into declarative metadata, and a brew vulns subcommand plus new supply‑chain docs arrive. HN readers praise Homebrew’s longevity and Linux usability, debate alternatives like mise and Nix, discuss update‑cooldown policies, and resolve to donate.

- Comment pulse  
  - Homebrew still beloved → commenters laud Mike McQuaid’s 17‑year stewardship and prefer Homebrew even on Linux for clear user/system separation and fresher packages.  
  - Alternatives explored → some switch to mise (with asdf/aqua) or Nix for per‑project toolchains and arbitrary versions—counterpoint: others hit ecosystem gaps and reverted to Brew.  
  - Security cadence debated → users request user‑configurable cooldowns or channels; maintainers highlight new built‑in cooldowns for risky registries and Homebrew’s maintainer‑mediated rolling‑release model.

- LLM perspective  
  - View: Homebrew is clearly repositioning as a cross‑platform, userspace package substrate rather than just “MacPorts but nicer”.  
  - Impact: Golden Gate dropping Intel plus Homebrew’s timeline will accelerate Apple‑silicon‑only tooling; Intel‑bound workflows should plan migration or containerization.  
  - Watch next: Measure tap‑trust, install‑steps, and internal API on large Brewfiles to verify if security refactors also significantly reduce real‑world install times.
