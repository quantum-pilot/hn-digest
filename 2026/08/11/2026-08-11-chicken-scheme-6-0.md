# Chicken Scheme 6.0

- Score: 296 | [HN](https://news.ycombinator.com/item?id=49251702) | Link: https://code.call-cc.org/releases/6.0.0/NEWS

### TL;DR

CHICKEN 6.0 moves its core closer to R7RS Small, adds every specified module, changes internal strings to UTF-8 for full Unicode, and replaces blobs with compatible bytevectors. Numerous APIs moved or changed, including process calls returning process objects and stricter R7RS syntax. FFI can now pass complex numbers and C structs or unions directly; compiler optimizations reuse closures; the build adopts configure, supports zig cc, and recommends w64devkit on Windows. Discussion welcomed the Unicode milestone and CHICKEN’s portable compile-to-C model.

### Comment pulse

- Users praised eggs, useful errors, compact standalone binaries, and C interoperability as the combination distinguishing CHICKEN from other Schemes.
- Crunch adds a statically typed R7RS subset, though it remains pre-1.0 and needs extra Windows setup.
- Documentation drew mixed reviews: core material is adequate, but egg coverage and reliable offline access remain weak.

### LLM perspective

- **View:** Standard conformance matters most when package tooling makes shared semantics usable in real projects.
- **Impact:** Unicode and R7RS support reduce portability work, while changed APIs impose immediate migration costs.
- **Watch next:** Offline egg documentation, conformance suites, Crunch 1.0, and simpler Windows setup.
