# FracturedJson

- Score: 488 | [HN](https://news.ycombinator.com/item?id=46464235) | Link: https://github.com/j-brooke/FracturedJson/wiki

### TL;DR

FracturedJson formats JSON for human scanning without expanding every value vertically. It inlines simple containers, packs long arrays across rows, aligns structurally similar objects as tables, and expands complex sections, with controls for width, nesting, padding, comments, commas, and number alignment. Implementations exist for .NET and JavaScript, with Python wrapping .NET and a new Rust port. HN discussion praised readability but emphasized shared conformance fixtures, standard-input support, copyright attribution, and the deployment burden of Python requiring a separate .NET runtime.

### Comment pulse

- Cross-language fixtures would improve trust → data-driven cases can expose drift between C#, JavaScript, Rust, and future ports.
- Python’s wrapper compromises portability → requiring .NET undermines the normal expectation that dependencies install through `pip` alone.
- CLI composability is essential → standard input and output make the formatter useful alongside `jq` and shell pipelines.

### LLM perspective

- View: FracturedJson optimizes visual information density while preserving ordinary JSON semantics.
- Impact: Developers can inspect structured data faster, especially repeated records and coordinate-heavy arrays.
- Watch next: Establish conformance fixtures, fuzz cross-port equivalence, and document stable formatting guarantees across releases.
