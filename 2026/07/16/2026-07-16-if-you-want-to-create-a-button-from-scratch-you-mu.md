# If you want to create a button from scratch, you must first create the universe

- Score: 225 | [HN](https://news.ycombinator.com/item?id=48930136) | Link: https://madcampos.dev/blog/2026/07/accessibility-from-scratch/

### TL;DR

A thought experiment rebuilds an HTML button as a custom element to show why semantic markup matters. Matching the native control requires labeling, focus, pointer and keyboard activation, disabled and active states, event cancellation, form submission/reset, attributes, values, and validation—nearly 500 JavaScript lines, still without newer popover and command APIs. A native `<button>` provides this behavior with no JavaScript and preserves user expectations. HN broadly agreed, while noting developers often go custom because browsers lack richer controls, branding pushes cross-platform consistency, and LLM accessibility depends heavily on prompting.

### Comment pulse

- Native defaults encode institutional memory → behavior, accessibility, and performance arrive together — counterpoint: bespoke visual identity keeps teams rebuilding controls across platforms.
- Missing primitives force customization → server-filtered comboboxes exceed basic HTML — counterpoint: shimming native behavior remains safer than discarding it wholesale.
- LLM accessibility experience varied → some saw inaccessible defaults; others obtained strong screen-reader improvements after explicitly requesting an audit.

### LLM perspective

- **View:** Native elements are compatibility contracts spanning input methods, assistive technology, forms, event semantics, and continuing browser evolution.
- **Impact:** Reimplementation transfers platform maintenance onto product teams, where rare interactions and future APIs become recurring correctness debt.
- **Watch next:** Customizable native controls, cross-browser consistency, automated accessibility tests, and whether coding agents choose semantic elements by default.
