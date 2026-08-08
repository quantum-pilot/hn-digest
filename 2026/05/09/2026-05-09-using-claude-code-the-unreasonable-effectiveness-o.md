# Using Claude Code: The unreasonable effectiveness of HTML

- Score: 405 | [HN](https://news.ycombinator.com/item?id=48071940) | Link: https://twitter.com/trq212/status/2052809885763747935

### TL;DR

Thariq argues Claude Code’s outputs have outgrown Markdown: self-contained HTML can combine tables, CSS, SVG, code, diagrams, interaction, responsive navigation, and export controls, making long plans and reports likelier to be read and shared. He uses it for design comparisons, annotated PR reviews, explainers, prototypes, and one-off editors that return selections as prompts or structured data. Generation takes two to four times longer and diffs are noisy. HN liked disposable single-file tools but warned that HTML raises token and execution costs while making precise human co-authoring harder.

### Comment pulse

- Markdown remains superior as editable source → render it through a template when richer presentation is needed.
- Single-file HTML excels for throwaway calculators, dashboards, and visual experiments → deployment can be as simple as sharing one artifact.
- Directly rendered HTML expands the attack surface → counterpoint: constrained local artifacts trade safety and tokens for interaction and information density.

### LLM perspective

- **View:** Separate semantic source from generated presentation when an artifact must outlive the session.
- **Impact:** Reviewers gain navigable explanations; authors may surrender control if every correction becomes a reprompt.
- **Watch next:** Round-trip editing, content-security defaults, accessible templates, stable IDs, and source-to-render diff tooling.
