# Java 25 officially released

- Score: 311 | [HN](https://news.ycombinator.com/item?id=45261946) | Link: https://mail.openjdk.org/pipermail/announce/2025-September/000360.html

### TL;DR

JDK 25 reached general availability with build 36 after no priority-one bugs appeared following its second release candidate. The LTS release contains 18 JEPs, including scoped values, compact source files, flexible constructor bodies, compact object headers, generational Shenandoah, module imports, cryptographic APIs, structured concurrency previews, and several JFR improvements, plus thousands of fixes. Commenters praised JVM longevity and compatibility, but experiences diverged: some run decade-old applications unchanged, while others described difficult migrations blocked by abandoned libraries and lingering concern about Oracle licensing.

### Comment pulse

- Java's mature tooling and ecosystem remain attractive for backends — counterpoint: legacy dependencies, verbosity culture, and licensing anxiety deter greenfield adoption.
- Module imports simplify small files, while critics worry wildcard-like visibility makes unfamiliar code harder to read without IDE assistance.

### LLM perspective

- View: Java's evolution now emphasizes reducing ceremony without abandoning the compatibility and observability that sustain long-lived systems.
- Impact: LTS status gives enterprises a consolidation target, but application libraries determine migration difficulty more than language features alone.
- Watch next: Track vendor builds, production adoption, preview-feature maturation, compact-header results, upgrade tooling, and real migration reports.
