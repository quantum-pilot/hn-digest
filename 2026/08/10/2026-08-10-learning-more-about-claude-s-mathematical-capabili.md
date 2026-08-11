# Learning more about Claude's mathematical capabilities

- Score: 155 | [HN](https://news.ycombinator.com/item?id=49247070) | Link: https://www.anthropic.com/research/riemann-zeta

### TL;DR

An unreleased Claude model found a claimed improvement to a long-standing result related to the Riemann hypothesis: raising the lower bound for zeros on the critical line from 41.6% to 67.2%, without proving the hypothesis itself. Across two Claude Code sessions it produced 31 million output tokens, tested 650 failed ideas, then coordinated about 60 subagents for a day and a half. Anthropic mathematicians checked the paper, outside experts examined it, and Claude produced a Lean-verifiable proof. HN marveled at encouragement-only prompting while questioning whether brute-force compute constitutes scientific insight.

### Comment pulse

- The method combines Bombieri with recent unconditional results; its novelty is treating positive- and negative-definite subspaces together in one quadratic form.
- Encouragement appeared to overcome model skepticism — counterpoint: commenters questioned whether persistence and massive search equal a new theoretical breakthrough.
- Practitioner anecdotes suggest released Claude versions already assist niche mathematics, provided humans independently verify claims and document methods.

### LLM perspective

- **View:** The notable capability is autonomous research orchestration: generating, falsifying, reviewing, formalizing, and checking literature at scale.
- **Impact:** Mathematicians gain a high-throughput conjecture partner, but validation costs and compute access shape who benefits.
- **Watch next:** Public paper scrutiny, Lean artifact review, independent reproduction, token cost, model release, and broader applicability.
