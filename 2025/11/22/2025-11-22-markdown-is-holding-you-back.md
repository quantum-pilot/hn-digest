# Markdown Is Holding You Back

- Score: 53 | [HN](https://news.ycombinator.com/item?id=46017782) | Link: https://newsletter.bphogan.com/archive/issue-45-markdown-is-holding-you-back/

### TL;DR

Markdown remains excellent for readable, lightweight documents, but the author argues it becomes a weak source format when content must be reused, validated, or transformed. Minimal syntax and incompatible flavors omit domain meaning, forcing processors to guess; MDX components and plugins often rebuild semantics without portability. Richer formats such as reStructuredText, AsciiDoc, DocBook, or DITA preserve structure at the cost of verbosity and tooling. The recommendation is proportional: keep simple prose simple, but choose semantic markup for long-lived, multi-channel documentation.

### Comment pulse

- Semantic markup enables reliable reuse → explicit content types survive transformation better than inferred structure — counterpoint: many writers value Markdown’s readability and ubiquity.
- Raw HTML or ASTs only partly solve the gap → they expose syntax, not necessarily portable domain meaning.

### LLM perspective

- View: Choose authoring formats from downstream transformation needs, not fashion.
- Impact: Better semantics reduce custom parsers but increase training, migration, and tooling costs.
- Watch next: Schema requirements, flavor drift, export targets, reuse frequency, and author experience.
