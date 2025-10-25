# The Swift SDK for Android

- Score: 276 | [HN](https://news.ycombinator.com/item?id=45698570) | Link: https://www.swift.org/blog/nightly-swift-sdk-for-android/

- TL;DR
    - Swift.org’s Android workgroup released nightly preview Swift SDK for Android, letting developers build Android apps and share Swift code across platforms. Guides/examples provided; swift-java generates Swift↔Java bindings. 25%+ of Swift packages already build for Android. HN discussion: focus on native Android UI with shared Swift business logic (Compose + Swift), not cross-platform UI; Skip bridges SwiftUI to Compose. Comparisons to Kotlin Multiplatform; skepticism about Apple’s long-term commitment and JVM interop complexity. Others praise the SDK model and open governance enabling community-led Android support.

- Comment pulse
    - Native UI shared logic wins → Compose/Views handle UX; Swift provides business code via swift-java, preserving feel — counterpoint: some want SwiftUI mapped to Compose.
    - Skip enables SwiftUI on Android → bridges SwiftUI to Jetpack Compose; supports native Swift execution (Fuse) and Kotlin transpilation (Lite); used in production demos.
    - Cautious optimism → SDK model shows community-led portability; but Apple follow-through questioned and JVM interop via JNI/FFI remains brittle for nontrivial semantics.

- LLM perspective
    - View: This positions Swift as a cross-platform core-logic language; UI stays native per platform until credible SwiftUI-to-Android mapping matures.
    - Impact: iOS-heavy teams can ship Android faster without Kotlin expertise; Android shops can consume Swift libraries without C++ bridges.
    - Watch next: Stabilized releases, toolchain CI, swift-java ergonomics and performance, Skip’s Compose bridge maturity, and any official guidance on UI interoperability.
