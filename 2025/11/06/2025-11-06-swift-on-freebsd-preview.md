# Swift on FreeBSD Preview

- Score: 165 | [HN](https://news.ycombinator.com/item?id=45837871) | Link: https://forums.swift.org/t/swift-on-freebsd-preview/83064

- TL;DR
  - Swift released a preview toolchain for FreeBSD 14.x (x86_64): a development compiler plus runtimes, requiring zlib‑ng, sqlite3, curl, libuuid, and python3. It’s pre‑release with gaps: TSan false positives, LLDB expression evaluation broken, SwiftPM command plugins hanging, C++ interop link errors, and libxml2 dependency issues; FreeBSD 15 needs compat14 libs. aarch64 is planned. HN welcomes broader Swift reach, debates Python’s role (LLDB/tests, not compiler), asks who will maintain FreeBSD ports, and notes containers/jails context.

- Comment pulse
  - Swift lags .NET in cross‑platform apps → .NET runs widely today; SwiftUI/UIKit won’t ship off‑Apple soon — counterpoint: community may build Android UI frameworks.
  - Python in dependencies is for LLDB scripting/tests → compiler/runtime don’t need it; LLVM lit is Python; Rust does similar.
  - Who maintains the FreeBSD ports package? → unclear; some want Swift team to own it to avoid volunteer delays and misdirected bug reports.

- LLM perspective
  - View: Swift’s FreeBSD preview signals a push beyond Apple devices, stress‑testing toolchain portability and surfacing ABI/tooling gaps early.
  - Impact: FreeBSD developers gain a first‑party Swift toolchain; package maintainers and CI/CD will adapt; debugging/testing workflows constrained until LLDB/TSan stabilize.
  - Watch next: Aarch64 builds, FreeBSD ports packages, clarified version‑support policy, and fixes for LLDB, TSan, SwiftPM plugins, C++ interop, and libxml2.
