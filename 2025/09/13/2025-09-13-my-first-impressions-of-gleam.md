# My first impressions of gleam

- Score: 156 | [HN](https://news.ycombinator.com/item?id=45231852) | Link: https://mtlynch.io/notes/gleam-first-impressions/

### TL;DR

An experienced Go and Python programmer tried Gleam by parsing old AIM logs and found the functional model increasingly enjoyable after initial friction. Pipelines, pattern matching, example-led documentation, warnings, and explicit Result and Option types stood out positively. Frustrations included unclear build artifacts, reliance on third-party CLI libraries, awkward error handling inside pipelines, a small standard library, and an immature ecosystem. Commenters argued that the compact core is intentional and highlighted parser combinators, exhaustive matching, and the BEAM runtime’s operational strengths.

### Comment pulse

- Commenters recommended recursive parsers, parser combinators, decoders, and algebraic data types instead of recreating imperative loops.
- Runtime discussion split between wanting native compilation and valuing BEAM concurrency, supervision, scheduling, and browser-capable JavaScript output.

### LLM perspective

- View: Gleam’s constraint-driven design teaches useful habits, but ecosystem gaps remain visible in ordinary tooling tasks.
- Impact: BEAM and JavaScript targets broaden deployment while static types make functional patterns approachable to newcomers.
- Watch next: Filesystem support, package maturity, error-pipeline ergonomics, clearer build documentation, and parser-library reliability.
