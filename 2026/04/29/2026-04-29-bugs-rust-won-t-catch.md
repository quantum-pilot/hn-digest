# Bugs Rust won't catch

- Score: 623 | [HN](https://news.ycombinator.com/item?id=47943499) | Link: https://corrode.dev/blog/bugs-rust-wont-catch/

- TL;DR  
  Canonical’s audit of uutils (Rust coreutils) found 44 CVEs that Rust’s borrow checker, Clippy, and cargo-audit can’t see, because they live at the OS/semantics boundary: TOCTOU races from path-based std::fs APIs, permission and path-identity mistakes, UTF‑8 assumptions over raw bytes, panics as DoS, discarded errors, behavior drift from GNU, and trust-boundary mixups like chroot+NSS. Rust still eliminated classic memory bugs, but correctness and Unix semantics require explicit “defensive Rust” patterns and bug-for-bug compatibility.

- Comment pulse  
  Rewriting vs original code → Decades of production harden GNU coreutils; rewrites re-learn old lessons and miss edge cases—counterpoint: uutils does run GNU’s test suite.  
  Rust stdlib and APIs → Path-based std::fs makes TOCTOU easy; better to expose fd/at-style ops and dev+inode checks than rely on canonicalize.  
  Canonical’s rollout and process → Shipping a full Rust rewrite as default core tools was premature; fuzzing and tests missed many issues, users became unwitting test subjects.

- LLM perspective  
  View: Treat “safe” Rust as memory-safe, not correctness-safe; design APIs that encode Unix realities (fds, bytes, error propagation).  
  Impact: Systems programmers and library authors must adopt stricter patterns and add compatibility and semantics tests, not just rely on type safety.  
  Watch next: Stronger fd-based std APIs, better differential fuzzing against GNU, and formalized “defensive Rust” guides baked into tooling and lints.
