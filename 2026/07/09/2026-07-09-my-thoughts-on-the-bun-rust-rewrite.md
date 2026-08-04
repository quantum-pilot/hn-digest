# My thoughts on the Bun Rust rewrite

- Score: 627 | [HN](https://news.ycombinator.com/item?id=48843352) | Link: https://andrewkelley.me/post/my-thoughts-bun-rust-rewrite.html

### TL;DR

Zig founder Andrew Kelley argues Bun’s Rust rewrite reflects a broken relationship and neglected engineering discipline more than language differences. He alleges Bun accumulated debt, ignored Zig guidance, and credited Rust for gains attributable to link-time optimization or cleanup. He questions whether tests can validate a million lines of generated code, disputes Bun’s fuzzing account, and requests compile-speed comparisons. Kelley welcomes the separation but admits resentment made his post personal and apologizes to worried Zig users. HN debated his professionalism, fuzzing evidence, stewardship risk, and whether candor justified reputational damage.

### Comment pulse

- The technical thesis is culture over language → bug rates depend on sustained cleanup, review, fuzzing, and project discipline, not safety features alone.
- Fuzzing became a factual flashpoint → Bun linked integrations and fixes — counterpoint: that evidence may not resolve what its team previously told ZSF.
- Tone altered the substance’s reception → personal management allegations and celebratory language made readers evaluate Zig stewardship instead of the rewrite claims.

### LLM perspective

- **View:** The post mixes engineering claims, personal testimony, and institutional rivalry; each requires different evidence and separate evaluation.
- **Impact:** Public conflict between flagship users and language maintainers can influence adoption, contributor trust, donations, hiring, and perceived supply-chain risk.
- **Watch next:** Compare benchmarks, audit generated code, reconstruct fuzzing timelines, and assess whether Rust improves maintainability after migration novelty fades.
