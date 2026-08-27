# Build Your Own React

- Score: 163 | [HN](https://news.ycombinator.com/item?id=46332526) | Link: https://pomb.us/build-your-own-react/

### TL;DR

Rodrigo Pombo’s interactive tutorial reconstructs a small React-like library, Didact, from JSX element creation through DOM rendering, interruptible work, fibers, commit phases, reconciliation, function components and a basic state hook. The implementation intentionally favors clarity over React’s optimizations, omitting keyed reconciliation, subtree skipping, effect lists, fiber reuse and update prioritization. Its main value is conceptual: matching familiar React names and call flow gives readers a tractable model for exploring the production codebase without pretending Didact is a replacement framework.

### Comment pulse

- Readers praised the animated, incremental presentation as unusually effective technical documentation, though fast scrolling can queue confusing animations.
- Several people used the tutorial’s concepts in alternative renderers, including backend JSX and a Python Tk implementation.

### LLM perspective

- View: Reimplementation works best here as a microscope for architecture, not a recipe for production React.
- Impact: The staged build makes fibers, reconciliation and hooks concrete enough to transfer into other rendering experiments.
- Watch next: Reader extensions for keyed children, effects and styles—and whether the presentation tooling improves rapid navigation.
