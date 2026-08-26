# Maybe comments should explain 'what' (2017)

- Score: 179 | [HN](https://news.ycombinator.com/item?id=46486780) | Link: https://www.hillelwayne.com/post/what-comments/

### TL;DR

The essay rejects the rule that comments should explain why but never what. Descriptive names should replace comments when code itself can remain clear, yet both why and what belong beside an operation when retrieving context would require archaeology or risky assumptions. It argues that aggressively extracting sequential logic into tiny methods can make debugging harder by scattering the execution path, whereas concise explanatory comments may preserve locality. Commenters largely agreed, criticizing Clean Code-style fragmentation and reframing the goal: add relevant information that cannot be expressed cleanly through code.

### Comment pulse

- Tiny extracted methods force repeated definition jumps, obscuring sequential behavior that may be clearer when kept together with local explanation.
- Comments and names both manage reader context; mutable object state can impose a larger hidden context than either technique solves.
- Long identifiers preserve meaning—counterpoint: excessive length buries operators and repeats type information already visible through tooling.

### LLM perspective

- View: The useful boundary is not why versus what, but whether information is local, durable, accurate, and otherwise unavailable.
- Impact: Maintainers debug faster when intent and mechanics stay near surprising code without duplicating obvious syntax.
- Watch next: Teams should review stale-comment defects, navigation cost, and comprehension time before enforcing blanket style rules.
