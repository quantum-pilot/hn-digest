# Object-oriented design patterns in C and kernel development

- Score: 248 | [HN](https://news.ycombinator.com/item?id=45023857) | Link: https://oshub.org/projects/retros-32/posts/object-oriented-design-patterns-in-osdev

### TL;DR

An operating-system developer demonstrates polymorphism in C by storing typed function pointers in operation tables and giving each object a pointer to its table. Their kernel uses this pattern for services with common lifecycle commands and schedulers whose policies can change without rewriting callers. Linux file operations illustrate the same uniform-interface idea across different resources. Runtime table replacement can also support modules, provided synchronization is correct. The tradeoffs are verbose calls and explicit context parameters, which the author sees as both clumsy and useful for revealing dependencies.

### Comment pulse

- Readers debated whether the pattern is object orientation, an abstract data type, or older data abstraction.
- Several preferred explicit `this`, while others disliked naming the object twice in each call.
- Comments clarified that the example uses typed functions returning `void`, not untyped `void` pointers.

### LLM perspective

- View: The label matters less than the explicit contract and controlled indirection the table provides.
- Impact: Operation tables enable subsystem substitution without requiring C++ runtime machinery.
- Watch next: Audit null operations, lifetime rules, synchronization, ABI stability, and hot-swap failure recovery.
