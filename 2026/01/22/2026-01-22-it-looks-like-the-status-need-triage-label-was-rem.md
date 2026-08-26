# It looks like the status/need-triage label was removed

- Score: 269 | [HN](https://news.ycombinator.com/item?id=46721179) | Link: https://github.com/google-gemini/gemini-cli/issues/16728

### TL;DR

A JetBrains IDE detection request exposed a Gemini CLI automation loop: one GitHub Actions workflow removed status/need-triage under certain conditions, while another restored labels removed by non-maintainers without exempting bots. The pair repeatedly toggled the label and emitted thousands of bot messages; the page showed 4,616 remaining activity items before mass comment deletions on January 22. HN compared it with reply-all and helpdesk loops, questioned inference costs, and emphasized that agents must recognize their own identities across API representations.

### Comment pulse

- Root cause → two independently reasonable workflows formed feedback because the enforcement rule treated sibling automation as an outsider.
- Operational cost → readers estimated notification and inference waste across thousands of events; the repository pays through its configured API key.
- AI relevance → some saw an agent-awareness failure; others argued ordinary event-rule testing could have caught the same bug.

### LLM perspective

- View: Event-driven agents need explicit actor normalization, loop guards, and bounded action budgets before they can mutate shared state.
- Impact: Maintainers and subscribers absorb notification floods, cleanup work, and inference charges from one missing exclusion.
- Watch next: Add bot allowlists, idempotency tests, rate limits, and alerts for repeated inverse actions.
