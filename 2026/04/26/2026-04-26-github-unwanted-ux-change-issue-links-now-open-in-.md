# GitHub unwanted UX change: issue links now open in a popup

- Score: 223 | [HN](https://news.ycombinator.com/item?id=47910546) | Link: https://github.com/orgs/community/discussions/192666

### TL;DR

GitHub tested opening linked issues in an overlay instead of navigating to their pages, aiming to speed slow cross-repository loads, keep readers’ place, and unify its issue viewer across surfaces. Users reported broken expectations, assistive-technology problems, wasted screen space, and difficulty copying the destination URL for AI-agent workflows; most wanted normal links or an opt-out. GitHub acknowledged missing the mark and rolled the experiment back while continuing work on the underlying performance problem. HN welcomed the reversal but questioned why a UX workaround shipped before the root latency was fixed.

### Comment pulse

- Commenters proposed an opt-in preview cohort so GitHub could collect metrics and feedback without changing everyone’s navigation.
- Comparisons to Jira, GitLab, and Azure DevOps reflected frustration with enterprise tools converging on modal-heavy interfaces.
- Some blamed designer incentives — counterpoint: others emphasized coordination complexity as products and teams accumulate competing goals.

### LLM perspective

- Link semantics are infrastructure: preserve addressability, modifier-key behavior, history, accessibility, and predictable focus before optimizing speed.
- Measure task completion and error rates, not only load time, during interface experiments.
- Fix cross-repository header latency, then retest previews as explicit hover or user-configurable behavior.
