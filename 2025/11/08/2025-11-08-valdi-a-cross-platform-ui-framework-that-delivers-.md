# Valdi – A cross-platform UI framework that delivers native performance

- Score: 468 | [HN](https://news.ycombinator.com/item?id=45852854) | Link: https://github.com/Snapchat/Valdi

- TL;DR
    Snapchat open-sourced Valdi, a cross-platform UI framework: write declarative TypeScript (TSX) once, compile to native views on iOS, Android, macOS—no webviews/bridges. It touts view pooling, viewport-aware rendering, a C++ layout engine, hot reload, VS Code debugging via Hermes, and polyglot modules with generated bindings to native code. Used internally for ~8 years; MIT-licensed, marked beta due to tooling/docs. HN compares it to React Native/Lynx, debates webview vs native tradeoffs and App Store limits, questions Swift/SwiftUI support, and community/distribution via Discord.

- Comment pulse
    - Web-first/WebView → avoid stores, ship faster; web covers notifications/GPS; HealthKit via small companion — counterpoint: App Store rejects site-wrappers; native gestures/features harder to match.
    - Valdi parallels React Native/Lynx → Hermes-based, hot reload, native bindings; RN adding AOT/JIT and generators; competition should lift developer experience and performance.
    - Adoption worries → Snapchat origin and Discord support; unclear Swift/SwiftUI story — counterpoint: docs claim Swift bindings; ex‑Snap engineers vouch for 8‑year production use.

- LLM perspective
    - View: Compelling native-first alternative if you want TypeScript ergonomics without bridges; success hinges on platform coverage and community depth.
    - Impact: Best fit for feature surfaces heavy on lists, gestures, animations; camera/AR-heavy apps must validate deep native integrations early.
    - Watch next: Independent benchmarks vs RN/Lynx, Swift/SwiftUI interop clarity, Windows/web roadmap, and signs of third‑party widgets, tooling, and governance.
