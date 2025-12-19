# Your job is to deliver code you have proven to work

- Score: 596 | [HN](https://news.ycombinator.com/item?id=46313297) | Link: https://simonwillison.net/2025/Dec/18/code-proven-to-work/

- TL;DR  
Willison argues that a developer’s job is not to produce code but to ship changes they have personally demonstrated to work. That means first doing manual, scenario-based checks, then bundling each change with automated tests that fail without it—something LLM tools now make easier. Coding agents should also be driven to prove their edits through execution and tests. HN commenters broaden this to PR hygiene, engineering accountability, overreliance on AI, and the limits of testing without real understanding.

- Comment pulse  
  - AI misuse is widespread, not just juniors → seniors and non-engineers paste agent output into PRs/tickets, offloading understanding and debugging — counterpoint: blaming “kids” hides older offenders.  
  - High-quality PRs document intent and validation → concise summaries plus explicit manual/automated test steps and screenshots ease review, enable async work; but reviewers often ignore long descriptions.  
  - Engineering ≠ code generation → real work is requirements, tradeoffs, accountability; tests demonstrate behavior but don’t prove correctness, so reasoning and exploratory testing remain essential.

- LLM perspective  
  - View: Testing discipline becomes more, not less, important as LLMs and agents spew plausible-but-wrong patches at scale.  
  - Impact: Teams that demand evidence-backed PRs will differentiate from “feature factories” shipping brittle, AI-pasted code.  
  - Watch next: Org practices: PR templates requiring proof, CI gating on tests, and policies clarifying human accountability for AI-generated contributions.
