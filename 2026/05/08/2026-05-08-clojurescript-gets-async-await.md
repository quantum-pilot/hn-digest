# ClojureScript Gets Async/Await

- Score: 258 | [HN](https://news.ycombinator.com/item?id=48059662) | Link: https://clojurescript.org/news/2026-05-07-release

### TL;DR
ClojureScript 1.12.145 introduces native-style async/await support for JavaScript interop. Marking a function with the `^:async` metadata makes the compiler emit a JavaScript `async function`, enabling `await` inside idiomatic ClojureScript code. This works both in regular functions and `deftest`s, simplifying interaction with Promise-based browser APIs and modern JS libraries. The feature targets ECMAScript 2016+, reflecting strong user survey demand and reducing reliance on third‑party async wrappers for common interop scenarios.

---

### LLM perspective
- View: This narrows the ergonomic gap between ClojureScript and TypeScript for Promise-based APIs while preserving Clojure’s core semantics.  
- Impact: Library authors can expose cleaner async APIs; app code sheds boilerplate around Promises and callback wrappers.  
- Watch next: Guidance on combining `^:async` with core.async, error handling patterns, and performance comparisons against hand-written Promise chains.
