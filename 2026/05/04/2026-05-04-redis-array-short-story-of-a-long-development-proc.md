# Redis array: short story of a long development process

- Score: 213 | [HN](https://news.ycombinator.com/item?id=48009172) | Link: https://antirez.com/news/164

### TL;DR

Redis creator Salvatore Sanfilippo spent four months designing and implementing a proposed Array type, using AI without shortening the schedule but broadening the work. A specification-first process led to a sparse, shape-changing structure that supports enormous numeric indexes while scanning or popping in proportion to stored elements, plus ARGREP backed by a hardened, optimized TRE regex engine and 32-bit support. He reviewed every core line and stress-tested extensively. HN saw skilled amplification rather than autonomous coding, warning managers not to generalize from an expert while reviewers debated the large patch.

### Comment pulse

- Expert supervision is load-bearing → Sanfilippo owned the design, checked every line, and used agents for expansion rather than delegation.
- Specification-first, adversarial review improves agent output → independent models expose gaps before plans and code harden.
- Large AI-assisted patches strain community review → counterpoint: maintainers said core implementation was about 5,000 lines, with most additions tests and dependencies.

### LLM perspective

- **View:** AI changed feasible scope more than elapsed time; ambition, not speed, was the reported gain.
- **Impact:** Senior systems programmers can explore complex designs while preserving human ownership of invariants.
- **Watch next:** PR review findings, benchmarks across sparse shapes, 32-bit results, TRE security audits, and acceptance into Redis.
