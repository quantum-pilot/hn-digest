# Relicensing with AI-Assisted Rewrite

- Score: 372 | [HN](https://news.ycombinator.com/item?id=47257803) | Link: https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/

### TL;DR

chardet’s maintainers used Claude Code to rewrite the library and released version 7 under MIT, replacing the LGPL attached to its Mozilla-derived predecessor. The article argues this may not escape the original copyright and that AI-authorship doctrine also complicates ownership. A maintainer says Claude worked in an empty repository without old-source access, yet critics cite the maintainer’s decade of exposure, reused tests, and opaque model training. Commenters stressed that expression, substantial similarity, and information flow—not matching functionality alone—will shape any legal answer, leaving downstream users with license risk.

### Comment pulse

- Clean-room arguments split on independence → direct source access, model training, human memory, specifications, and code similarity provide different kinds of evidence.
- AI authorship does not automatically erase prior rights → counterpoint: independently generated, sufficiently distinct implementations may avoid derivative-work status.
- The practical harm lands downstream → uncertain provenance can force users or distributions to audit, pin, replace, or fork a dependency.

### LLM perspective

- **View:** An AI rewrite cannot supply the provenance wall that relicensing needs unless inputs, logs, and comparisons are auditable.
- **Impact:** Maintainers shift unresolved infringement and ownership questions onto every adopter of the new release.
- **Watch next:** Repository diffs, retained Claude logs, contributor claims, downstream package decisions, and any litigation.
