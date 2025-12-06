# Patterns for Defensive Programming in Rust

- Score: 181 | [HN](https://news.ycombinator.com/item?id=46163609) | Link: https://corrode.dev/blog/defensive-programming/

- TL;DR  
The article shows how to turn “this should never happen” comments into compile-time guarantees using small, idiomatic Rust patterns. It recommends slice pattern matching instead of indexing, explicit field initialization over blanket Default, destructuring in trait impls, preferring TryFrom, exhaustive matches, descriptive unused fields, temporary mutability, constructor-enforced validation (via private fields or sealing), must_use return types, and enums/parameter structs instead of bools. Comments debate equality design, share real bugs from unsafe indexing, and connect these ideas to LLM-generated Rust.

- Comment pulse  
  - Equality semantics debate → Some prefer decomposing PizzaOrder into PizzaDetails vs timestamp; others argue equality should remain strict—counterpoint: decomposition doesn’t cover all comparison notions.  
  - Indexing lessons → Readers report production bugs from slice overflows, now prefer iterators and compiler-enforced bounds instead of manual indices.  
  - Enums vs bools → Enums plus helper methods or matches give clearer APIs than raw booleans, even if slightly less syntactically convenient.

- LLM perspective  
  - View: Patterns encode domain assumptions in types, giving automated code generators safer rails than comments and ad-hoc checks.  
  - Impact: Stronger defaults in libraries and templates could make novice and LLM-written Rust code more robust with minimal effort.  
  - Watch next: Measure defect rates and effort in codebases that adopt these Clippy lints and patterns versus conventional Rust styles.
