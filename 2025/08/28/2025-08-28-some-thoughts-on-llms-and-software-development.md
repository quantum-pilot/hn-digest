# Some thoughts on LLMs and software development

- Score: 420 | [HN](https://news.ycombinator.com/item?id=45055641) | Link: https://martinfowler.com/articles/202508-ai-thoughts.html

- TL;DR
    - Martin Fowler argues most AI dev surveys miss that value depends on workflow: beyond autocomplete, agents that read/edit code behave differently. He won’t predict programming’s future, urging experimentation. He sees an inevitable AI bubble with unknown timing. Treat LLM output as inherently ungrounded; query multiple times (especially for numbers) and avoid using LLMs for deterministic math. Expect more non‑determinism and larger attack surfaces; agentic browsers may be unsafe. HN debates framing of “hallucinations,” code-quality tradeoffs, and augmentation over replacement.

- Comment pulse
    - ‘Hallucinations are the feature’ is equivocation → redefining a bug as output adds nothing — counterpoint: it’s ironic shorthand reminding users no outputs are self-grounded.
    - LLMs accelerate 90%-right code → review burden, boilerplate sprawl, and fragile designs grow; accountability shifts to the driver who must truly understand generated changes.
    - Best use today is augmentation, not replacement → tools like Claude Code boost flow; ask models multiple times for numerics, borrowing triple-modular redundancy.

- LLM perspective
    - View: Evaluate workflows, not models: compare inline autocomplete vs repo-editing agents, and mandate deterministic tools for math and security-sensitive steps.
    - Impact: Teams adopting agents without guardrails will ship faster but accumulate brittle boilerplate, review debt, and security exposure.
    - Watch next: Benchmarks of code-edit agents, secure agent sandboxes/browser isolation, and policies tying AI-generated changes to owner verification and rollback paths.
