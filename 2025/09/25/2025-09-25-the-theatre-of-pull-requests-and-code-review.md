# The Theatre of Pull Requests and Code Review

- Score: 208 | [HN](https://news.ycombinator.com/item?id=45371283) | Link: https://meks.quest/blogs/the-theatre-of-pull-requests-and-code-review

### TL;DR

The article argues that oversized pull requests invite superficial approval and shared quality failures. It recommends changes reviewable in 5–10 minutes, roughly 300 lines rather than 500-plus, plus coherent commits that compile, explain intent, and remain useful for bisecting. Fixup commits and autosquash can preserve that narrative while development stays iterative. Commenters strongly disputed universal thresholds: logical cohesion can matter more than line count, stacked PRs create overhead, and context or design discussion may outperform commit storytelling. Others defended small, readable histories, especially in distributed projects.

### Comment pulse

- Context-first reviewers want authors to self-review, identify expert-relevant lines, explain choices, and ask focused questions rather than request blanket approval.
- Rule skeptics warn arbitrary slicing hides system-level mistakes; supporters say stacked tooling preserves coherence while keeping reviews manageable.

### LLM perspective

- View: Reviewability is a cognitive-budget problem, not a line-count compliance exercise.
- Impact: Teams benefit when authors package intent, risk, and test evidence around logically separable changes.
- Watch next: Compare escaped defects, review latency, and rework across whole-feature, stacked, and commit-by-commit workflows.
