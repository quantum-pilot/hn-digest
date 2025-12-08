# Scala 3 slowed us down?

- Score: 161 | [HN](https://news.ycombinator.com/item?id=46182202) | Link: https://kmaliszewski9.github.io/scala/2025/12/07/scala3-slowdown.html

### TL;DR
A team migrated a high-throughput Scala 2.13 service to Scala 3.7.3. Functional tests and basic load tests passed, but hours into production the Kafka consumer lag grew, and per-instance throughput dropped. Profiling showed the JIT compiler and a Quicklens macro-based library dominating CPU time—caused by a Scala‑3‑specific bug in Quicklens’s chained operations. Upgrading Quicklens removed the regression and restored Scala 2–level performance. The episode underlines that cross-version migrations must include realistic performance testing and scrutiny of macro/inline-heavy libraries.

---

### Comment pulse
- Strong praise for the post’s disciplined debugging narrative → readers value real-world, stepwise reasoning over abstract language debates — counterpoint: some replies complain without engaging the article.
- Many criticize Scala 3’s direction → say it ignored core pain points, stalled ecosystem momentum, and reflects academic priorities more than product needs.
- Technical angle: Scala 3’s `inline` differs from Scala 2’s `@inline` → macro-heavy libraries can explode JIT work; discussion broadens into dependency-upgrade strategies and version pinning.

---

### LLM perspective
- View: This case is about ecosystem maturity, not “Scala 3 is slow”; migration risk lives in libraries and tooling boundaries.
- Impact: Teams with macro/inline-heavy stacks must budget time for profiling and dependency audits during any major language upgrade.
- Watch next: Better cross-version CI benchmarks for popular libraries, stricter macro guidelines, and migration checklists that mandate production-like load tests.
