# Specsmaxxing – On overcoming AI psychosis, and why I write specs in YAML

- Score: 258 | [HN](https://news.ycombinator.com/item?id=47994012) | Link: https://acai.sh/blog/specsmaxxing

### TL;DR

The author argues that durable acceptance criteria, not longer prompts, are the best defense against agents losing requirements across context windows, sessions, and handoffs. His open-source Acai toolkit stores one feature’s behavior and constraints in YAML, assigns stable Acceptance Criteria IDs, and links those IDs to code, tests, implementation states, comments, and a review dashboard. The goal is acceptance coverage and spec-aligned review rather than reading giant diffs. HN recognized familiar requirements-analysis and behavior-driven-development ideas, while debating whether this preserves intent or merely adds another fragile, nondeterministic compilation layer.

### Comment pulse

- Specs preserve rationale that generated code lacks → stable intent helps future agents and humans understand why behavior exists.
- Defining behavior is not equivalent to implementation → translating requirements into robust mechanisms remains difficult, exhausting engineering work.
- The approach resembles analysts, Cucumber, and BDD → counterpoint: linking IDs across artifacts may add useful traceability for generated code.

### LLM perspective

- **View:** Requirement traceability becomes more valuable as code-generation throughput exceeds human diff-review capacity.
- **Impact:** Engineers spend more time specifying, validating, and reconciling intent across products, branches, and implementations.
- **Watch next:** Spec drift, ID maintenance cost, acceptance-coverage accuracy, defect rates, review time, and adoption beyond the author’s workflow.
