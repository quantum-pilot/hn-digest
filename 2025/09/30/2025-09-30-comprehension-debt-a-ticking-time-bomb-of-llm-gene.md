# Comprehension debt: A ticking time bomb of LLM-generated code

- Score: 474 | [HN](https://news.ycombinator.com/item?id=45423917) | Link: https://codemanship.wordpress.com/2025/09/30/comprehension-debt-the-ticking-time-bomb-of-llm-generated-code/

- TL;DR
  - LLM-generated code accelerates output but accumulates “comprehension debt”: future changes stall because nobody understands what or why. Teams that review/rework erase speed gains; teams that don’t bank unread, undertested code, then hit “doom loops” where models can’t fix issues and humans must decipher it. HN ties this to Naur’s “theory building” and Lamport’s “programming ≠ coding”: LLMs shortcut the learning developers used to gain while typing. Commenters propose countermeasures—drive design first, use prototypes deliberately, and constrain generation via tests, standards, types, and better context.

- Comment pulse
  - Programming is theory-building; LLMs skip incidental modeling, creating opaque code. — counterpoint: LLMs can help reconstruct theory for successors if fed context.
  - Code review can't match LLM output; you either bottleneck or rubber-stamp. Use tests as primitives; block merges until old+new tests pass.
  - LLMs often overcomplicate; simplify at creation and iterate prompts. Strong types/formal specs constrain outputs and shrink error surface.

- LLM perspective
  - View: Treat LLMs as typists under human architecture; capture ‘why’ via ADRs, specs, and tests before code generation.
  - Impact: Quality leaders shift effort to intent-capture, test infra, and refactoring; junior dev roles tilt toward system reading and test-first workflows.
  - Watch next: Metrics: rework/MTTR on AI code, test coverage growth, prompt/context patterns; tools that compile natural-language requirements into checkable specifications.
