# How to effectively write quality code with AI

- Score: 132 | [HN](https://news.ycombinator.com/item?id=46916586) | Link: https://heidenstedt.org/posts/2026/how-to-effectively-write-quality-code-with-ai/

### TL;DR
The article proposes a workflow for AI-assisted coding that keeps humans firmly in charge: define architecture and constraints up front, maintain detailed in-repo documentation, build good logging/debug tooling, and clearly label AI-written and high-risk code for later human review. It emphasizes property-based tests that AIs cannot edit, strict linting/formatting, context-specific prompts, minimizing code complexity, and breaking work into small, verifiable chunks. HN discussants debate whether this reintroduces “waterfall,” how much thinking should move from coding to spec-writing, and how much context AIs should really see.

---

### Comment pulse
- Coding as thinking → Some developers learn by writing/running code; heavy specs + AI risk disengaging them from the problem — counterpoint: others now treat specs/tests as the main creative work.
- Speed vs rigor → Critics say these safeguards erase AI’s speed advantage and resemble waterfall; supporters use AI for small, iterative, easily-reviewed changes to stay agile.
- Old practices, new incentives → Docs, small diffs, marking risky code are not new, but AI finally consumes this metadata, making the payoff visible and worth the discipline.

---

### LLM perspective
- View: Treat AI as a junior pair-programmer plus superscalar refactoring engine, not an autonomous coder.
- Impact: Teams with strong architecture, testing, and repo hygiene will benefit disproportionately from AI tools.
- Watch next: Tooling that auto-labels AI edits, tracks review state, and enforces “AI can’t touch these tests” boundaries.
