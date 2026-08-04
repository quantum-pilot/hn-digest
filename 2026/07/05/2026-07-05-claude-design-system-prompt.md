# Claude Design System Prompt

- Score: 115 | [HN](https://news.ycombinator.com/item?id=48792399) | Link: https://github.com/Trystan-SA/claude-design-system-prompt

### TL;DR

The MIT-licensed repository packages a 20-chapter design prompt and 14 skills spanning discovery, prototyping, system extraction, accessibility, interaction states, and anti-slop review. It has Claude and Codex variants emphasizing content, hierarchy, tokens, semantic HTML, and deliberate visual direction. HN’s central objection was provenance: the project claims reverse engineering but documents no method, its skill list differs from Claude Design’s reported tools, and it offers no demonstrations. Commenters therefore suspected a ground-up imitation, raising licensing questions. Practical users added explicit geometry planning improves SVGs, while export sanitization may strip animation.

### Comment pulse

- Reverse-engineering provenance is unsubstantiated → no extraction method or evidence is shown, and the repository’s skills diverge from Claude Design’s reported inventory.
- MIT licensing depends on authorship → a ground-up implementation may be licensable — counterpoint: copied proprietary prompts could not be relicensed merely by publishing them.
- Claude Design needs geometric scaffolding for SVGs → defining algorithms before drawing improves precision, while sanitized exports can silently remove animation.

### LLM perspective

- **View:** Prompt libraries need software-grade evidence: provenance, versioning, reproducible demos, regression tests, and documented failure cases.
- **Impact:** If effective, reusable procedures can standardize design quality across models; if unverified, they shift aesthetic sameness into longer instructions.
- **Watch next:** Provenance notes, side-by-side outputs, blind evaluations, accessibility scores, cross-model behavior, prompt updates, SVG export tests, and license clarification.
