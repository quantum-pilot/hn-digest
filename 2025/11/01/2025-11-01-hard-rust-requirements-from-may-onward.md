# Hard Rust requirements from May onward

- Score: 309 | [HN](https://news.ycombinator.com/item?id=45779860) | Link: https://lists.debian.org/debian-devel/2025/10/msg00285.html

### TL;DR

A Debian APT developer plans, no earlier than May 2026, to introduce hard Rust dependencies through the compiler, standard library, and Sequoia. Proposed Rust work covers parsing untrusted `.deb`, `.ar`, and `.tar` data, HTTP handling, and signature verification, with memory safety and testing as motivations. Ports lacking a working Rust toolchain were asked to become ready within six months or face retirement. This is a maintainer's announced direction, not a completed migration, and comments dispute its compatibility and rewrite risks.

### Comment pulse

- Supporters prioritized memory safety for parsers handling untrusted data and argued Rust already covers most relevant architectures.
- Skeptics questioned replacing mature C code, introducing new bugs, and narrowing support for unofficial ports.

### LLM perspective

- View: APT's security boundary makes safer parsing attractive, but migration quality matters more than language choice alone.
- Impact: The requirement may simplify maintenance while forcing marginal architectures to solve tooling gaps or disappear.
- Watch next: Examine staged rewrites, differential tests, fuzzing results, bootstrap options, and concrete port readiness before May.
