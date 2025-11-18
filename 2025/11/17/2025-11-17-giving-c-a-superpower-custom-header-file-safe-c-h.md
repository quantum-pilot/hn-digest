# Giving C a superpower: custom header file (safe_c.h)

- Score: 233 | [HN](https://news.ycombinator.com/item?id=45952428) | Link: https://hwisnu.bearblog.dev/giving-c-a-superpower-custom-header-file-safe_ch/

- TL;DR
  - A 600‑line header (safe_c.h) layers RAII and ergonomics onto C: scoped cleanup via compiler attributes, UniquePtr/SharedPtr, type-safe vectors/spans, Result-style errors, contracts, safer strings, and RAII mutex guards. The author’s cgrep uses these to be leak-free and thread-safe, and claims strong performance versus ripgrep. HN likes the idea but questions zero-cost claims (mutexed SharedPtr), correctness of “C23 cleanup,” and whether local RAII solves program-wide ownership/lifetimes. Some say just use C++; others value C’s simpler toolchains and hackability.

- Comment pulse
  - Mutex-based SharedPtr harms portability and cost → Use C11 atomics; C++ uses atomics; Rust splits Rc/Arc — counterpoint: overhead small; safety usually wins.
  - Local RAII ≠ global safety → Ownership transfer, copy semantics, and intrusive containers need discipline or types; otherwise xfree-style bugs persist.
  - “C23 [[cleanup]]” claim is inaccurate → It’s GCC’s [[gnu::cleanup]]; portability requires feature-detecting compilers and fallbacks.

- LLM perspective
  - View: Great ergonomics uplift for C; still lacks type-level ownership to prevent cross-scope lifetime bugs.
  - Impact: Useful for C-only/embedded/legacy teams wanting safer patterns without adopting C++/Rust toolchains.
  - Watch next: Atomics-based SharedPtr and Rc/Arc split; MSVC/Clang/GCC portability; audited benchmarks with sanitizers/PGO; documented ownership rules.
