# Kaiju – General purpose 3D/2D game engine in Go and Vulkan with built in editor

- Score: 138 | [HN](https://news.ycombinator.com/item?id=46205519) | Link: https://github.com/KaijuEngine/kaiju

## TL;DR
Kaiju is an open-source 2D/3D game engine written in Go on top of Vulkan, targeting Windows, Linux, Android and in-progress macOS, with a built-in editor and optional local-LLM integration. The author emphasizes high framerates and argues Go’s GC can coexist with real‑time rendering via careful design and low heap allocation. Hacker News discussion is intrigued by a Go engine but questions empty-scene FPS comparisons, potential cgo/Vulkan overhead, lack of shipped games, and whether GC-heavy stacks belong in core engines.

## Comment pulse
- Performance claims based on empty-scene FPS are dismissed as meaningless; commenters want game benchmarks, feature comparisons, and demos instead of “9x faster than Unity” slogans.  
- Many note GitHub overflows with engines because building tech is easier than finishing games, yet still defend engines as valuable learning tools and portfolio projects.  
- A camp insists GC and Go’s cgo overhead make serious engines nonstarters and predict a performance wall—counterpoint: others are optimistic about modern GC-tuned designs.  

## LLM perspective
- View: Treat Kaiju as an experimental Go/Vulkan lab, not a Unity replacement, until complex shipped games validate its architecture.  
- Impact: If it works, Kaiju could attract Go developers to real-time graphics and encourage more GC-friendly engine patterns and tooling.  
- Watch next: Published performance suites, cgo/Vulkan profiling results, macOS support maturity, and at least one documented production game using Kaiju.
