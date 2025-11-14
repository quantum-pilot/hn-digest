# Rust in Android: move fast and fix things

- Score: 253 | [HN](https://news.ycombinator.com/item?id=45918616) | Link: https://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

TL;DR
Google says Rust is making Android both safer and faster. Memory-safety bugs dropped below 20% overall; Rust shows ~1000x lower memory-safety bug density than C/C++ (0.2 vs ~1000 per MLOC). Rust changes get ~25% shorter reviews, ~20% fewer revisions, and ~4x fewer rollbacks. A Rust buffer-overflow near-miss (CVE-2025-48530) was neutralized by Android’s Scudo allocator and fixed pre-release. Rust is expanding into Linux kernel 6.12 drivers, firmware, and security-critical apps/Chromium. HN cheers the data, questions some numbers, and notes tooling gaps.

Comment pulse
- Rust improves throughput and stability → 25% faster reviews, ~20% fewer revisions, ~4x fewer rollbacks; developers like compile-time guarantees — counterpoint: C++ changes skew older/riskier.
- Security gains look massive → claimed ~1000x lower memory-safety density (0.2 vs ~1000/MLOC); Scudo guard pages turned a Rust overflow into a crash.
- Adoption/tooling tension → Rust praised over CMake/C++ and desired for Android apps, yet no first-class NDK/Android Studio tooling today.

LLM perspective
- View: Metric-backed evidence shows Rust reduces both vulnerabilities and operational drag; prioritize Rust for new system components.
- Impact: Fewer rollbacks reduce cross-team churn; OEMs and partners must adopt Scudo and invest in unsafe-Rust training.
- Watch next: First-class Android Rust tooling, kernel driver uptake, third-party audits of bug-density claims, and measurable firmware exploit-rate changes.
