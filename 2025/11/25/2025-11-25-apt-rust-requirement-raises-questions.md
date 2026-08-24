# APT Rust requirement raises questions

- Score: 240 | [HN](https://news.ycombinator.com/item?id=46045972) | Link: https://lwn.net/SubscriberLink/1046841/5bbf1fc049a18947/

### TL;DR

APT maintainer Julian Andres Klode plans a direct Rust dependency in May 2026 for archive parsing and HTTP signature verification with Sequoia. Official Debian release architectures already support Rust, but several unofficial legacy ports would need toolchains, remain on older APT, or sunset. Critics challenge the deadline, unilateral tone, and avoidable coupling, suggesting niche parsers become optional modules. Supporters argue obsolete ports should not impede safer modernization. Debian’s unfinished policies for statically linked Rust crates, security rebuilds, and dependency tracking add a separate maintenance concern.

### Comment pulse

- Requiring Rust can modernize parsing and verification → supported architectures already ship relevant tooling — counterpoint: maintainers question the unilateral process.
- Modularizing niche parsers would preserve portability → only limited utilities need them, avoiding a core dependency for every build.
- Static Rust dependencies complicate security maintenance → crate rebuild and vulnerability-tracking policy remains unfinished.

### LLM perspective

- View: The technical case is plausible, but Debian should pair it with modularity and explicit project governance.
- Impact: Unofficial legacy ports may lose current APT unless volunteers deliver reliable Rust toolchains.
- Watch next: Technical Committee action, parser modularization, port maintainers, and Static-Built-Using policy.
