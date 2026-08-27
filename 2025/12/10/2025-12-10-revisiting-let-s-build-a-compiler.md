# Revisiting "Let's Build a Compiler"

- Score: 250 | [HN](https://news.ycombinator.com/item?id=46214693) | Link: https://eli.thegreenplace.net/2025/revisiting-lets-build-a-compiler/

### TL;DR

Eli Bendersky modernizes Jack Crenshaw’s enduring compiler tutorial by translating its Pascal implementations to Python and replacing Motorola 68000 assembly with WebAssembly, backed by executable tests. He attributes the original’s appeal to building a hand-written recursive-descent parser incrementally and generating runnable code early instead of front-loading theory. Its direct syntax-directed translation remains excellent for learning, but becomes restrictive around types and optimization; Bendersky suggests introducing an AST and analysis phase near the tutorial’s type chapter. Commenters endorsed complete vertical slices before sophistication.

### Comment pulse

- Readers valued reaching executable code early because it turns a seemingly large system into testable, understandable primitives.
- Direct emission teaches fundamentals — counterpoint: IR enables serious optimization, register allocation, and richer analysis once the language grows.

### LLM perspective

- View: The best beginner compiler exposes the entire pipeline quickly, then lets its own limitations motivate additional phases.
- Impact: Modern targets remove obsolete setup while preserving the tutorial’s strongest lesson: build working vertical slices.
- Watch next: A follow-on chapter transitioning the tested WebAssembly compiler from direct emission to AST-based type analysis.
