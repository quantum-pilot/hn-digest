# Pnpm has a new setting to stave off supply chain attacks

- Score: 208 | [HN](https://news.ycombinator.com/item?id=45286526) | Link: https://pnpm.io/blog/releases/10.16

### TL;DR

pnpm 10.16 adds `minimumReleaseAge`, which blocks dependency versions until a configured number of minutes after publication; exclusions allow selected packages to update immediately. The delay aims to avoid newly compromised releases that registries and scanners often identify quickly. The release also adds programmable finders for querying dependency metadata beyond names and versions. Commenters welcomed a persistent project setting but noted the tradeoff: widespread delays could slow both attack discovery and urgent fixes, while unclear minute-based units invite configuration mistakes.

### Comment pulse

- Automated security scanners may remain early canaries even if developers delay installs — counterpoint: delayed adoption can also postpone discovery and fixes.
- Participants compared similar uv and Yarn controls, preferring repository configuration over flags developers must remember.

### LLM perspective

- View: Release-age gating is a useful blast-radius reducer, not a substitute for lockfiles, scanning, provenance, or dependency review.
- Impact: Teams gain a low-effort buffer against account compromises while accepting slower access to legitimate patches.
- Watch next: Measure malicious-release detection times, emergency override safety, unit clarity, excluded-version support, and adoption across package managers.
