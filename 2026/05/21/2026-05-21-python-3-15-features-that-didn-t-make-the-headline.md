# Python 3.15: features that didn't make the headlines

- Score: 321 | [HN](https://news.ycombinator.com/item?id=48220696) | Link: https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html

### TL;DR

Python 3.15’s quieter additions target awkward edges: `TaskGroup.cancel()` stops structured-concurrency groups without exception scaffolding; `ContextDecorator` now spans coroutine and generator lifetimes; and threading helpers safely serialize, synchronize, or duplicate iterator consumption. `Counter` gains xor, while JSON loaders can pair `array_hook` with `object_hook` to build immutable trees from tuples and `frozendict`. HN reaction favored the concurrency ergonomics but exposed sharper questions about backward compatibility, algebraic consistency, documentation accuracy, and whether lazy imports solve genuine design problems or conceal import-heavy codebases.

### Comment pulse

- Lazy-import value remains situational → module-scope annotations may still force evaluation, while earlier versions can emulate deferred module attributes through `__getattr__`.
- Counter coverage needs correction → the subtraction example is wrong, while xor’s absolute count difference is non-associative and lacks an obvious use case.
- ContextDecorator’s automatic lifecycle handling could alter existing behavior → counterpoint: deliberately relying on the previous immediate exit is considered improbable.

### LLM perspective

- **View:** Lifecycle and concurrency guarantees matter most because they replace bespoke exception, queue, and wrapper patterns rather than shorten syntax.
- **Impact:** Free-threaded applications gain standard iterator coordination, while library maintainers should retest context-manager decorators around generators and coroutines.
- **Watch next:** Beta compatibility reports, iterator throughput under contention, decorator regressions, lazy-import startup measurements, and clarification of Counter xor semantics.
