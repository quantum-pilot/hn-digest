# Functional programming and reliability: ADTs, safety, critical infrastructure

- Score: 141 | [HN](https://news.ycombinator.com/item?id=46406901) | Link: https://blog.rastrian.dev/post/why-reliability-demands-functional-programming-adts-safety-and-critical-infrastructure

### TL;DR

The article argues that reliability improves when domain models make illegal states unrepresentable. Using OCaml and TypeScript, it replaces magic strings, nulls, conflicting booleans, ambiguous numbers, and thrown expected errors with algebraic data types, exhaustive matching, Options, Results, branded units, immutability, and pure cores surrounded by effectful shells. Banking and telecom examples show typed transaction and call lifecycles preventing invalid settlement or billing. HN agreed these tools help, but challenged conflating static typing with functional programming and treating correctness as a substitute for fault tolerance.

### Comment pulse

- Strong types constrain both humans and code generators → precise interfaces shrink implementation space and improve compiler feedback.
- Reliability requires correctness and recovery → explicit states help retries and reconciliation, but cannot eliminate messy external failures.
- Functional programming is broader than static ADTs → purity, immutability, and controlled effects also benefit dynamically typed languages.

### LLM perspective

- View: Types are local proof tools; production reliability still depends on idempotency, redundancy, observability, and reconciliation.
- Impact: Teams can turn domain changes into compiler-guided edits while reducing runtime ambiguity and review burden.
- Watch next: Measure incident rates, repair time, and AI-generated defect rates before and after stronger modeling.
