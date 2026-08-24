# C isn't a programming language anymore (2022)

- Score: 106 | [HN](https://news.ycombinator.com/item?id=46907350) | Link: https://faultlore.com/blah/c-isnt-a-language/

### TL;DR

Aria Desires argues C is now both language and de facto protocol: general-purpose languages must speak its ABI to call operating systems and one another. C headers require compiler-level preprocessing, while layouts and calling conventions vary by target and can differ between Clang and GCC. Foreign runtimes therefore hard-code platform definitions, making fixes such as enlarging `intmax_t` ecosystem-breaking. Symbol versioning, opaque types, and self-sized records can preserve compatibility. Commenters debated whether C’s longevity justifies this dominance or a language-neutral interoperability standard could improve it without recreating COM or CORBA complexity.

### Comment pulse

- C’s success freezes mistakes → operating systems, libraries, and foreign runtimes embed representations that standards or platforms cannot safely revise.
- C offers unmatched durability → decades-old code remains serviceable — counterpoint: critics distinguish historical entrenchment from technical merit.
- Cleaner interoperability risks new complexity → commenters proposed an explicit ABI or IDL, then invoked COM and CORBA as cautionary precedents.

### LLM perspective

- View: The complaint targets C as the universal in-process interface, not its usefulness as an implementation language.
- Impact: Language authors inherit header parsing, target layouts, calling conventions, and compatibility work without adopting C’s source semantics.
- Watch next: Machine-readable ABI specifications, compiler conformance tests, Rust’s `crabi`, versioned types, opaque interfaces, and language-neutral IDL experiments.
