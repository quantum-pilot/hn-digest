# A clickable visual guide to the Rust type system

- Score: 258 | [HN](https://news.ycombinator.com/item?id=45167401) | Link: https://rustcurious.com/elements/

- TL;DR
    - Clickable map of Rust’s type system emphasizing lang items—the built-in types/traits that enable syntax—and excluding library structs like Vec and String. It clarifies where the language ends and the standard library begins, useful for no_std and embedded contexts. HN readers praised the integer range callouts, debated symmetric signed integers with NaN vs two’s complement, and asked why PhantomData sits in the unsafe-support group (it aids dropck in unsafe patterns). Cheats.rs was recommended for lifetimes and memory-layout diagrams; the fixed-width layout also got kudos.

- Comment pulse
    - Appreciated integer range labels → help recall bounds; debate on symmetric NaN integers vs two's complement—counterpoint: CPUs lack integer NaN, inefficient.
    - PhantomData belongs in unsafe-support → signals ownership to dropck for pointer-owning types; primarily created to aid unsafe patterns.
    - cheats.rs recommended → clear visuals for lifetimes and memory layout; readers want such diagrams integrated into official docs.

- LLM perspective
    - View: Visual taxonomy separates language intrinsics from library types; great for understanding unsafe, generics, and no_std boundaries.
    - Impact: Instructors and embedded teams gain a reference to avoid misuse of lang items and PhantomData-driven drop semantics.
    - Watch next: Add compiler version gates, auto-trait coverage, and links to MIR/borrow-checker visuals; measure learning gains in courses.
