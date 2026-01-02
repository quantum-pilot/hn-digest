# Rust--: Rust without the borrow checker

- Score: 115 | [HN](https://news.ycombinator.com/item?id=46453062) | Link: https://github.com/buyukakyuz/rustmm

### TL;DR
Rust-- is a fork of the Rust compiler where the borrow checker is disabled, letting you compile code that normally fails Rust’s ownership and borrowing rules (e.g., use-after-move, multiple mutable references, self-referential structs). The binary and examples demonstrate such patterns “working” at compile time. HN discussion stresses this doesn’t change Rust’s runtime or aliasing rules: violating them is still undefined behavior and breaks optimizer assumptions, effectively turning Rust into C++. Many treat it as an educational or joke project, not for production.

---

### Comment pulse
- Borrow checker pain is mostly a learning phase → once you design with ownership in mind, it “keeps you honest.” Lifetimes are where many still struggle.
- Thinking in ownership and limited mutation improves code quality even in other languages → counterpoint: relying on copying everywhere wastes memory/CPU instead of learning correct sharing.
- Disabling borrowck only removes static checks → optimizer still assumes Rust’s aliasing rules; violating them yields C++-style UB, despite compiling and maybe “seeming” to work.

---

### LLM perspective
- View: Treat Rust-- as “unsafe mode everywhere”; useful for experiments, but indistinguishable from C++ in soundness risks.
- Impact: Could help people understand why the borrow checker exists by showing how easily “working” code can be subtly wrong.
- Watch next: Dynamic tools that detect borrow-rule violations at runtime; experiments with more flexible, gradual borrow-checking for difficult patterns.
