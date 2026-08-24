# LLMs could be, but shouldn't be compilers

- Score: 108 | [HN](https://news.ycombinator.com/item?id=46912781) | Link: https://alperenkeles.com/posts/llms-could-be-but-shouldnt-be-compilers/

### TL;DR

Alperen Keles argues that even a hallucination-free LLM should not be treated like a traditional compiler. Higher-level languages relinquish control through defined semantics and testable guarantees; natural-language prompts are functionally underspecified, leaving models to choose data models, edge cases, errors, security, and performance. Easy generation can turn developers into consumers who discover hidden commitments late, so specification and verification become the core skills. Commenters debated determinism versus semantic closure, human-style oversight versus software metrics, and whether generated source remains acceptable when tested or defeats abstraction by requiring lower-level inspection.

### Comment pulse

- Determinism is not decisive → commenters argued compilers need semantically bounded outputs and decidable errors, while LLM prompts remain open-ended.
- Testing generated code divides readers → static artifacts can be validated — counterpoint: inspecting lower-level source means the natural-language abstraction failed.
- Intermediate representations may help → description-to-specification-to-plan-to-implementation pipelines expose choices before generation and narrow the target behavior.

### LLM perspective

- View: An LLM resembles program synthesis from incomplete requirements more than compilation from a language with defined semantics.
- Impact: Implementation becomes cheaper, but specification, verification, and maintaining developer understanding become the limiting work.
- Watch next: Formal contracts, robust tests, traceable design decisions, intermediate specifications, error metrics, reproducibility, and long-term code comprehension.
