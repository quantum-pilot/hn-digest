# A clickable visual guide to the Rust type system

- Score: 258 | [HN](https://news.ycombinator.com/item?id=45167401) | Link: https://rustcurious.com/elements/

### TL;DR

This compact interactive reference maps Rust's possible types, emphasizing language items: built-in types and traits that enable specific syntax. It intentionally omits familiar library collections such as `Vec`, `String`, and `HashMap` because they are ordinary structs, and highlights the platform-independent `core` foundation behind `no_std` software without a dynamic heap. The frozen text does not reproduce the clickable diagram itself, so much of the resource's value is visual. HN readers praised integer ranges, layout, and its usefulness as a bookmark.

### Comment pulse

- Integer ranges make the page practical → readers appreciated a quick reminder of two's-complement asymmetry.
- Visual references complement API documentation → commenters also valued graphical treatments of lifetimes and memory layouts.
- Category choices prompt useful questions → `PhantomData` appears under unsafe support because it informs ownership and drop checking.

### LLM perspective

- View: The guide teaches Rust's language boundary by separating compiler-recognized machinery from ordinary library-defined structures.
- Impact: Learners can form a clearer taxonomy before confronting ownership, embedded constraints, or unsafe abstractions.
- Watch next: Coverage updates, accessibility without interaction, stable-versus-unstable distinctions, and links from each category to canonical documentation.
