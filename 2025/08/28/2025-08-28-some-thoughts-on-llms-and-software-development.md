# Some thoughts on LLMs and software development

- Score: 420 | [HN](https://news.ycombinator.com/item?id=45055641) | Link: https://martinfowler.com/articles/202508-ai-thoughts.html

- TL;DR
  - Fowler argues LLM impact hinges on workflow: beyond autocomplete, tools that read/edit code matter, yet surveys ignore this. He declines predictions, calls AI a bubble that will pop but leave survivors. Treat outputs as non‑deterministic “hallucinations”: query multiple times, don’t offload deterministic math, and mind security (Willison’s lethal trifecta; agentic browsers unsafe). HN debates the term, reports 90%-right code harming quality and review, and converges on LLMs as accelerants/assistants—not replacements.

- Comment pulse
  - Semantics debate: “hallucination” vs “bullshit”; some say Fowler’s irony clarifies probabilistic outputs, others call it equivocation — counterpoint: framing sets user expectations.
  - Productivity vs quality: LLMs flood 90%-correct boilerplate; reviews suffer; owners must be accountable; augmentation useful, replacement unlikely.
  - Verification heuristics: ask thrice like TMR; works for people too, but can induce contradictions; rigorous tests remain essential.

- LLM perspective
  - View: Treat LLMs as stochastic collaborators; gate with deterministic tooling: compilers, linters, tests, types, review.
  - Impact: Processes shift to smaller PRs, AI-aware reviews, stronger ownership, and explicit security threat modeling for agent features.
  - Watch next: Compare autocomplete vs code-editing agents; invest in reproducibility/traceability; explore sandboxed browsers with strict capability isolation.
