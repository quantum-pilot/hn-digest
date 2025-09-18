# Object-oriented design patterns in C and kernel development

- Score: 248 | [HN](https://news.ycombinator.com/item?id=45023857) | Link: https://oshub.org/projects/retros-32/posts/object-oriented-design-patterns-in-osdev

- TL;DR
    - A kernel hobbyist shows how C structs of function pointers (“vtables”) provide encapsulation and polymorphism in an OS: uniform service APIs (start/stop/restart), hot-swappable schedulers (yield/block/add/next), and module-driven behavior changes at runtime—all echoing Linux’s file_operations. Downsides are verbosity and explicit “this,” which can improve clarity in kernel contexts. HN notes this pattern predates OOP (ADTs), contrasts NULL-optional ops with class hierarchies, cites dynamic messaging (Smalltalk/Objective‑C) and Go-like interfaces, and debates implicit vs explicit “this,” with a correction about typed vs void pointers.

- Comment pulse
    - ADT predates OOP → NULL-able function pointers make optional behavior simple; OOP needs extra classes or runtime checks — counterpoint: defaults/interfaces (e.g., Go) soften this.
    - Explicit this debated → explicit clarifies scope and dependencies; implicit this saves typing and reads cleaner with methods, avoiding object->ops->fn(obj).
    - Pattern scope → vtables used for polymorphism, not just memory; OP adds hot-swapping; correction: he uses typed pointers, not void pointers.

- LLM perspective
    - View: Vtables-in-C are a practical middle ground between ADTs and OOP, ideal where RTTI and exceptions are undesirable.
    - Impact: Easier hot-swapping of schedulers/services, cleaner driver interfaces, fewer rebuilds and reboots in embedded or kernel environments.
    - Watch next: Benchmarks for dispatch overhead, lockless vtable updates, ABI-stability rules for modules, and typed optional operations (NULL vs defaults).
