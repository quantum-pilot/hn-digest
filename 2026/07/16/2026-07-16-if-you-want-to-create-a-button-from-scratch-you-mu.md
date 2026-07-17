# If you want to create a button from scratch, you must first create the universe

- Score: 225 | [HN](https://news.ycombinator.com/item?id=48930136) | Link: https://madcampos.dev/blog/2026/07/accessibility-from-scratch/

- TL;DR  
  The article walks through building a custom `<sagan-button>` web component that fully matches a native `<button>`: ARIA roles, labels, focus, mouse/touch/pointer/keyboard events, disabled and active states, form association, validation, event ordering, and new APIs like Popover. It ends up as ~500 lines of JavaScript that still only approximates native behavior, illustrating why “use semantic HTML first; don’t re‑implement controls with divs + ARIA” is practical, not dogma. HN extends this to UI history, missing widgets, and AI-generated code.

- Comment pulse  
  - OS-native widgets solved basic controls decades ago; the web endlessly re-skins them, trading speed and usability for aesthetics—counterpoint: closed stacks like Flash were worse long-term.  
  - Developers see the same anti-pattern in iOS (gestures instead of Button); debate whether LLMs will worsen accessibility or become powerful automatic a11y refactoring tools.  
  - Others note real gaps (e.g., combobox with server filtering) still force custom widgets; blame slow standards, Safari lag, and awkward Web Components ergonomics.

- LLM perspective  
  - View: Default to native HTML and ask models to “keep semantics, add styling,” not “build a custom widget from scratch.”  
  - Impact: Less JS, fewer a11y regressions, easier audits; especially important as agents start generating large UI codebases autonomously.  
  - Watch next: Standardized combobox/menu widgets, stronger built-in a11y linters, and framework tooling that wraps native controls instead of replacing them.
