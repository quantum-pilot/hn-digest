# John Carmack on mutable variables

- Score: 457 | [HN](https://news.ycombinator.com/item?id=45767725) | Link: https://twitter.com/id_aa_carmack/status/1983593511703474196

### TL;DR

John Carmack recommends single assignment except for genuinely iterative calculations, arguing that retained intermediate values improve debugging and prevent moved code from silently reading the wrong version of a variable. In C and C++, he would prefer initialization-time constness by default with explicit mutability. Commenters explain that reassignment hides ordering dependencies, while distinct names make data flow visible. Others caution that mutation and immutability form a continuum: disciplined local mutation can remain readable and avoid awkward names or functional workarounds.

### Comment pulse

- Single assignment exposes dependencies → reordered statements fail visibly instead of silently consuming a differently mutated value.
- Immutable values localize reasoning → pure functions can be tested from inputs without reconstructing global program state.
- Pragmatic mutation remains useful → loops and obvious post-processing may be clearer than proliferating artificial intermediate names.

### LLM perspective

- View: Default immutability is primarily a control-flow aid, not a claim that state changes never belong in programs.
- Impact: Teams gain safer refactors when names encode transformation stages and mutation stays tightly scoped.
- Watch next: Compare compiler defaults, linter warnings, and defect rates in mixed imperative-functional codebases.
