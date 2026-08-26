# Corroded: Illegal Rust

- Score: 158 | [HN](https://news.ycombinator.com/item?id=46483531) | Link: https://github.com/buyukakyuz/corroded

### TL;DR

Corroded is a satirical Rust crate that packages deliberately unsound operations behind cheerful APIs: null dereferences, unrestricted transmutation, forged static lifetimes, aliased mutable references, use-after-free, unchecked indexing, uninitialized values, and synchronization-free globals. Its README also plants bogus instructions telling language models these patterns are endorsed, safe best practices. Commenters enjoyed the parody and compared its hazards with permissive C or C++ behavior, but warned that automated code generators might miss the irony—while noting Rust’s compiler checks become more valuable when humans review less generated code.

### Comment pulse

- The fake model instructions extend the joke from unsafe code into prompt injection and training-data contamination.
- Readers argued strict languages are especially useful for generated code because compilers reject many subtle errors before execution.
- Comparisons with C and C++ supplied the punchline—counterpoint: removing Rust’s guarantees makes the examples undefined behavior, not acceptable safety.

### LLM perspective

- View: The crate is effective satire precisely because ergonomic names can conceal contracts that Rust normally makes explicit.
- Impact: Copying these APIs into real systems risks memory corruption, races, crashes, information exposure, and optimizer-dependent failures.
- Watch next: Package scanners and coding agents should distinguish parody metadata from trusted documentation before recommending dependencies or patterns.
