# Wordgard: In-browser rich-text editor from the creator of ProseMirror

- Score: 255 | [HN](https://news.ycombinator.com/item?id=48772573) | Link: https://wordgard.net/

### TL;DR

Wordgard is a new MIT-licensed JavaScript foundation for semantic, schema-constrained browser editors, emphasizing a general programmable API, replaceable extensions, structured custom elements, accessibility, bidirectional text, and collaborative editing. It deliberately controls supported document structure rather than exposing arbitrary HTML. HN’s main question was why teams should migrate from ProseMirror when no direct upgrade path exists. Creator Marijn Haverbeke said satisfied users need not switch; Wordgard is a fresh iteration based on accumulated design insights. Commenters also highlighted typed JSON schemas as an unresolved editor pain point.

### Comment pulse

- Migration lacks urgency → concepts transfer but code does not — counterpoint: the creator recommends staying with ProseMirror when it already works.
- Browser primitives remain insufficient → contenteditable supplies basic editing, but libraries still reconcile selection quirks, controlled schemas, UI, and interoperability.
- Programmatic document access needs better typing → developers currently duplicate schemas or generate editor definitions from a typed meta-schema.

### LLM perspective

- **View:** A clean-slate successor can improve architecture without becoming the default migration target.
- **Impact:** New projects gain another structured option; existing ProseMirror deployments face deliberate reevaluation costs.
- **Watch next:** Compare extension ergonomics, collaboration behavior, accessibility, and typed document tooling on production-scale editors.
