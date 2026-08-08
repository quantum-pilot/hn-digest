# Debian must ship reproducible packages

- Score: 339 | [HN](https://news.ycombinator.com/item?id=48081245) | Link: https://lists.debian.org/debian-devel-announce/2026/05/msg00001.html

### TL;DR

Debian’s release team has made reproducibility a migration requirement for Forky: new packages that cannot be rebuilt identically, and testing packages that regress, are now blocked from progressing. Migration tooling also runs autopkgtests for binary-only non-maintainer uploads. Adding loong64 required multi-architecture rebuilds, so the tests have enlarged the CI queue; uploaders remain responsible for resolving blockers and filing release-critical bugs against failing reverse dependencies. Commenters celebrated a long-running supply-chain milestone, while critics questioned added contributor friction and others stressed that reproducible Debian packages are not equivalent to source-bootstrapped, hermetic builds.

### Comment pulse

- Supporters called nondeterministic compiler output a longstanding bug and connected deterministic rebuilds to lessons from supply-chain compromises such as SolarWinds.
- Skeptics saw no Debian attack since 2007 this would have prevented — counterpoint: prevention and independent verification matter before a known incident.
- Comparisons with NetBSD and StageX highlighted scope: fewer packages ease reproducibility, while mandatory multi-party, source-bootstrapped releases provide stronger guarantees.

### LLM perspective

- View: Enforcing the property at migration converts a best-effort metric into a release invariant.
- Impact: Maintainers absorb diagnostic work, while users gain stronger evidence that distributed binaries correspond to declared sources.
- Watch next: Blocked-package rate, exception policy, CI latency, toolchain fixes, bootstrap provenance, and whether reproducibility reaches release artifacts end-to-end.
