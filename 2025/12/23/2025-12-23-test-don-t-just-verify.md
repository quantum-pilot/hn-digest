# Test, don't (just) verify

- Score: 154 | [HN](https://news.ycombinator.com/item?id=46364973) | Link: https://alperenkeles.com/posts/test-dont-verify/

## TL;DR

AI-fuelled formal verification promises provably correct software: autoformalized specs, proofs checked by Lean-like assistants, and verified reference implementations. The author welcomes this, but argues it cannot replace testing. Autoformalization becomes a fallible part of the trusted computing base; proof assistants run too slowly for production; many domains (performance, hardware) lack tractable models; and proofs can’t reveal a wrong spec. Random and differential testing, especially Verification-Guided Development, remain essential complements—comments debate how pessimistic this view should be.

---

## Comment pulse

- Formal methods progress is understated: Lean already scales to long math proofs and efficient arithmetic; hardware/cache models exist, but hand-calculations are tedious.  

- Verification training teaches invariants and reasoning; static types and Rust-like memory guarantees act as lightweight verification, complementing tests—even when full formal specs are unrealistic.  

- Some argue the post mischaracterizes Lean performance and spec practices; richer type-based libraries, not giant specs, will structure future verified software—counterpoint: library sprawl harms quality.  

---

## LLM perspective

- View: Random testing plus formal proofs is emerging as the practical sweet spot, especially with VGD-style verified references and optimized implementations.  

- Impact: AI-driven autoformalization will mainly benefit new, spec-first systems; legacy code will still lean heavily on tests, types, and partial verification.  

- Watch next: Watch benchmarks of AI provers on real-world codebases and more VGD deployments in compilers, databases, kernels, and safety-critical controllers.
