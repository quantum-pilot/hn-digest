# Rust in the kernel is no longer experimental

- Score: 920 | [HN](https://news.ycombinator.com/item?id=46213585) | Link: https://lwn.net/Articles/1049831/

### TL;DR

A brief Maintainers Summit report says assembled Linux developers reached consensus that Rust is no longer experimental, will lose that label, and is now a permanent core part of the kernel. The source promises later details, so it does not define new maintenance rules, architecture coverage, or a rollout schedule. Commenters interpret the decision as confidence for Rust driver investment, not a requirement to rewrite core Linux or preserve stable in-kernel APIs. Some distributions reportedly already enable Rust-built components, though individual examples in the thread are uncertain.

### Comment pulse

- Supporters called the label change a milestone and want more distribution kernels built with Rust enabled.
- Permanence does not imply every architecture must support Rust or that subsystem maintainers gain a stable internal API.
- Readers noted maintainer attrition and past resistance, tempering celebration with questions about long-term staffing.

### LLM perspective

- View: Removing “experimental” changes project confidence more than kernel mechanics, but that confidence can unlock driver investment.
- Impact: Vendors can plan Rust drivers with less fear that upstream will abandon the language.
- Watch next: Summit details, maintainer capacity, architecture policy, and Rust-enabled configurations in conservative distributions.
