# Malicious Rust crate Arrayref runs a build-time payload

- Score: 373 | [HN](https://news.ycombinator.com/item?id=49374269) | Link: https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/

### TL;DR

SafeDep reports that a compromised maintainer account published `arrayref` 0.3.10 alongside malicious `internment` and `append-only-vec` releases. `arrayref` added typosquatted `proc-macro1`, a working `proc-macro2` copy whose build script downloaded and detached an OS-specific payload during compilation. Older releases were yanked, nudging upgrades toward the bad version; crates.io removed the malicious releases. Its 245 million lifetime downloads show ecosystem reach, not infections. Commenters debated incident transparency, curated dependencies, richer standard libraries, and build sandboxing—counterpoint: malicious library code can execute later anyway.

### Comment pulse

- Critics wanted deleted-version markers and advisories; replies said response lag does not prove crates.io was unprepared.
- “Batteries included” advocates sought fewer dependencies, while opponents cited diverse domains, permanence, staffing, and stale standard-library risks.
- Build-script sandboxing drew support, but practical permissions and later execution of poisoned binaries limit protection.

### LLM perspective

- View: Account compromise combined with trusted transitive build execution created an unusually effective supply-chain path.
- Impact: Anyone who compiled affected releases on supported systems may need compromise investigation, not merely dependency rollback.
- Watch next: Second-stage analysis, transparent removal records, stronger publisher security, dependency auditing, and build-time network controls.
