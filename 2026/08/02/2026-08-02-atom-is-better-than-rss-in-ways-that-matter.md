# Atom is better than RSS, in ways that matter

- Score: 129 | [HN](https://news.ycombinator.com/item?id=49138897) | Link: https://chrismorgan.info/atom%3Erss

### TL;DR

Atom specifies text constructs that distinguish plain text, escaped HTML, and XHTML, making titles containing characters such as `<` and `&` unambiguous. RSS leaves title and content encoding underspecified, forcing readers and publishers into incompatible conventions and heuristics; its summary-versus-full-content distinction is similarly unclear. The author nevertheless concedes that major podcast platforms entrenched RSS and often reject Atom. HN agreed Atom is cleaner for implementers, but questioned HTML titles, preferred JSON Feed, and noted that ordinary subscribers rarely notice format differences until a parser fails.

### Comment pulse

- Publisher-side ambiguity creates reader-side blame: malformed or differently escaped feeds fail unpredictably even when modern parsers try to compensate.
- Atom supporters value explicit semantics — counterpoint: critics say unrestricted title markup is impractical and JSON Feed better matches reader presentation needs.
- Podcast distribution remains the decisive lock-in; Apple’s early RSS-only catalog helped freeze layers of extensions into the ecosystem.

### LLM perspective

- View: Protocol quality matters most at ambiguous boundaries, where tolerant parsing converts specification gaps into permanent interoperability debt.
- Impact: New publishers can choose Atom cheaply, but podcast creators remain constrained by aggregator acceptance rather than parser capability.
- Watch next: Test representative readers against special-character titles, full-versus-summary entries, timestamps, malformed markup, and Atom podcast submissions.
