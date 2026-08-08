# ClojureScript Gets Async/Await

- Score: 258 | [HN](https://news.ycombinator.com/item?id=48059662) | Link: https://clojurescript.org/news/2026-05-07-release

### TL;DR

ClojureScript 1.12.145 adds native JavaScript async/await interop. Marking a function or test with `^:async` makes the compiler emit an async function, and `await` can be used inside its expression-oriented body, including nested lets and exception handling. Now that ClojureScript targets ECMAScript 2016, the feature removes extra dependencies for common Promise-based browser APIs and libraries. It was the most requested enhancement in the latest survey. Commenters welcomed simpler debugging and error behavior than core.async or macro libraries, while noting ClojureScript supported other asynchronous paradigms long before JavaScript did.

### Comment pulse

- Contributor Borkdude reportedly proved feasibility in Squint before transferring those lessons into the core compiler.
- Core.async remains powerful CSP-style machinery — counterpoint: critics cite larger bundles, weak error semantics, and transformed state-machine code that is difficult to debug.
- Broader discussion linked renewed Clojure interest to REPL-driven agent workflows, a recent documentary, and durable backward compatibility.

### LLM perspective

- Native emission improves stack traces and interop because generated control flow matches the host platform.
- Benchmark bundle size and source-map quality against Promesa and core.async before migrating.
- Watch for edge cases around macros, higher-order calls, cancellation, and Promise rejection propagation.
