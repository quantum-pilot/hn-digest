# Scaling LLMs to Larger Codebases

- Score: 191 | [HN](https://news.ycombinator.com/item?id=46354970) | Link: https://blog.kierangill.xyz/oversight-and-guidance

### TL;DR

The author argues that scaling coding agents requires investment in guidance and oversight, not simply larger context windows. Teams should iteratively build lean prompt libraries, maps, conventions, and modular APIs so models infer routine choices without rediscovering the repository. Technical debt and inconsistent architecture impede both humans and agents. Human reviewers must still understand product and design consequences, while types, tests, linters, and architectural checks can encode recurring feedback. HN users endorsed research-plan-execute-review loops and context partitioning, but reported inconsistent instruction-following and sharply different outcomes across domains.

### Comment pulse

- Context engineering → documenting each observed agent snag compounds returns, though large instruction files may be ignored or consume scarce context.
- Workflow → separate research, planning, execution, and fresh-context review improve complex changes — counterpoint: newer agents sometimes handle this internally.
- Architecture → small, explicit module boundaries aid navigation, reuse, testing, and parallel agent work more than indiscriminate repository ingestion.

### LLM perspective

- View: Agent readiness largely overlaps maintainability: clear boundaries and executable constraints benefit every contributor.
- Impact: Senior engineers shift toward designing context, reviewing choices, and strengthening feedback systems rather than merely accepting generated code.
- Watch next: Measure one-shot success, review time, defect rates, prompt drift, ignored instructions, and context-partitioning costs.
