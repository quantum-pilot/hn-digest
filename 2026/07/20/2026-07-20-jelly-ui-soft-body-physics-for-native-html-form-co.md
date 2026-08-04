# Jelly UI: Soft-body physics for native HTML form controls

- Score: 296 | [HN](https://news.ycombinator.com/item?id=48981620) | Link: https://jelly-ui.com/

### TL;DR

Jelly UI is a dependency-free library of 40 Web Components that adds soft-body animation to familiar HTML controls through one module script. It ships with dark mode, right-to-left support, WCAG AA color tokens, reduced-motion behavior, and an MIT license. HN liked the playful polish but tested its engineering and UX: commenters debated whether the shared animation loop repaints too aggressively, found inconsistent drag-away clicking, and noted that reduced-motion users could mistake the demo for broken. The author fixed the click behavior and added an animation override and notice.

### Comment pulse

- Animation-loop criticism met profiling evidence → one reader feared full-page repainting — counterpoint: the engine tracks only active components and appeared idle efficiently.
- Native-control semantics remain the benchmark → drag-away release behaved inconsistently, reinforcing how tiny interaction details complicate custom widgets; the author fixed it.
- Playfulness divided users → animation can clarify state changes — counterpoint: others prefer interfaces that stay quiet, and reduced-motion users need visible controls.

### LLM perspective

- **View:** Motion earns its place when it reinforces state without changing familiar control semantics or delaying interaction.
- **Impact:** Easy installation lowers adoption friction, but animation makes performance, accessibility, and behavioral consistency central library obligations.
- **Watch next:** Benchmark busy pages, test input edge cases, expose motion controls, and verify every element against native behavior.
