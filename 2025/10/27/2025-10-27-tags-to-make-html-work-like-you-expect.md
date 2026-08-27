# Tags to make HTML work like you expect

- Score: 388 | [HN](https://news.ycombinator.com/item?id=45719140) | Link: https://blog.jim-nielsen.com/2025/dont-forget-these-html-tags/

### TL;DR

For a minimal HTML file that behaves predictably, the author recommends four declarations: an HTML5 doctype for standards mode, `lang` for screen readers and language-aware tools, UTF-8 metadata for correct character decoding, and a viewport setting so mobile browsers render at device width. Server headers can provide the charset, but embedding it helps local files. The deliberately simple checklist prompted useful additions such as semantic `main` and `nav` elements, plus discussion of quirks mode, invalid-but-tolerated minifier output and comfortable reading widths.

### Comment pulse

- HN itself reportedly omits a doctype and renders in quirks mode, illustrating the compatibility behavior under discussion.
- Readers noted semantic landmarks help assistive technology even when they do not change visual rendering.

### LLM perspective

- View: A tiny explicit baseline prevents legacy defaults from silently shaping accessibility, encoding and mobile layout.
- Impact: These declarations reduce environment-specific surprises without requiring a framework or comprehensive boilerplate.
- Watch next: Validators should catch aggressive minification that browsers tolerate but the authoring specification rejects.
