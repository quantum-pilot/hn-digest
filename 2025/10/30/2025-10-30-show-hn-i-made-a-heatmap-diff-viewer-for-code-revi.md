# Show HN: I made a heatmap diff viewer for code reviews

- Score: 160 | [HN](https://news.ycombinator.com/item?id=45760321) | Link: https://0github.com

### TL;DR

The supplied product description presents a code-review viewer that colors diff lines and tokens by estimated attention value, highlighting secrets, unusual cryptography, or complex logic rather than issuing only bug verdicts. Public pull requests can be opened by replacing GitHub’s domain; the service description says it clones repositories and asks GPT-5-Codex for structured heatmap data. HN commenters question GitHub permissions, model cost, and missing project context, while requesting clearer labels, configurable gradients, pre-PR review, and learning from prior reviewer behavior.

### Comment pulse

- Attention ranking could tame large PRs → reviewers already triage points of interest, especially in AI-generated changes.
- Diff-only context is incomplete → important defects often involve unchanged files or missing parallel edits elsewhere.
- Trust needs clearer boundaries → commenters challenge sign-in permissions and want public repositories usable without authorization.

### LLM perspective

- View: A heatmap is useful as navigation, but its visual confidence can overstate an uncertain model judgment.
- Impact: Reviewers may scan faster, provided low-ranked code remains reviewable and permission scope stays minimal.
- Watch next: Measure missed defects, review time, calibration, repository-context gains, cost, and authorization behavior.
