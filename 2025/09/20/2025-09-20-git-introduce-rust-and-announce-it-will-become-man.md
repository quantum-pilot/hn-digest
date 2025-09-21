# Git: Introduce Rust and announce it will become mandatory in the build system

- Score: 292 | [HN](https://news.ycombinator.com/item?id=45312696) | Link: https://lore.kernel.org/git/20250904-b4-pks-rust-breaking-change-v1-0-3af1d25e0be9@pks.im/

TL;DR
- Git is adopting Rust with a staged plan: optional initially, later a mandatory build dependency, likely when GCC supports Rust to preserve broad platform coverage. Motivations include memory safety beyond C, ongoing feature development, and attracting contributors who prefer Rust. Critics worry Git is “done,” Rust adds toolchain complexity, and GCC’s Rust may lag. Clarification: Rust becomes required to build Git, not for all future patches or rewrites. Supporters note Git’s polyglot history and say repo formats/hackability won’t change.

Comment pulse
- GCC track record skepticism → gcj’s failure and no Rust standard raise fears of divergence or stale compilers.
- Feature headroom examples → jj and git-branchless demonstrate in-memory merges and improved UX enabled by Rust implementations.
- Barrier-to-entry debate → Added toolchain/language vs. Git already using C/shell/Perl/Tcl; many developers prefer Rust.

LLM perspective
- View: Staged mandate balances safety and contributor pipeline without forcing rewrites or blocking C-only contributions.
- Impact: Distros/CI must ship Rust toolchains; long-tail platforms may struggle; build docs need clearer environment requirements.
- Watch next: gccrs stabilization, first Rust components landing, measurable perf/security wins, and a fallback plan where Rust isn’t available.
