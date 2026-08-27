# Font with Built-In Syntax Highlighting (2024)

- Score: 124 | [HN](https://news.ycombinator.com/item?id=46364131) | Link: https://blog.glyphdrawing.club/font-with-built-in-syntax-highlighting/

### TL;DR

The author embeds lightweight HTML, CSS, and JavaScript syntax highlighting inside a modified Monaspace color font. OpenType COLR glyph palettes supply colors, while contextual alternates substitute colored glyphs when character sequences resemble keywords, tags, functions, strings, or comments. This keeps source text plain, eliminates page scripts, and uniquely works inside textareas, but it is not a parser: keywords can color ordinary prose, multiline state breaks at manual line endings, language changes require rebuilding the font, and PowerPoint lacks support.

### Comment pulse

- The technique is an inventive constraint exercise → build-time DOM highlighting remains more accurate for static blogs.
- Textareas are the compelling niche → native editing, search, undo, and plain text can coexist with color.
- Parser limits are decisive → losing context across newlines blocks common strings, templates, and multiline comments.

### LLM perspective

- View: Font shaping can provide zero-markup lexical hints, but it cannot reliably replace language-aware parsing.
- Impact: Small sandboxes and editable fields gain highlighting without contenteditable or injected spans.
- Watch next: A HarfBuzz-WASM parser could test whether accuracy improves without sacrificing native textarea behavior.
