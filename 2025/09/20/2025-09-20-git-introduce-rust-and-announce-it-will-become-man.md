# Git: Introduce Rust and announce it will become mandatory in the build system

- Score: 292 | [HN](https://news.ycombinator.com/item?id=45312696) | Link: https://lore.kernel.org/git/20250904-b4-pks-rust-breaking-change-v1-0-3af1d25e0be9@pks.im/

### TL;DR

A Git patch series proposes adding optional Rust infrastructure as a test balloon, converting the small dependency-free varint subsystem to verify C interoperability and build tooling. It gives distributors time to adapt before Rust becomes mandatory for building Git 3.0, especially on platforms where toolchain support is difficult. The initial RFC supported Meson and anticipated Makefile, CI, and formatting work. Commenters debated memory safety, contributor appeal, portability, and added complexity, while clarifying that Rust would be a build requirement—not a mandate that every contribution use Rust.

### Comment pulse

- Gradual adoption reduces disruption → optional support lets maintainers test interoperability while distributors prepare toolchains.
- Motivation remains debated → supporters cite safety and new contributors; skeptics question changing a mature C project.
- Hackability concerns are narrower than claimed → repository formats and external clients do not depend on Git’s implementation language.

### LLM perspective

- View: A trivial subsystem is an appropriate experiment because it tests integration without tying success to a major feature.
- Impact: Builders inherit another compiler; maintainers gain access to Rust safety and a wider contributor pool.
- Watch next: Track platform coverage, GCC Rust maturity, binary portability, CI cost, and defects found in mixed-language boundaries.
