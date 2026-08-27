# Your job is to deliver code you have proven to work

- Score: 596 | [HN](https://news.ycombinator.com/item?id=46313297) | Link: https://simonwillison.net/2025/Dec/18/code-proven-to-work/

### TL;DR

Simon Willison argues that contributors must demonstrate changes before asking others to review them, especially when coding agents can generate large patches cheaply. His standard combines manual testing of realistic and edge cases with automated tests that fail when the implementation is reverted. Evidence may include reproducible commands, output, screenshots, or recordings. Agents should run and inspect their work, but the human contributor remains accountable. Commenters largely agreed while noting tests demonstrate selected cases rather than logically proving correctness under every relevant condition.

### Comment pulse

- Commenters said untested, AI-generated work comes from experienced developers and non-engineers too, not only juniors.
- Good PRs explain context, tradeoffs, test steps, and evidence, though several noted reviewers often ignore long descriptions.
- Others emphasized self-review, reasoning about untested states, and organizational incentives that reward speed over engineering quality.

### LLM perspective

- View: Cheap code generation raises the value of verification, judgment, and concise evidence rather than reducing reviewer obligations.
- Impact: Requiring demonstrations shifts quality work back to authors and preserves scarce review attention.
- Watch next: Teams should define evidence standards that cover behavior, regressions, edge cases, and human understanding without ritualistic paperwork.
