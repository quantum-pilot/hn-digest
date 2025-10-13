# Show HN: Rift – A tiling window manager for macOS

- Score: 195 | [HN](https://news.ycombinator.com/item?id=45553995) | Link: https://github.com/acsandmann/rift

- TL;DR
  - Rift is a new Rust-based tiling window manager for macOS that prioritizes speed, polish, and native feel: i3/BSP layouts, animated moves, Mission Control-like workspace view, focus-follows-mouse, hot-reload config, trackpad workspace gestures, and Sketchybar/CLI/Mach integration. It works with “Displays have separate Spaces” and doesn’t require disabling SIP, but is pre-release and built on private APIs. HN split: many stick with lightweight window placement tools (Rectangle/Moom) for simplicity; others argue true tiling shines with multi-window workflows and 5K/ultrawide monitors; devs discuss Accessibility API/Rust viability.

- Comment pulse
  - Snapping often beats tiling → Rectangle/Moom meet ~80% needs with minimal setup — counterpoint: tiling cuts context switching in multi-window workflows.
  - High‑res/ultrawide users need finer grids → standard tiling leaves oversized panes; tools like Moom/komorebi offer custom partitions; consistent hjkl bindings desired.
  - Building WMs on macOS is viable → Accessibility framework plus Rust/objc2 bindings suffice; debugging mostly with docs and rust‑analyzer, no heavy Xcode setup.

- LLM perspective
  - View: Rift blends tiling power with macOS-native affordances (Spaces, gestures, animations) without SIP compromises.
  - Impact: Devs on Macs gain repeatable layouts and automation while keeping Mission Control workflows; power users may switch from Aerospace/yabai.
  - Watch next: Stability under Sonoma/Sequoia updates, grid presets for 5K/ultrawide, keybinding customization, performance vs Aerospace/yabai in latency and CPU.
