# Nested code fences in Markdown

- Score: 178 | [HN](https://news.ycombinator.com/item?id=46705201) | Link: https://susam.net/nested-code-fences.html

### TL;DR

The article explains CommonMark’s escape hatch for displaying fence markers inside literal code. A block may use backticks or tildes, with any run of at least three characters; its closing fence must use the same character and be at least as long as the opener, so choosing a longer outer fence preserves shorter inner ones. Inline spans similarly use matching backtick runs, with surrounding spaces enabling literal edge backticks after normalization. Commenters connected the technique to GitHub suggestions, JupyterBook, LLM prompts, parser tests, and MIME-style boundary selection.

### Comment pulse

- Practical reuse surfaced quickly → Readers apply longer fences to GitHub suggestions, documentation systems, and prompts requesting Markdown inside code blocks.
- Arbitrary depth needs delimiter planning → Each outer layer can use a longer run, provided embedded content never matches its terminating boundary.
- Syntax history divided opinion → Some saw exception-heavy chaos; replies distinguished original ambiguous Markdown from CommonMark’s specification, reference implementation, and tests.

### LLM perspective

- View: Variable-length delimiters are a simple, composable solution when authors inspect content and choose a collision-free outer boundary.
- Impact: The rule prevents broken rendering in documentation, review suggestions, generated prompts, and examples containing Markdown syntax.
- Watch next: Renderer conformance across CommonMark-derived tools, especially extensions whose preprocessing may alter fences before parsing.
