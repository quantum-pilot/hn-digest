# Bombadil: Property-based testing for web UIs

- Score: 220 | [HN](https://news.ycombinator.com/item?id=47436592) | Link: https://github.com/antithesishq/bombadil

### TL;DR
Bombadil is a new Rust-based tool for property-based testing of web UIs. Instead of scripting fixed flows like Cypress/Playwright, you define JS/TS temporal properties over DOM state; Bombadil then drives the browser via randomized “action generators” and online LTL monitoring to search for violations, aiming to uncover subtle, stateful bugs early. HN discussion praises the lightweight single binary and novel LTL-on-DOM design, but questions practical effectiveness, missing features (shrinking, repros), and lack of real-world examples vs existing UI test frameworks.

---

### Comment pulse
- Property-based UI testing is promising but Bombadil is early-stage → random action generators exist, yet shrinking, reliable repros, and richer real-world examples are still missing.  
- Minimal, single-executable tooling is a selling point → avoids npm dependency bloat; Rust binary running locally/CI feels like esbuild-style focused tooling.  
- Random PBT seems weak for rare edge cases → skeptics prefer Pex/Z3-style symbolic execution — counterpoint: practitioners report many real bugs, including in dependent libraries.  

---

### LLM perspective
- View: Pairing Bombadil with LLM-generated properties and actions could make property-based UI testing accessible to teams without formal-methods expertise.  
- Impact: If it matures, teams might shift some brittle scripted E2E tests into more robust, spec-driven fuzzing-style suites.  
- Watch next: Benchmarks versus Cypress/Playwright, shrinker quality on real apps, and how well Antithesis integration stabilizes flaky repros.
