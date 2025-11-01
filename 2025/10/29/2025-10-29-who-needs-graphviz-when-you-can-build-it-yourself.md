# Who needs Graphviz when you can build it yourself?

- Score: 495 | [HN](https://news.ycombinator.com/item?id=45742907) | Link: https://spidermonkey.dev/blog/2025/10/28/iongraph-web.html

- TL;DR
  - SpiderMonkey built iongraph, a tiny, loop-aware layout for compiler control-flow that favors stable, source-like structure and interactivity over dot’s unstable, area-minimizing layouts. It simplifies Sugiyama (layering, dummies, local straightening, railroad-style edges), exploits reducible control flow, and renders massive graphs in milliseconds. HN discusses dot vs Graphviz, DOT’s enduring portability, specialization vs generality, and whether visualizing huge graphs helps without drill-down tools.

- Comment pulse
  - Not Graphviz vs all; it's chiefly dot. → Contributing the layout would help many—counterpoint: MPL vs EPL, JS-to-C port, and reducible-CFG assumptions limit portability.
  - Specialized algorithms beat general ones in constrained domains. → Exploiting CFG properties yields stability and speed; use heuristics first, fallback to general solvers when unsuitable.
  - Big graph pictures often underdeliver. → Minimal-area layouts aren’t necessarily readable; interactive drill-down, search, and linkable subgraphs matter more than static beauty.

- LLM perspective
  - View: A domain-first, constraint-light approach often outperforms generic optimizers when user comprehension and stability are primary goals.
  - Impact: Expect adoption in compiler tooling, profilers, and IDEs where step-by-step IR exploration beats static PDFs.
  - Watch next: Benchmarks on other CFG producers, modular drill-down/linking UX, and an upstream-friendly reference implementation beyond SpiderMonkey.
