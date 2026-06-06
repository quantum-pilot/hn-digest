# Debian must ship reproducible packages

- Score: 339 | [HN](https://news.ycombinator.com/item?id=48081245) | Link: https://lists.debian.org/debian-devel-announce/2026/05/msg00001.html

- TL;DR  
  Debian is making reproducible builds a requirement for shipped packages, turning a decade-long experimental effort into baseline policy. Supporters see this as a major supply‑chain security milestone and a statement of Debian’s quality bar. Skeptics argue reproducibility hasn’t yet blocked concrete attacks and mainly increases maintainer friction. Commenters compare Debian’s progress with NetBSD and projects like stagex that also pursue fully bootstrapped, hermetic builds, debating how far “reproducible” must go to meaningfully increase trust.  

*Content unavailable; summarizing from title/comments.*

### Comment pulse
- Reproducible‑by‑policy is hailed as a huge Debian milestone built over many years → stronger trust in binaries—counterpoint: no past Debian attack would have been stopped.  
- Most packages already build reproducibly; only ~5% fail CI → new rule mainly forces cleanup of edge cases, not an overnight ecosystem rewrite.  
- Others note NetBSD and stagex achieved fully reproducible, even source‑bootstrapped systems → argue Debian still leans on opaque binary seeds—counterpoint: Debian’s scale is far larger.  

### LLM perspective
- View: Debian normalizing reproducible builds turns a niche hardening practice into an expected default for general‑purpose Linux distributions.  
- Impact: Maintainers must fix non‑deterministic toolchains and packaging quirks; downstream distros and auditors gain easier verification of official binaries.  
- Watch next: Whether Debian moves from reproducible‑from‑binaries toward fully bootstrapped, audited build roots, and how tooling automates verification at scale.
