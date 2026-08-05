# Twenty Years of Pandoc

- Score: 401 | [HN](https://news.ycombinator.com/item?id=49156750) | Link: https://pandoc.org/twenty-years-of-pandoc.html

### TL;DR

Pandoc began in 2006 as John MacFarlane’s 3,000-line Haskell learning project and grew through more than 200 releases into a document-conversion platform installed on millions of machines. Its reader/AST/writer architecture now supports 51 inputs, 76 outputs, filters, citations, templates, sandboxing, servers, Lua, Typst, and browser WASM. MacFarlane credits Haskell’s types and purity for safe evolution and high-quality contributions. HN celebrated the architecture and longevity, arguing deterministic, efficient conversion will remain preferable to LLM translation despite models’ ability to infer ambiguous intent.

### Comment pulse

- The AST unlocked compounding value → N readers and M writers yield N×M conversions while filters operate on one shared representation.
- Haskell shaped project culture → a smaller self-selected contributor pool brought strong types, abstraction skills, and relatively high signal.
- LLMs complement rather than replace converters → inferred intent helps ambiguous markup, but batch work needs determinism, reliability, and low energy use.

### LLM perspective

- View: Pandoc’s durability comes from a stable domain model plus disciplined extensibility, not format count alone.
- Impact: Writers and tool builders retain a dependable interoperability layer across academic, publishing, and development workflows.
- Watch next: CommonMark parser migration, WASM adoption, new formats, maintainer succession, and hybrid deterministic-plus-semantic conversion.
