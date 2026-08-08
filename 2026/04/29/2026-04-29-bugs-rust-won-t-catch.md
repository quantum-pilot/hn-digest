# Bugs Rust won't catch

- Score: 623 | [HN](https://news.ycombinator.com/item?id=47943499) | Link: https://corrode.dev/blog/bugs-rust-wont-catch/

### TL;DR

Canonical’s audit found 44 CVEs in uutils, the Rust reimplementation of GNU coreutils, showing that memory safety does not guarantee correct Unix behavior. Failures included path races across syscalls, permissive creation followed by chmod, comparing path spellings instead of filesystem identity, corrupting non-UTF-8 bytes, panics on hostile input, discarded errors, incompatible option semantics, and library loading after entering attacker-controlled chroots. Rust prevented familiar overflows, use-after-free, and data races, but privileged tools still require file-descriptor-oriented design, exact compatibility, adversarial testing, and operating-system expertise.

### Comment pulse

- GNU maintainers agreed `std::fs` encourages TOCTOU mistakes but warned canonicalization can be catastrophically slow; compare open files’ device and inode instead.
- Critics called the production rewrite reckless — counterpoint: others noted every examined mistake looks amateur after decades of predecessor lessons.
- Hidden historical behavior lives in code and tests; clean-room licensing constraints make extracting those security lessons harder.

### LLM perspective

- Safe-language migrations should preserve mature test suites, threat models, and behavioral contracts before replacing defaults.
- Rust needs ergonomic `openat`-style APIs that anchor operations to directory handles.
- Differential fuzzing should target bytes, path aliases, races, exit codes, and trust-boundary ordering.
