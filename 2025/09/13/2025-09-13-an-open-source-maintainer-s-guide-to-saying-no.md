# An open-source maintainer's guide to saying “no”

- Score: 131 | [HN](https://news.ycombinator.com/item?id=45234593) | Link: https://www.jlowin.dev/blog/oss-maintainers-guide-to-saying-no

- TL;DR
  - Maintaining OSS often means saying no—even to good ideas—to protect a project’s mental model and API coherence. Low-effort, LLM-generated code has flipped the cost calculus: maintainers now face high-effort reviews of misaligned PRs. The author recommends documenting the “why,” shifting burden of proof to contributors, and using a contrib module with owner-maintained, non-core features. Politeness is mandatory; stewardship is non-negotiable. As with MCP’s committee, disciplined scope keeps systems healthy. HN echoes boundaries, warns about untested LLM PRs, and debates drive-by PR etiquette.

- Comment pulse
  - Say no to preserve generality → niche features burden everyone; coherent abstractions beat feature lists—counterpoint: maintainers don’t owe years of unpaid labor; set boundaries.
  - LLM‑authored PRs often untested → review becomes expensive, eroding trust; clear testing expectations and maintainability limits justify rejections or conditional merges.
  - Etiquette dispute → some require “open an issue first”; others accept PR‑first since forking is a right; maintainers owe users nothing, so document contribution policies.

- LLM perspective
  - View: Shift from code-first to rationale-first: PR template asks for problem statement, alignment with principles, maintenance plan, and test evidence.
  - Impact: Fewer misaligned changes; clearer review criteria; faster merges for aligned fixes; contributors self-select or move features to contrib/ or forks.
  - Watch next: Track rejection reasons, review time, post-merge breakage; pilot bot triage and issue-first gates; refine contrib ownership and compatibility policy.
