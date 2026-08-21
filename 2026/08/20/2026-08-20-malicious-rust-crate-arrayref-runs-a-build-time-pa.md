# Malicious Rust crate Arrayref runs a build-time payload

- Score: 373 | [HN](https://news.ycombinator.com/item?id=49374269) | Link: https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/

### TL;DR
A compromised crates.io account for popular Rust crate `arrayref` published version 0.3.10 that silently depends on fake crate `proc-macro1`. That crate’s build script downloads an architecture-specific payload from a hard‑coded IP and executes it during compilation, detached from Cargo so builds succeed while malware runs. Several related crates were removed and indicators of compromise (IP, file paths, hashes) are documented. HN discussion focuses on crates.io/GitHub incident handling, thin stdlibs driving dependency sprawl, and how to harden Cargo build scripts and ecosystems.

---

### Comment pulse
- Incident response UX is poor → deleted versions and vanished GitHub repos give no “removed for malware” state or advisory link—counterpoint: Rust team has a documented, improving process.  
- Many blame thin stdlibs → dependency sprawl increases attack surface; others say “batteries included” is unrealistic for general-purpose languages and expensive without big corporate backing.  
- Hardening Cargo → calls for sandboxed `build.rs` and curated, audited core crates; skeptics note sandbox limits and that payloads can move into normal library code.

---

### LLM perspective
- View: Build-time code execution plus transitive dependencies creates a stealthy, high-impact supply-chain vector even in memory-safe languages.  
- Impact: Expect stricter crate policies, improved publisher verification, and more scrutiny of unusual build dependencies or network-using build scripts.  
- Watch next: Concrete Cargo RFCs on sandboxing/permissions, explicit “malicious-removed” crate state, and emergence of community-curated Rust dependency baselines.
