# Openrsync: An implementation of rsync, by the OpenBSD team

- Score: 307 | [HN](https://news.ycombinator.com/item?id=48334854) | Link: https://github.com/kristapsdz/openrsync

### TL;DR

Openrsync is an ISC-licensed rsync implementation now merged into OpenBSD base, originally built for its RPKI validator. It speaks protocol 27 and interoperates with modern rsync while supporting only a subset of command-line options. Its roughly 10,000 lines of C combine receiver and generator work in an event loop; OpenBSD builds use pledge and unveil, while portability glue targets several Unix systems. Hacker News welcomes an auditable alternative but reports friction around destination semantics, trailing slashes, limited flags, and macOS script breakage.

### Comment pulse

- A user’s file-to-path transfer unexpectedly nested the basename; replies suggest pre-existing directories and slash semantics may explain behavior rather than incompatibility.
- Source trailing slashes copy directory contents; omission copies the directory itself, a familiar but persistently confusing rsync convention.
- Commenters value implementation diversity amid alleged upstream regressions, citing a Go alternative and macOS adoption as signs the ecosystem need not depend on one codebase.

### LLM perspective

- **View:** Protocol-compatible replacements reduce monoculture risk, but behavioral compatibility extends beyond wire format to decades of CLI edge cases.
- **Impact:** OpenBSD gains a sandboxed base utility; cross-platform users gain another implementation with migration testing costs.
- **Watch next:** Option coverage, interoperability tests, path-semantics fixes, portability sandboxes, and macOS compatibility notes.
