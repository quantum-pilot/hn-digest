# Kaiju – General purpose 3D/2D game engine in Go and Vulkan with built in editor

- Score: 138 | [HN](https://news.ycombinator.com/item?id=46205519) | Link: https://github.com/KaijuEngine/kaiju

### TL;DR

Kaiju is a work-in-progress 2D and 3D engine written in Go and backed by Vulkan, with a built-in editor, Windows, Linux, and Android support, a Mac port underway, and local-model interoperability. Its README calls the engine production-ready but the editor unfinished, while the repository shows no published releases. It claims high frame rates, low memory use, and minimal garbage-collector pressure. Commenters welcomed managed-language experimentation but rejected empty-scene FPS comparisons, wanted shipped games and representative workloads, and raised Go-to-Vulkan FFI concerns.

### Comment pulse

- Critics noted FPS is nonlinear: reducing an empty frame below one millisecond says little about performance once real workloads dominate.
- Engine building was dismissed as avoiding product tradeoffs — counterpoint: others value it as education, portfolio work, and a distinct technical craft.
- Skeptics called garbage collection and cgo overhead disqualifying; supporters saw modern managed runtimes as promising when allocation pressure is controlled.

### LLM perspective

- View: Kaiju is an ambitious engineering project whose performance marketing currently outruns the supplied evidence.
- Impact: It could broaden Go’s role in game tooling if real projects validate editor usability and runtime consistency.
- Watch next: Versioned releases, reproducible frame-time benchmarks, complex scenes, shipped games, Mac support, GC pauses, and FFI profiles.
