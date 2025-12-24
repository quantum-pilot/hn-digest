# Font with Built-In Syntax Highlighting (2024)

- Score: 124 | [HN](https://news.ycombinator.com/item?id=46364131) | Link: https://blog.glyphdrawing.club/font-with-built-in-syntax-highlighting/

### TL;DR
The author modifies the Monaspace Krypton font to embed syntax highlighting directly into the font itself using OpenType color glyphs (COLR) and contextual alternates. Keywords, strings, comments, and function names in HTML/CSS/JS are detected via elaborate substitution rules, so plain `<code>` text gets colored without JavaScript, extra spans, or build steps—highlighting even works in `<textarea>`. Limitations include basic pattern matching, no cross-line context, awkward extensibility (font editing required), and dependence on OpenType support; future work might use harfbuzz-wasm for real parsing.

### Comment pulse
- Clever technical stunt → Feels like bootloader-sized code-golf; most prefer generators or JS highlighters for maintainability—counterpoint: static blogs benefit from zero-build, zero-JS snippets.  
- Questioning “bloat” → Some see moving logic into fonts as just relocating complexity; others note OpenType rules aren’t scripts and preserve static HTML.  
- Practicality concerns → Textarea highlighting and web editors are exciting, but missing multiline context and PowerPoint support make it unsuitable for many real workflows.

### LLM perspective
- View: A smart abuse of OpenType showing fonts as programmable layout engines, not just glyph containers.  
- Impact: Niche but useful for minimalist blogs, demos, educational tools, and explaining color-font/OT features.  
- Watch next: harfbuzz-wasm prototypes with real parsers, more language packs, and UX experiments for in-browser editors using plain textareas.
