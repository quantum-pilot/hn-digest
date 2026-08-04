# Show HN: Edsger – A handwritten Clojure REPL for the reMarkable 2

- Score: 233 | [HN](https://news.ycombinator.com/item?id=48374552) | Link: https://handwritten.danieljanus.pl/2026-06-01-edsger.html

### TL;DR

Edsger turns a reMarkable 2 notebook into a stylus-driven “almost Clojure” REPL. A Go process polls Xochitl’s proprietary page files, diffs new strokes, renders them for Claude Sonnet 4.6 transcription, evaluates the expression locally, then injects a Dijkstra-handwriting-style result image below it through an XOVI/QML plugin. Everything except OCR runs on-device. The workflow is deliberately artistic rather than practical: responses take roughly 14 seconds, mostly because Xochitl waits about 12 seconds to save. HN treated it as successful hack art while focusing on latency and alternative architectures.

### Comment pulse

- The filesystem is the bottleneck → direct framebuffer consumption could observe strokes immediately, bypassing Xochitl’s delayed notebook persistence.
- A canonical notebook could improve portability → store handwriting, transcription, and output separately, then render them onto the tablet or PDF.
- Impracticality is part of the appeal → commenters saw the build as art and a demonstration of reMarkable’s root-accessible Linux openness.

### LLM perspective

- **View:** Piggybacking on Xochitl trades implementation effort for latency; replacing its UI stack reverses that trade.
- **Impact:** Open tablet access enables experimental interfaces that closed mobile ecosystems make prohibitively difficult.
- **Watch next:** On-device stroke recognition, event-driven IPC, save-bypass hooks, and measured latency by pipeline stage.
