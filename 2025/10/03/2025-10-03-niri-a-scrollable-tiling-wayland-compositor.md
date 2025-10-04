# Niri – A scrollable-tiling Wayland compositor

- Score: 419 | [HN](https://news.ycombinator.com/item?id=45461500) | Link: https://github.com/YaLTeR/niri

TL;DR
- Niri is a Rust Wayland compositor built around scrollable tiling: windows live in columns on an infinite horizontal strip, so opening new ones never resizes others. Each monitor has its own strip and dynamic vertical workspaces. It’s stable, supports fractional scaling and NVIDIA, adds floating windows, gestures, tabs, live-reload config, accessibility, and integrated Xwayland via xwayland-satellite. HN users report “aha” workflow gains versus classic tilers, while skeptics prefer fixed, hotkeyed workspaces; requests include a scratch layer and lighter maintainer load.

Comment pulse
- Scrollable-strip model → shifts focus to topic-centric flows with unlimited windows; avoids layout churn; a “minimap” zoom helps avoid getting lost.
- Muscle-memory workspaces → instant Super+number jumps; scrolling risks window hunting — counterpoint: consistent strip order + overview maintain locality.
- Ecosystem and maintainership → PaperWM users switch due to fewer quirks; COSMIC/macos interest rising; Xwayland support improved; solo maintainer overloaded—donations and triage encouraged.

LLM perspective
- View: Scrollable tiling excels for deep, related multitasking; classic fixed workspaces remain superior for strict, muscle-memory switching.
- Impact: Expect pressure on COSMIC/others to offer scrollable layouts; improved Xwayland reduces migration friction for legacy apps.
- Watch next: Scratchpad layer, touchscreen gestures, config include/override release, NVIDIA/perf benchmarks, usability studies comparing navigation speed vs i3/sway.
