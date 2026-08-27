# NixOS 25.11 released

- Score: 147 | [HN](https://news.ycombinator.com/item?id=46099022) | Link: https://nixos.org/blog/announcements/2025/nixos-2511/

### TL;DR

NixOS 25.11 “Xantusia” ships with seven months of support, while 25.05 reaches end of life after December 31, 2025. Its 2,742 contributors produced 59,430 commits, adding 7,002 packages and 107 modules while updating 25,252 packages and removing thousands of obsolete items. Highlights include GNOME 49, LLVM 21, GCC 14, and CMake 4. Commenters praised stable branches for configuration API stability and easy rollbacks, but noted data migrations, steep onboarding, and uneven nix-darwin experiences.

### Comment pulse

- Stable-branch value → configuration compatibility matters even when unstable builds evaluate and rollback cleanly.
- Operational caveat → application data migrations can defeat binary rollback or risk corruption.
- Adoption friction → powerful reproducibility competes with confusing terminology, sparse beginner guidance, and macOS integration complexity.

### LLM perspective

- View: NixOS’s release discipline stabilizes configuration interfaces, not merely package versions.
- Impact: Infrastructure teams gain reproducible fleets; newcomers still pay a substantial conceptual and documentation cost.
- Watch next: Review incompatibilities, migration behavior, GNOME’s X11 removal, and 25.05 upgrades before December’s deadline.
