# A couple million lines of Haskell: Production engineering at Mercury

- Score: 401 | [HN](https://news.ycombinator.com/item?id=47991802) | Link: https://blog.haskell.org/a-couple-million-lines-of-haskell/

### TL;DR

Mercury runs roughly two million lines of Haskell for a financial platform serving 300,000 businesses, largely with generalists trained after hiring. Its lesson is pragmatic: use types to preserve operational knowledge and prevent silent corruption, isolate impurity and advanced machinery behind simple APIs, model domain errors independently of transport, and design libraries for instrumentation. Temporal replaced fragile hand-built workflow coordination, while tests still cover semantic and I/O failures types cannot catch. Commenters admired the approach but debated whether Haskell caused the results or merely reflects an unusually disciplined engineering culture.

### Comment pulse

- “Make invalid states unrepresentable” transfers across languages — counterpoint: Haskell’s expressive types make some guarantees less awkward than TypeScript or C#.
- Productivity comparisons split sharply: Rust simplified some developers’ work, while others found its borrow and abstraction constraints obstructive.
- Customers praised reliability, but skeptics credited product focus, leadership, and execution more than language choice.

### LLM perspective

- The most reusable pattern is containment: concentrate complexity where failures are costly, then expose boring interfaces.
- Track onboarding time, incident classes, change lead time, and ecosystem-maintenance cost against comparable teams.
- Library authors should add observability hooks and controlled escape hatches before downstream users resort to forks.
