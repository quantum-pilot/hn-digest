# When I reject AI code even if it works

- Score: 217 | [HN](https://news.ycombinator.com/item?id=48614631) | Link: https://vinibrasil.com/when-i-reject-ai-code-even-if-it-works/

### TL;DR

The essay says coding agents shift the bottleneck from implementation to comprehension. Even passing code should be discarded when its author cannot explain the approach, the diff exceeds the problem, abstractions arrive before need, or local success makes the wider system harder to reason about. The writer often uses a rejected first pass to understand the problem, then guides a second attempt with stronger context. HN commenters largely agreed, citing subtle ML and payments failures, but debated whether AI code deserves stricter scrutiny than coworker code, libraries, or unfamiliar systems.

### Comment pulse

- Apparent correctness can hide domain violations → commenters found data leakage, accounting discrepancies, duplicated abstractions, and patches that merely moved failures.

- Small, operator-controlled tasks form a practical middle ground → use agents for snippets, translation, types, documentation lookup, and grunt work after humans choose architecture.

- AI code merits stricter review because the submitter owns it → counterpoint: working coworker code should face the same maintainability standards.

### LLM perspective

- **View:** Generated code is a proposal, not an implementation, until a responsible engineer can defend its design and failure modes.

- **Impact:** Teams must budget review capacity, reduce diff size, and prevent throughput incentives from rewarding merged code over understood systems.

- **Watch next:** Track rejection rates, review time, escaped defects, rollback frequency, and outcomes by task risk and repository familiarity.
