# Rust Coreutils 0.5.0 Release: 87.75% compatibility with GNU Coreutils

- Score: 90 | [HN](https://news.ycombinator.com/item?id=46264329) | Link: https://github.com/uutils/coreutils/releases/tag/0.5.0

### TL;DR
Rust Coreutils 0.5.0 advances its goal of being a drop-in replacement for GNU coreutils: 566 GNU tests now pass, yielding 87.75% test-suite compatibility, plus Unicode-aware text handling, checksum and install improvements, and broader CI coverage across OpenBSD, Redox and Cygwin. HN discussion focuses less on features and more on risk: whether ~88% compatibility is safe for distros to ship by default, the GPL→MIT license shift, and how much memory safety helps for these tools.

### Comment pulse
- Compatibility figure seems misleading; untested behavior and 12% known failures could still break scripts—counterpoint: shared tests have also uncovered real bugs in GNU coreutils.  
- Some fear replacing GPL GNU tools with MIT Rust ones lets vendors delay source for security fixes, weakening copyleft—counterpoint: others see GPL itself as undesirable.  
- Critics call a Rust rewrite needless for same-user CLI tools and prefer C hardening or Fil-C; supporters value memory safety, new tests and modernization.  

### LLM perspective
- View: Rust Coreutils is gradually becoming a practical drop-in, but distros should avoid defaulting to it before compatibility is effectively 100%.  
- Impact: If successful, it lowers long-term maintenance risk for ubiquitous tools and provides portable, memory-safe primitives for Rust-heavy userlands.  
- Watch next: track regression rates, performance versus GNU (and Fil-C builds), and how Ubuntu and others expose opt-out/rollback for conservative users.
