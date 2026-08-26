# LLVM: The bad parts

- Score: 266 | [HN](https://news.ycombinator.com/item?id=46588837) | Link: https://www.npopov.com/2026/01/11/LLVM-The-bad-parts.html

### TL;DR

LLVM’s lead maintainer catalogs improvement opportunities rather than reasons to abandon the project. Organizational problems include scarce expert review, API churn, huge builds, noisy post-commit CI, weak end-to-end testing, divergent backends, slow compilation, and absent first-class performance tracking. Technical debt spans undef semantics, incomplete formal specification, constraint encoding, floating-point behavior, decade-long migrations, undocumented ABI lowering, runtime-library discovery, context versus module ownership, and LICM-induced register pressure. HN readers largely agreed, requesting IR-level executable tests, better review incentives, and more coherent distribution of LLVM’s excellent diagnostic tooling.

### Comment pulse

- Review capacity is the social bottleneck → contributor volume exceeds qualified reviewer time, and employers still reward implementation more visibly.
- IR-level executable tests are missing → backend authors lack documented semantics and comprehensive cross-operation correctness coverage.
- Tooling quality is fragmented → sanitizers and clang utilities are excellent — counterpoint: platform packages expose inconsistent subsets and versions.

### LLM perspective

- View: LLVM’s hardest problems arise where massive scale turns individually reasonable choices into system-wide coordination debt.
- Impact: Frontends and backends absorb churn, testing gaps, build costs, and undocumented contracts that favor well-resourced teams.
- Watch next: Prioritize reviewer assignment, executable IR suites, flaky-bot cleanup, public performance tracking, and ABI-lowering standardization.
