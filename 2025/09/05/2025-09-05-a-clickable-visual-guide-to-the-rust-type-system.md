# A clickable visual guide to the Rust type system

- Score: 266 | [HN](https://news.ycombinator.com/item?id=45140572) | Link: https://rustcurious.com/elements/

### TL;DR

RustCurious presents a clickable map of Rust’s core types and language-integrated traits, aiming to show that every possible Rust type fits within its boxes. It deliberately excludes familiar library structures such as `Vec`, `String`, and `HashMap`, emphasizing the boundary between compiler-supported language items and ordinary library code. That separation helps explain Rust’s platform-independent core and `no_std` use without a dynamic heap. Readers found the compact overview approachable, though one commenter argued its periodic-table-like groupings create visual correspondences that are sometimes arbitrary rather than explanatory.

### Comment pulse

- Several readers praised the page’s density and accessibility, especially for people familiar with other statically typed languages.
- One detailed critique says the arrangement implies relationships that the Rust type system does not actually support.

### LLM perspective

- View: The guide works best as a navigational index, not a formal taxonomy of type relationships.
- Impact: Distinguishing language items from library structs can clarify what remains available in constrained `no_std` environments.
- Watch next: Whether future revisions explain grouping choices and link each visual relationship to precise semantics.
