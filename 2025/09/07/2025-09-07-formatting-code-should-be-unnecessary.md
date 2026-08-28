# Formatting code should be unnecessary

- Score: 350 | [HN](https://news.ycombinator.com/item?id=45163043) | Link: https://maxleiter.com/blog/formatting

### TL;DR

The author argues that source formatting disputes could disappear if systems stored a semantic representation rather than text. Rational’s R1000 reportedly stored Ada programs as DIANA trees, with source rendered through each developer’s preferred pretty-printing settings; the same representation also supported incremental compilation, semantic analysis, and refactoring. Commenters counter that plain text enables universal tools and that deliberate typography can communicate relationships not contained in an AST. Others saw standard automated formatters as a far cheaper practical solution.

### Comment pulse

- Critics emphasized the ecosystem value of grep, diff, version control, and editor independence built around plain text.
- Debate split over whether custom alignment carries meaning or merely preserves subjective formatting preferences.

### LLM perspective

- View: Semantic storage solves formatting conflicts only by relocating complexity into editors, interchange, and version-control tooling.
- Impact: Projectional systems promise richer operations, but text remains compelling because every tool can inspect it.
- Watch next: Hybrid formats that preserve canonical text while letting editors render semantic, personalized views without noisy diffs.
