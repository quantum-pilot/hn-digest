# Thoughts and feelings around Claude Design

- Score: 201 | [HN](https://news.ycombinator.com/item?id=47818700) | Link: https://samhenri.gold/blog/20260418-claude-design/

### TL;DR

The author predicts design tooling will split as code becomes the product’s source of truth. Figma’s proprietary primitives, nested variables, modes, and component variants created a manual parallel representation that agents scarcely learned because training data favored code. Claude Design instead produces HTML and JavaScript and could merge design and implementation into one loop with Claude Code. A second category may remain code-free and maximize visual exploration. Commenters see real potential but report restrictive weekly usage, stylistic homogenization, roughness, and skepticism that code removes complexity inherent in large products.

### Comment pulse

- Early users produced deployable concepts quickly but exhausted preview quotas after one or two serious design-system sessions.
- Similar outputs across unrelated prompts suggest agentic design may converge toward recognizable defaults.
- Code collapses handoff friction — counterpoint: mature products still need many modes, exceptions, responsive states, and creative visual manipulation.

### LLM perspective

- The strongest near-term workflow is bidirectional iteration between repository context and visual exploration.
- Open, parseable design formats may gain leverage by exposing intent to both humans and agents.
- Watch export fidelity, quota economics, accessibility, responsive behavior, and round-trip edits after code changes.
