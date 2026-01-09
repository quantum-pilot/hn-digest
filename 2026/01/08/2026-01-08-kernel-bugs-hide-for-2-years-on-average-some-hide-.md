# Kernel bugs hide for 2 years on average. Some hide for 20

- Score: 277 | [HN](https://news.ycombinator.com/item?id=46536340) | Link: https://pebblebed.com/blog/kernel-bugs

### TL;DR

Mining 20 years of Linux git history via `Fixes:` tags, the author traces 125k bug–fix pairs and finds kernel bugs live a mean 2.1 years, with some surviving 10–20. Race conditions and networking subsystems (e.g., CAN, SCTP) hide longest; null derefs are found fastest. A 19‑year refcount leak case study shows how rare sequences and subtle logic errors evade tests. The VulnBERT model fuses CodeBERT with handcrafted bug features to flag bug‑introducing commits at review time with 92% recall and 1.2% FPR. HN discussion focuses on how far Rust and better types help, what “bug lifetime” really measures, and how similar long‑lived races appear in application code.

---

### Comment pulse

- Rust helps mainly by removing large classes of memory bugs; this frees attention for deep logic/concurrency issues—counterpoint: borrow checking doesn’t magically fix DMA/spec misunderstandings.  
- Long bug lifetimes do not imply low severity; severe UAFs and races can lurk for years because they rarely trigger or are hard to reproduce.  
- Similar multi‑year lifetimes appear in browsers (e.g., CSP bugs) and app state machines, where only rare input or timing patterns expose flaws.

---

### LLM perspective

- View: Treat “commit risk scoring” like static analysis: always-on, noisy-but-cheap, guiding reviewers and fuzzers toward the most suspicious changes.  
- Impact: Most leverage for large C/C++ codebases with good metadata (Fixes tags, subsystem labelling) and many infrequent, subtle bugs.  
- Watch next: Port VulnBERT-style hybrids to other kernels/browsers, and wire them into CI + fuzzing to auto-prioritize high-risk code paths.
