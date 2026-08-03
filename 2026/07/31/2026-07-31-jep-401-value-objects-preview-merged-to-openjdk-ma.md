# JEP 401: Value Objects (Preview) merged to OpenJDK master

- Score: 224 | [HN](https://news.ycombinator.com/item?id=49119063) | Link: https://github.com/openjdk/jdk/pull/31120

### TL;DR

OpenJDK integrated the first preview implementation of value objects as commit cc278db, alongside JEP 539 strict field initialization, which it depends on. The unusually broad change spans the Java language, JVM, and standard library: 2,934 commits touched 1,888 files, adding 208,011 lines and removing 13,161. Commenters welcome value semantics as a long-missing route to better performance and praise Java’s compatibility-conscious evolution. They caution that this is only Valhalla’s first part, with null constraints and generic support still to come.

### Comment pulse

- The design offers graded tradeoffs → commenters distinguish classical objects, identity-free objects, atomic values, and tearable values by semantics and performance.
- Java’s language reputation is improving → supporters cite recent evolution, while critics locate lingering pain in culture and oversized frameworks.
- Cross-language comparisons divide readers → Java’s dates, switches, and values were contrasted with JavaScript — counterpoint: others called them fundamentally incomparable.

### LLM perspective

- View: Partitioned discussion preserved full implementation context without pretending the compiler, runtime, and library layers were independent.
- Impact: Area-specific reviewers converged on one integration decision for an unusually intertwined change.
- Watch next: Track preview feedback, null constraints, generics, and performance changes in value-heavy workloads.
