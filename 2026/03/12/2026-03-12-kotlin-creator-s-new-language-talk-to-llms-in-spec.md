# Kotlin creator's new language: talk to LLMs in specs, not English

- Score: 267 | [HN](https://news.ycombinator.com/item?id=47350931) | Link: https://codespeak.dev/

## TL;DR
CodeSpeak is a “spec-first” workflow where you maintain plain‑text specs and let an LLM generate and regenerate the actual code, treating code as a disposable artifact. Case studies on real OSS projects (yt-dlp, Faker, BeautifulSoup, MarkItDown) show roughly 6–10× fewer lines than the original code while still passing (and often adding) tests. HN is split between seeing this as a natural evolution of prompt engineering and worrying about underspecified text, nondeterminism, and lack of formal guarantees.

---

## Comment pulse
- Specs-as-programs is an old “always fails” idea → LLMs now handle underspecified prompts, so systematically structuring prompts/specs may finally be useful — counterpoint: a complete spec is still as hard as code.
- Tool is more workflow than language → markdown specs drive LLM edits; pros: saved prompts, coherent design; cons: spec–code drift, limited agent configurability, unclear business moat vs simple OSS clones.
- Skeptics: stochastic models, evolving architectures and lossy natural-language specs make long-term regenerations risky → some want pipeline: text → formal spec → verifiable code, or at least spec-generated tests.

---

## LLM perspective
- View: Treat human-written specs, not code, as the primary artifact; code is recompiled “AI assembly” that can be thrown away and regenerated.
- Impact: Most compelling for large, test-rich codebases with repetitive glue logic; less so for tightly tuned algorithms or performance-critical kernels.
- Watch next: Robust spec–code sync, integration with formal methods or property tests, and whether an open ecosystem outpaces any closed commercial implementation.
