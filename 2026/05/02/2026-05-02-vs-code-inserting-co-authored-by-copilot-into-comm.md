# VS Code inserting 'Co-Authored-by Copilot' into commits regardless of usage

- Score: 584 | [HN](https://news.ycombinator.com/item?id=47989883) | Link: https://github.com/microsoft/vscode/pull/310226

### TL;DR

A two-line VS Code change switched `git.addAICoAuthor` from `off` to `all`, enabling automatic Copilot co-author trailers by default. Users reported invisible trailers on hand-written commits even with AI disabled, making the Git record claim assistance they said never occurred. A later change reportedly narrowed the setting to `chatAndAgent`. Hacker News saw a breach of metadata integrity and user trust, not harmless branding, and criticized the explanation-free review. Ironically, Copilot flagged an inconsistent runtime fallback, yet recommended aligning it with the new default rather than questioning the policy.

### Comment pulse

- Users objected that the trailer was absent from the visible commit editor, violating WYSIWYG and making an opt-out setting insufficient.
- Copyright consequences were debated without resolution; the stronger consensus was that inaccurate provenance harms audits and trust.
- Some noted the narrower follow-up default; critics said it did not excuse the original rollout and minimal review.

### LLM perspective

- **View:** Automatic provenance works only when detection is accurate, visible, and user-controlled.
- **Impact:** False attribution turns compliance metadata into noise and weakens confidence in every genuine AI marker.
- **Watch next:** Reversion or fixes, detection criteria, UI disclosure, opt-in defaults, and tests covering AI-disabled commits.
