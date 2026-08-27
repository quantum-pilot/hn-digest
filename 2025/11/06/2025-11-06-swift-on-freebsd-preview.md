# Swift on FreeBSD Preview

- Score: 165 | [HN](https://news.ycombinator.com/item?id=45837871) | Link: https://forums.swift.org/t/swift-on-freebsd-preview/83064

### TL;DR

The Swift project published a preview development bundle for FreeBSD 14.3 or newer on x86-64, including the compiler and runtimes. Installation currently requires zlib-ng, Python 3, SQLite, libuuid, and curl. Known limitations include ThreadSanitizer test failures, LLDB’s inability to evaluate Swift expressions, hanging command plugins, a C++ interoperability issue, and FreeBSD system modules still imported through “Glibc”; LLDB and lld also expect an unavailable libxml2 version. The team is investigating aarch64 and support across FreeBSD 14 minor releases.

### Comment pulse

- Commenters welcomed another non-Apple platform while debating how much GUI support matters for Swift adoption.
- Several inferred Python supports tooling or tests, not necessarily compiled Swift programs, and asked who will own packaging.

### LLM perspective

- View: This is meaningful compiler portability work, but the preview’s debugger and plugin gaps limit daily development.
- Impact: FreeBSD users can begin testing Swift services and expose platform assumptions upstream.
- Watch next: aarch64 builds, package ownership, LLDB expression support, plugin reliability, and native FreeBSD module naming.
