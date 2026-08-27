# C++ says “We have try. . . finally at home”

- Score: 107 | [HN](https://news.ycombinator.com/item?id=46408984) | Link: https://devblogs.microsoft.com/oldnewthing/20251222-00/?p=111890

### TL;DR

C++ lacks a language-level `finally`, but scope-bound destructors provide comparable cleanup through RAII; helpers such as `wil::scope_exit` store a lambda whose destructor runs when control leaves the block. The important difference is exception behavior: Java, JavaScript, C#, and modern Python propagate a new exception from `finally`, while C++ terminates if a destructor throws during stack unwinding. HN largely favored RAII for pairing acquisition with release, but stressed that fallible cleanup—especially closing writable files—cannot always be safely hidden in destructors.

### Comment pulse

- RAII centralizes cleanup → resources release automatically across branching and exceptions without repeated, nested `finally` blocks.
- Destructors and `finally` are not equivalent → cleanup failures may need explicit reporting rather than termination or suppression.
- `defer` offers ergonomic scope cleanup → placing reversal beside acquisition aids review, though execution no longer follows source order.

### LLM perspective

- View: Cleanup syntax matters less than making ownership and failure semantics explicit at acquisition time.
- Impact: Libraries should separate infallible release guards from operations whose completion errors must reach callers.
- Watch next: Compare standard scope-guard proposals, exception chaining, and explicit-close guidance across language ecosystems.
