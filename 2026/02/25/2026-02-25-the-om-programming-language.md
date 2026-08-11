# The Om Programming Language

- Score: 218 | [HN](https://news.ycombinator.com/item?id=47154971) | Link: https://www.om-language.com/

### TL;DR

Om is an early proof-of-concept for a maximally small, prefix-concatenative language in which programs and data share the same representation. Any BOM-free UTF-8 text is valid; operators consume only the remainder they need, enabling streaming, single-pass evaluation without stack-underflow states. Unknown or incomplete operations remain representable as programs, while a common immutable operand interface replaces conventional types. The header-only C++ implementation emphasizes Unicode correctness, embedding, and extensibility, but the author says basic numbers, files, optimization, and major design stabilization are still missing before practical use.

### Comment pulse

- Readers wanted worked examples above the fold because the abstract semantics are difficult to evaluate without seeing small programs execute.
- Comparisons centered on Forth and Joy; supporters liked composability, while skeptics expected familiar concatenative stack-juggling and readability costs.
- Several treated Om primarily as a language-design thought experiment rather than a production contender, consistent with its explicitly unfinished status.

### LLM perspective

- **View:** Om’s novelty lies in prefix consumption and program-preserving partial evaluation, not production readiness.
- **Impact:** Its tiny syntax may aid experimentation with interpreters, streaming evaluation, and homoiconic representations.
- **Watch next:** Concrete examples, basic facilities, performance work, and evidence that the semantics scale.
