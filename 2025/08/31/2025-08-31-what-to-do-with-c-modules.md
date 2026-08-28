# What to do with C++ modules?

- Score: 226 | [HN](https://news.ycombinator.com/item?id=45086210) | Link: https://nibblestew.blogspot.com/2025/08/we-need-to-seriously-think-about-what.html

### TL;DR

Meson creator Jussi Pakkanen argues that C++ modules should be removed unless they demonstrate at least 5× compilation speedups across multiple existing projects. He says their original performance promise gave way to interface isolation, while five years of incomplete tooling exposed a coordination gap among standards, compilers, scanners, and build systems. Current `import std` gains may resemble precompiled headers, perhaps only 10–20%. Adoption also demands refactoring, newer toolchains, portability compromises, and more complex builds without proven developer payoff.

### Comment pulse

- Supporters value explicit exported interfaces, macro isolation, and escape from header dependency graphs even without dramatic speed gains.
- Critics said standardizing an unproven cross-tool design created complexity that incremental prototypes could have exposed earlier.
- D’s module experience was offered as mature prior art, alongside calls to constrain or replace preprocessor metaprogramming.

### LLM perspective

- View: The disagreement is fundamentally about whether encapsulation alone justifies ecosystem-wide migration costs.
- Impact: Library and build-tool authors bear integration work long before ordinary developers receive consistent benefits.
- Watch next: Reproducible multi-project benchmarks, stable cross-tool protocols, and real-world `import std` portability.
