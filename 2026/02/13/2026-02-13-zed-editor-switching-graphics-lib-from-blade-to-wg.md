# Zed editor switching graphics lib from blade to wgpu

- Score: 277 | [HN](https://news.ycombinator.com/item?id=47002825) | Link: https://github.com/zed-industries/zed/pull/46758

## TL;DR
Zed has replaced its custom Blade-based Linux renderer in GPUI with wgpu, the de‑facto Rust graphics abstraction. Blade was causing serious stability problems, especially on NVIDIA + Wayland, and wgpu lets Zed piggyback on a broader ecosystem (Bevy, Iced, etc.) and future driver work. The change currently targets Linux only; native Metal/DirectX renderers remain for macOS/Windows due to performance and memory concerns. HN discussion zooms out to Rust GUI’s fragility, GPUI’s de-prioritization, and Zed’s place as a fast VS Code–class editor.

## Comment pulse
- Rust GUI ecosystem is immature and under-resourced → core crates stagnate, so apps choose between incomplete frameworks, convoluted architectures, or retreating to stacks like Qt/WPF.  
- Zed is pausing GPUI-as-a-library work → company prioritizes editor features; community fork (gpui‑ce) may carry general-purpose UI needs, but maintainer time is uncertain.  
- Zed targets “fast VS Code” more than JetBrains-level IDE → users praise speed, stability, and moderate AI integration—counterpoint: some miss advanced refactoring and language-specific tooling.  

## LLM perspective
- Aligning Linux rendering with wgpu reduces bespoke graphics code, but increases reliance on a still-evolving cross-platform abstraction layer.  
- Most immediate beneficiaries are Linux users on Wayland/NVIDIA; they trade Blade’s instability for wgpu’s broader testing and possible VRAM overhead.  
- Watch GPUI‑ce’s momentum, wgpu desktop regressions/optimizations, and whether Zed’s roadmap turns “web client” from aspiration into funded project.
