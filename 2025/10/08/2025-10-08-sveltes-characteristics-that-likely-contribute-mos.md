# Svelte’s characteristics that likely contribute most to improved performance

- Score: 171 | [HN](https://news.ycombinator.com/item?id=45519915) | Link: https://chuniversiteit.nl/papers/svelte-is-fast

- TL;DR
  - A 2022 study compared Angular, React, Vue, Svelte, and Blazor, linking rendering strategies to performance. Svelte leads by compiling components, tracking dirtiness and hoisting static content; Vue benefits from fine-grained bindings; vDOM diffing and Blazor’s JS interop add overhead. Benchmarks show Svelte fastest across create/update tasks, especially at scale. HN debates recency and relevance amid Svelte 5, React/Angular changes; some praise Svelte but criticize SvelteKit UX; others note WebAssembly can be fast beyond Blazor.

- Comment pulse
  - Evidence is outdated → Study uses 2020–2021 versions; Svelte 5 and Angular/React changes may alter rankings — counterpoint: Svelte’s binding/compile-time approach remains, so trends persist.
  - Wasm isn’t inherently slow → Blazor suffers JS interop overhead; Rust frameworks (Leptos, Dioxus) hit near-vanilla results on comparable benchmarks.
  - Svelte praised; SvelteKit criticized → Developers enjoy Runes and components, but dislike Kit’s magic-file routing and perceived complexity versus Svelte’s original simplicity.

- LLM perspective
  - View: Benchmarks isolate script time; UX also hinges on network, layout, hydration strategy, and memory—architectural choices still matter.
  - Impact: Compiler-first patterns spread beyond Svelte; expect convergence and fewer framework-specific pitfalls for large trees.
  - Watch next: Updated benchmarks for Svelte 5, React 19/Compiler, Angular Signals, Vue 3.x; Blazor AOT and Wasm DOM-access proposals.
