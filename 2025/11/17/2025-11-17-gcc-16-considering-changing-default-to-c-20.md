# GCC 16 considering changing default to C++20

- Score: 92 | [HN](https://news.ycombinator.com/item?id=45953202) | Link: https://inbox.sourceware.org/gcc/aQj1tKzhftT9GUF4@redhat.com/

### TL;DR

A GCC developer proposed declaring C++20 non-experimental and making GNU C++20 the default dialect, replacing the GNU C++17 default introduced with GCC 11. A similar switch had been considered for GCC 15 but deferred because library support and compiler issues, including concepts mangling and modules, remained incomplete. The message asks maintainers whether blockers still exist and says modules would presumably remain disabled by default. This is a proposal on the GCC mailing list, not a finalized GCC 16 change, and explicit compiler flags can already select a dialect.

### Comment pulse

- Readers emphasized that changing defaults can break projects that implicitly depend on the prior dialect.
- Bootstrapping also limits how aggressively a compiler can require newer language support from the compiler building it.

### LLM perspective

- View: A newer default improves expectations only when compatibility costs are deliberate and well documented.
- Impact: Implicit builds may change behavior, while explicit `-std` users should retain predictable language selection.
- Watch next: Maintainer consensus, identified blockers, release notes, bootstrap requirements, and the final modules decision.
