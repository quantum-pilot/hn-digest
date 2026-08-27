# Kaiju – General purpose 3D/2D game engine in Go and Vulkan with built in editor

- Score: 138 | [HN](https://news.ycombinator.com/item?id=46205519) | Link: https://github.com/KaijuEngine/kaiju

### TL;DR

Kaiju is a heavily developed 2D/3D engine using Go and Vulkan, with Windows, Linux, functional Android, work-in-progress macOS, local-model interoperability, and an unfinished editor. Its README calls the engine production-ready and claims much faster rendering and lower memory than established engines, citing 5,400 FPS for an empty cube scene versus Unity’s 1,600. HN welcomed experimentation with garbage-collected game engines but rejected that microbenchmark as evidence of practical superiority, citing missing features, cgo overhead, scarce game demonstrations, and no published releases.

### Comment pulse

- Empty-scene FPS measures little beyond baseline overhead → frame times, features, realistic scenes, and stable pacing matter more than headline ratios.
- Building engines remains valuable without shipping games → it teaches performance engineering, though real projects force missing trade-offs.
- Go’s garbage collector is not automatically disqualifying → counterpoint: Vulkan FFI overhead and complex-scene behavior need credible measurement.

### LLM perspective

- View: Kaiju’s interesting proposition is productive managed-language engine development; its performance marketing currently outruns supplied evidence.
- Impact: Indie developers need demonstrated workflows and shipped games more than isolated rendering throughput.
- Watch next: Publish releases, representative benchmarks, frame-time distributions, memory traces, platform support, editor stability, and complete game case studies.
