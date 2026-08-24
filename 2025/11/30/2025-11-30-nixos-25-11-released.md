# NixOS 25.11 released

- Score: 147 | [HN](https://news.ycombinator.com/item?id=46099022) | Link: https://nixos.org/blog/announcements/2025/nixos-2511/

### TL;DR

The latest stable NixOS release arrives with 59,430 commits from 2,742 contributors, adding 7,002 packages and updating 25,252 while removing 6,338. Its system modules gain 107 entries and 1,778 options. Major platform changes include GNOME 49 without X11 sessions, LLVM 21, GCC 14, and CMake 4. Support runs through June 30, 2026; the preceding release reaches end of life after December 31, 2025. Discussion emphasizes reproducibility, stable interfaces, and migration planning over novelty.

### Comment pulse

- Stable channels reduce surprise → predictable interfaces and updates matter when application data migrations cannot be rolled back with the operating system.
- Nix lowers environment drift → reproducible development and CI win praise — counterpoint: terminology, flakes, and cross-platform pinning remain steep.

### LLM perspective

- View: Release stability matters when it covers interfaces and stateful migrations, not merely packages that can be rolled back.
- Impact: Teams gain a larger supported package set, but GNOME’s X11 removal may force desktop workflow changes.
- Watch next: Early upgrades should reveal whether documentation and flake terminology remain the larger barrier than technical regressions.
