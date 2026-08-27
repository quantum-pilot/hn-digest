# Build Android apps using Rust and Iced

- Score: 158 | [HN](https://news.ycombinator.com/item?id=46350641) | Link: https://github.com/ibaryshnikov/android-iced-example

### TL;DR

A sample repository demonstrates Android applications built in Rust with Iced through NativeActivity and GameActivity. It combines Android Activity support with winit and wgpu, layering Iced onto an existing graphics pipeline because Iced lacks direct Android support. The examples build through cargo-ndk and include phone and watch previews. Text input remains incomplete: soft-keyboard resizing, language switching, and IME are unresolved, while clipboard and keyboard visibility require Java calls. Commenters see potential for shared Rust code but emphasize tooling, accessibility, and platform-integration gaps.

### Comment pulse

- Performance-sensitive or Rust-heavy applications may benefit; typical apps retain stronger Kotlin and Compose tooling.
- Iced currently lacks built-in accessibility, while foundational Android integration and text input need sustained maintainership.

### LLM perspective

- View: The repository proves rendering integration, not production parity with native Android UI stacks.
- Impact: Rust teams can prototype shared interfaces, but accessibility and IME gaps constrain deployable applications.
- Watch next: Track GameActivity input support, accessibility semantics, lifecycle reliability, and device-wide testing.
