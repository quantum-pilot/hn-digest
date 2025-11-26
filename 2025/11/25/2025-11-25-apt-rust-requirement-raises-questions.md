# APT Rust requirement raises questions

- Score: 240 | [HN](https://news.ycombinator.com/item?id=46045972) | Link: https://lwn.net/SubscriberLink/1046841/5bbf1fc049a18947/

### TL;DR
Debian’s APT maintainer Julian Klode plans to require Rust for APT from May 2026, mainly to get memory‑safe parsing and PGP verification via Sequoia-PGP. In practice, only a few very old, unofficial ports (alpha, m68k, hppa, sh4) are affected, which can stay on older APT or work to bootstrap Rust. The real controversy is governance and process: a Canonical‑employed maintainer announcing a major dependency and implied deadline unilaterally, despite unresolved Rust tooling, static-linking, and security-maintenance issues in Debian.

---

### Comment pulse
- Governance and tone → Unilateral “Rust or sunset your port” email, plus “retro computers” rhetoric, felt hostile and Canonical‑driven to some — counterpoint: affected ports are obscure and shouldn’t block progress.  
- Technical scope → Many like the idea to split APT so only Canonical‑centric tools (apt-ftparchive, etc.) need Rust, while core package management stays C++/portable.  
- Broader Rust debate → Rust’s ecosystem (cargo, static linking, many crates) clashes with distro practices; some blame “rewrite it in Rust” zealotry, others say distros must invest or accept upstream norms.

---

### LLM perspective
- View: The technical change is modest; the social misstep is large, exposing Debian’s friction over modernization and corporate influence.  
- Impact: Debian ports, security team, and infra tools must either handle Rust’s static-linking model or cordon off Rusty components.  
- Watch next: Debian policy on Static-Built-Using, Rust toolchain coverage on fringe arches, and whether APT is modularized to isolate Rust-dependent utilities.
