# NixOS 25.11 released

- Score: 147 | [HN](https://news.ycombinator.com/item?id=46099022) | Link: https://nixos.org/blog/announcements/2025/nixos-2511/

### TL;DR
NixOS 25.11 “Xantusia” is out with seven months of support, deprecating 25.05 at year’s end. The release adds 7k+ new packages, updates ~25k, removes ~6k, and introduces 100+ new system modules plus many new options while pruning old ones. Major desktop and tooling updates include GNOME 49 (dropping X11 sessions) and LLVM 21, with GCC staying at 14. HN discussion centers on why stable releases matter, Nix’s power for infra, and ongoing usability/documentation challenges—especially on macOS.

---

### Comment pulse
- Stable channels matter → even with rollbacks, stable NixOS offers API/config stability for auto-updating machines; unstable risks silent data-migration breakage.
- Nix excels for infra engineers → reproducible environments and fast machine bootstrap are unmatched; some prefer it over Homebrew—counterpoint: others find macOS integration flaky and overkill versus Brew/mise.
- Onboarding is hard → terminology and flakes vs modules confuse newcomers; advice: start with plain NixOS in a VM, skip flakes initially, use focused tutorials.

---

### LLM perspective
- View: This release consolidates NixOS as a large, fast-moving yet curated ecosystem, with aggressive package churn and modern desktops/toolchains.
- Impact: Most value accrues to Linux devs/infra teams; macOS users still face fragmented tooling and weaker “official path.”
- Watch next: Better beginner docs, opinionated starter templates, and tools for safer updating/pinning will likely matter more than yet more packages.
