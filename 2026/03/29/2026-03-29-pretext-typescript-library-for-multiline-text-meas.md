# Pretext: TypeScript library for multiline text measurement and layout

- Score: 172 | [HN](https://news.ycombinator.com/item?id=47556290) | Link: https://github.com/chenglou/pretext

### TL;DR

Pretext is a TypeScript library that predicts multiline text height and line breaks without DOM measurement or reflow. `prepare()` segments and measures text once through the browser’s canvas font engine; cached widths then let `layout()` use arithmetic, with a benchmark reporting about 19 ms and 0.09 ms respectively for 500 texts. It supports multilingual, emoji, bidirectional and pre-wrapped content, plus fixed- or variable-width manual layout for DOM, Canvas, SVG, and WebGL. Its CSS model is intentionally narrow, server-side rendering remains planned, and named fonts are required for reliable macOS results.

### Comment pulse

- Developers emphasized the difficulty of matching Chinese, emoji, hyphenation, bidirectional text, and Safari-specific behavior across a broad corpus.
- Demos failed visibly on one Fedora/Firefox system — counterpoint: supporters see such discrepancies as exactly the maintenance burden Pretext tackles.
- Some showcased effects now have CSS solutions; commenters still saw unsolved text-measurement APIs as candidates for browser standardization.

### LLM perspective

- **View:** Separating expensive shaping from cheap repeated wrapping is the library’s practical architectural win.
- **Impact:** Reliable premeasurement improves virtualization, scroll anchoring, responsive composition, and browser-free overflow checks.
- **Watch next:** Cross-browser accuracy drift, font loading, CSS coverage, server-side support, and standards-track equivalents.
