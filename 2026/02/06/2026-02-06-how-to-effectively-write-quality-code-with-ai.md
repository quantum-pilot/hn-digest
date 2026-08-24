# How to effectively write quality code with AI

- Score: 132 | [HN](https://news.ycombinator.com/item?id=46916586) | Link: https://heidenstedt.org/posts/2026/how-to-effectively-write-quality-code-with-ai/

### TL;DR

Mia Heidenstedt proposes a control-heavy workflow for AI-assisted coding: humans decide architecture, interfaces, data structures, and tests; maintain repository documentation and path-specific prompts; expose concise debug signals; mark AI-written and high-risk functions by review status; protect human-authored property tests; generate independent interface tests; enforce linting; reduce complexity; prototype alternatives; and split work into verifiable increments. Commenters liked explicit risk marking and small tasks but disputed documentation-first rigor. Critics said coding creates understanding or long context worsens results; supporters described rapid specification-review loops with humans retaining comprehension.

### Comment pulse

- Coding is a thinking tool → critics lose discovery when agents implement plans before developers encounter constraints directly.
- Detailed specs preserve intent → supporters iterate rapidly around cheap prototypes — counterpoint: critics see waterfall overhead and lost discovery.
- AI revives familiar disciplines → documentation, linting, tests, and small changes predate agents, but models consume those artifacts directly.

### LLM perspective

- View: The workflow moves quality’s bottleneck from typing code to precise intent, observability, independent tests, and human comprehension.
- Impact: Teams gain speed only when verification overhead stays below generation savings and responsibility remains unmistakably human.
- Watch next: Defects by review status, security regressions, specification churn, context cost, test mutation, and developer comprehension over time.
