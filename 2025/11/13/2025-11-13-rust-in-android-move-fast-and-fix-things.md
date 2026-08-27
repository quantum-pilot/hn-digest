# Rust in Android: move fast and fix things

- Score: 253 | [HN](https://news.ycombinator.com/item?id=45918616) | Link: https://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

### TL;DR

Google reports that Android’s roughly five million lines of Rust have produced one potential memory-safety vulnerability, fixed before release, and estimates more than 1,000-fold lower vulnerability density than its C/C++ code. For similarly sized changes, Rust reportedly requires 20% fewer revisions, spends 25% less time in review, and has about one-quarter the rollback rate. A hardened allocator blocked the unsafe-Rust overflow. Discussion praised the delivery metrics but raised selection bias: Rust is newer code, while C++ changes often touch older systems.

### Comment pulse

- Readers found reduced rollbacks and review time as persuasive as the headline security comparison.
- Some noted Android still lacks official Rust userspace tooling through its NDK and Android Studio.

### LLM perspective

- View: Google’s internal data makes memory safety look like a delivery advantage, not merely defensive engineering.
- Impact: Organizations can justify Rust adoption through operational stability even when security savings feel abstract.
- Watch next: Age-adjusted comparisons and broader tooling support would test whether results transfer beyond Android’s internal environment.
