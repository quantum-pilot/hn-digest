# Fine, I'll build my own text editor

- Score: 242 | [HN](https://news.ycombinator.com/item?id=49524863) | Link: https://dbushell.com/2026/09/01/text-editor/

### TL;DR

An experiment in browser-based text editing moves from fully custom Canvas rendering to plaintext contenteditable and finally a textarea. Canvas offered visual control but required reimplementing selection, history, scrolling, input, and accessibility. Contenteditable restored native behavior but developed unpredictable performance at larger sizes; textarea performed better, with a separate visible layer for syntax highlighting. The author pauses at a promising prototype, noting remaining virtualization, tab handling, and UTF-16 grapheme pitfalls. Commenters celebrate editor construction while favoring native controls and sustained optimization.

### Comment pulse

- Native textarea wins early → decades of browser engineering provide selection, undo, input behavior, accessibility, and consistent performance.
- Editors invite reinvention → their visible mechanics are satisfying, but mature behavior hides enormous edge-case complexity.
- Performance debt compounds → commenters reject assuming future hardware will erase inefficiency, especially when workloads expand alongside capacity.

### LLM perspective

- View: Starting with semantic native controls preserves accessibility and lets custom rendering focus on genuine differentiation.
- Impact: Browser editor authors can prototype quickly without inheriting Canvas’s complete input and selection burden.
- Watch next: Benchmark large files, grapheme editing, IME input, screen readers, highlighted ranges, and virtualized scrolling across engines.
