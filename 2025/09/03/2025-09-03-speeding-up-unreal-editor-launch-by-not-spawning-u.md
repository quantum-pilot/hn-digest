# Speeding up Unreal Editor launch by not spawning unused tooltips

- Score: 205 | [HN](https://news.ycombinator.com/item?id=45111273) | Link: https://larstofus.com/2025/09/02/speeding-up-the-unreal-editor-launch-by-not-spawning-38000-tooltips/

### TL;DR

Profiling revealed Unreal Editor eagerly constructed roughly 38,000 tooltip widget trees for a simple project, consuming about 40 MB and adding two to five seconds in debug builds or just under one second in development builds. The proposed patch stores tooltip text and creates a widget only when requested, where a single creation costs about 0.05 milliseconds. An update found around 20,000 tooltips came from two optional open panels—project settings and editor preferences—so layouts materially affect the result.

### Comment pulse

- Readers generalize the lesson: inspect invocation counts, not only expensive individual calls, because tiny costs compound across ubiquitous abstractions.
- Unreal users contrast its immense feature set and visual capabilities with slower iteration and developer experience than smaller engines.

### LLM perspective

- View: Laziness fits tooltips perfectly because potential UI inventory is enormous while human attention remains strictly serial.
- Impact: A contained allocation change can reduce startup time and memory without shifting noticeable latency into normal interaction.
- Watch next: Epic's pull-request decision, measurements across layouts and plugins, first-hover latency, caching, and similar eager widget construction.
