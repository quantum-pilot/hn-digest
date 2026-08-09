# Spanish legislation as a Git repo

- Score: 684 | [HN](https://news.ycombinator.com/item?id=47553798) | Link: https://github.com/EnriqueLop/legalize-es

### TL;DR

Legalize España converts more than 8,600 consolidated Spanish laws from the BOE open-data API into Markdown, one law per file, with YAML metadata and each reform represented as a commit dated to its official publication. That makes current text searchable with tools and historical changes inspectable through `git log`, `diff`, and `blame`; the repository reports roughly 27,800 commits and reform history since 1960. HN praised the accessible dataset but warned it is an unofficial mirror whose source coverage may be incomplete, while judicial interpretations—the scarcer, valuable layer—remain absent.

### Comment pulse

- The creator built the pipeline in about four hours with Claude Code and is testing open-dataset versus paid API models.
- Lawyers argued statutes are one layer; judgments resolve interactions and ambiguities, yet Spain lacks comparable open case-law data.
- Git authorship could identify politicians and tests encode loopholes — counterpoint: legal coherence is not trivial regression testing.

### LLM perspective

- **View:** Git is an excellent audit and distribution layer, but not a semantic model of law or authoritative publication mechanism.
- **Impact:** Developers gain reproducible inputs for compliance, research, alerts, and AI retrieval; lawyers still supply interpretation and verification.
- **Watch next:** Coverage audits, court-decision linkage, stable identifiers, canonical government adoption, and provenance-preserving APIs.
