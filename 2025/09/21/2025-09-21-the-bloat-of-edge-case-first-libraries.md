# The bloat of edge-case first libraries

- Score: 125 | [HN](https://news.ycombinator.com/item?id=45319399) | Link: https://43081j.com/2025/09/bloat-of-edge-case-libraries

- TL;DR
    - The author argues JavaScript’s ecosystem bloats from “edge‑case‑first” micro-libraries that do runtime type/value checks for rare scenarios (e.g., is-number, is-arrayish, pascalcase). He advocates designing for the common case, assuming correct types, validating values at data boundaries, and replacing deps with native features or modern zero-dep alternatives; highlights e18e tools. HN adds: much of this was justified in 2014-era JS, dynamic vs static typing shifts responsibility, deep transitive inertia resists cleanup, and trivial snippets shouldn’t become dependencies—LLMs can generate them.

- Comment pulse
    - Validate at boundaries → dynamic code should trust callers; pervasive checks are slow and brittle — counterpoint: static types already prevent many misuse cases.
    - These libs were needed in 2014-era JS → lack of TS, cross-realm quirks; the mistake is using them today for common paths.
    - Transitive inertia blocks cleanup → deep, old deps are hard to change; favor top-level libs with lean trees and paste trivial snippets (LLMs help).

- LLM perspective
    - View: Prefer narrow, zero-dep APIs; validate types at boundaries; reserve edge-case handling for optional adapters/plugins.
    - Impact: Maintainers reduce transitive risk, bundle size, and patch churn; users gain faster installs and fewer supply-chain vulnerabilities.
    - Watch next: Track e18e replacements, ESLint-depend adoption, and major libs dropping micro-deps; benchmark cold-start/size before/after to justify migrations.
