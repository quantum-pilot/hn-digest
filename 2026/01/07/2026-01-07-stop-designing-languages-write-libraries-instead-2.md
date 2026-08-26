# “Stop Designing Languages. Write Libraries Instead” (2016)

- Score: 215 | [HN](https://news.ycombinator.com/item?id=46525640) | Link: https://lbstanza.org/purpose_of_programming_languages.html

### TL;DR

The essay rejects the apparent choice between better languages and better libraries. Libraries create most visible productivity, but their power and ergonomics are bounded by language semantics: Rails depends on Ruby metaprogramming, runtime evaluation, first-class functions, dynamic typing, and garbage collection. C, Java, Scheme, and Stanza illustrate different ceilings for reusable abstractions, event handling, continuations, and static checking. The author therefore defines a general-purpose language by which powerful, approachable libraries it permits—and by which capabilities cannot be implemented as libraries at all.

### Comment pulse

- Prolog prompted debate over whether relational semantics can survive as a library without first-class variables, search, and specialized runtimes.
- Scala experiences split readers: language-integrated abstractions can replace Java boilerplate, yet DSL-heavy cultures may burden maintainers.
- Others called the framing a false dichotomy and emphasized implementations, interoperability, and ecosystem maturity alongside syntax.

### LLM perspective

- View: A language’s value is less feature count than the abstraction budget it grants library authors.
- Impact: Choosing a conservative language can externalize complexity into frameworks, generators, conventions, and repetitive application code.
- Watch next: Extensible type systems and portable runtimes may blur the boundary without eliminating ecosystem tradeoffs.
