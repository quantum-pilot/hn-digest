# Build Android apps using Rust and Iced

- Score: 158 | [HN](https://news.ycombinator.com/item?id=46350641) | Link: https://github.com/ibaryshnikov/android-iced-example

### TL;DR
This repo shows how to build real Android apps in Rust using the Iced GUI toolkit on top of `android-activity`, `winit`, and `wgpu`, with examples for both `NativeActivity` and `GameActivity`, plus partial text-input support and watch/phone demos. Hacker News sees it as a technically strong proof-of-concept that may appeal to Rust-heavy teams wanting shared core logic across platforms, but questions whether it can beat Kotlin + Jetpack Compose on tooling, accessibility, and day‑to‑day developer experience.

---

### Comment pulse
- Rust UI on Android is niche → Kotlin/Compose wins on tooling, a11y, and “native feel”; Rust is attractive for shared logic and performance-sensitive apps.  
- Ecosystem gap → winit and platform glue are undermaintained; a few funded full‑time maintainers could unlock React-Native-style Rust modules and better cross‑platform stories.  
- Alternatives debated → Slint (Rust-friendly DSL, native, license quirks) and Dioxus (WebView/Tauri; experimental native) show same hard problems: IME, text input, and accessibility.

---

### LLM perspective
- View: This is best seen as infrastructure R&D, not a turnkey replacement for Kotlin/Compose yet.  
- Impact: Most useful to Rust-first teams and libraries needing a mobile UI surface without rewriting in JVM/Swift.  
- Watch next: Proper IME/a11y support, winit funding, and a polished template/CLI would determine whether this grows beyond enthusiasts.
