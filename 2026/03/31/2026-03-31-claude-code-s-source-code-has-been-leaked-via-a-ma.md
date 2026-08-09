# Claude Code's source code has been leaked via a map file in their NPM registry

- Score: 1863 | [HN](https://news.ycombinator.com/item?id=47584540) | Link: https://twitter.com/Fried_rice/status/2038894956459290963

### TL;DR

The author says a source map accidentally bundled with Claude Code’s npm package exposed readable CLI source that was quickly mirrored. Their inspection found feature-gated anti-distillation decoy tools, server-signed text summaries, native client attestation, an internal undercover mode, prompt-cache protections, an unreleased always-on KAIROS agent, and a likely April Fools companion. The article argues roadmap flags are more damaging than code disclosure because competitors cannot unlearn future plans. HN focused on roadmap leakage, imperfect cleanup, and whether extreme code complexity necessarily means poor software.

### Comment pulse

- Labeling the version Unpublished merely deprecated it, leaving artifacts accessible; npm policy may prevent removal after substantial downloads.
- KAIROS, Buddy, and undercover flags reveal product direction, though some hidden strings were already extractable from bundled binaries.
- A 3,167-line function drew architectural criticism — counterpoint: nesting and branch counts alone do not establish poor runtime behavior.

### LLM perspective

- **View:** The durable loss is advance notice of strategy; implementation details can be replaced, but disclosed intent cannot.
- **Impact:** Competitors gain roadmap signals while security researchers gain precise targets around attestation, caching, and command validation.
- **Watch next:** Anthropic’s incident explanation, artifact status, build-pipeline source-map checks, and whether exposed feature flags are renamed or retired.
