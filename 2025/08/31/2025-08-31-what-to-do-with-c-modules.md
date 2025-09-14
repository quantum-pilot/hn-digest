# What to do with C++ modules?

- Score: 226 | [HN](https://news.ycombinator.com/item?id=45086210) | Link: https://nibblestew.blogspot.com/2025/08/we-need-to-seriously-think-about-what.html

- TL;DR
  - Jussi Pakkanen argues C++ modules should prove 5× faster builds or be dropped. After years of fractured compiler–build-system work, the narrative shifted to “isolation,” while import std delivers PCH‑like gains (~10–20%) and adds non‑portable BMIs, refactors, and fragile tooling. HN debates alternatives: adopt D‑style modules and curb the preprocessor; use incremental compilers like zapcc; or introduce a minimal “import = include‑without‑leakage.” Some praise encapsulation wins, but most remain skeptical without cross‑vendor coordination and verified speedups on large codebases.

- Comment pulse
  - D-style modules + drop/limit preprocessor → proven independent semantics and faster builds; reduces brittleness. — counterpoint: C interop and template specialization semantics complicate feasibility.
  - Use incremental compilers (zapcc) for 5× → cache compiler state across invocations. — counterpoint: overlaps with ccache, heavy memory, maturity/debuggability questioned; not the committee’s remit.
  - Modules’ value is encapsulation, not speed → explicit interfaces, no macro leakage. — counterpoint: toolchains immature; mixed include/import impractical; third‑party and Qt moc block adoption.

- LLM perspective
  - View: Without shared build graph/BMI conventions, modules stagnate; form a cross‑vendor taskforce to define reference pipeline and interop rules.
  - Impact: If import std remains PCH‑like, enterprises won’t refactor; modules stay niche in greenfield, header‑heavy ecosystems continue relying on PCH/ccache.
  - Watch next: Publish audited speedups on LLVM, Chromium, Qt; standardize cross‑compiler BMI or stable import std cache; plan for mixed include/import migration.
