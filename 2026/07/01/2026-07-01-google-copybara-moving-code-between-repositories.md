# Google copybara: moving code between repositories

- Score: 290 | [HN](https://news.ycombinator.com/item?id=48740698) | Link: https://github.com/google/copybara

### TL;DR

Copybara moves and transforms code between repositories while requiring one authoritative source of truth. Its main pattern keeps private monorepo code synchronized with public Git repositories, but it can import outside contributions, preserve blame during one-time splits, remap paths, exclude files, and rewrite content. State lives in destination commit labels, enabling repeatable multi-user runs; Git is the only mature backend. HN users found simple one-way exports practical, warned that bidirectional transforms and divergence become tedious, and compared alternatives including Josh, git subtree, and the retired fbshipit.

### Comment pulse

- One-way migrations suit Copybara → users export a folder with rewritten history, retaining content and authorship for blame while development moves elsewhere.
- Bidirectional sync is fragile → transformations may not invert, divergent commits gain different SHAs, and baseline tracking becomes confusing despite origin trailers.
- Backend gaps invite extensions → Git dominates, while a contributor added Perforce support and commenters noted Piper compatibility does not mean shared implementation.

### LLM perspective

- **View:** Copybara is best understood as release plumbing for a monorepo boundary, not a general substitute for package management.
- **Impact:** Small projects seeking shared folders may incur more configuration overhead than extracting a library or dependency.
- **Watch next:** Evaluate transform reversibility, conflict workflows, provenance trailers, backend maturity, and snapshot testing before allowing inbound changes.
