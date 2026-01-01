# LLVM AI tool policy: human in the loop

- Score: 211 | [HN](https://news.ycombinator.com/item?id=46440833) | Link: https://discourse.llvm.org/t/rfc-llvm-ai-tool-policy-human-in-the-loop/89159

### TL;DR
LLVM is proposing an AI tool policy that allows any tooling but requires a “human in the loop”: contributors must fully review AI-generated code, understand it well enough to answer review questions, and clearly label substantial AI assistance. The policy targets “extractive” contributions where LLM users dump unvetted output on maintainers, wasting scarce review time. It bans autonomous agents posting code or reviews without human approval, defines a standard rejection template, and aligns with similar policies emerging in other large open source projects.

---

### Comment pulse
- Responsibility remains personal → Reviewers expect whoever’s name is on the PR to fully own and understand the code—counterpoint: that doesn’t actually reduce wasted reviewer time.
- Maintainer burden is the core problem → AI has exploded low-effort submissions, but reviewer capacity is flat, so explicit anti‑slop rules are needed to avoid “death by a thousand cuts.”
- Policy seen as reasonable guardrail → Most discussion favors “human in the loop” as pragmatic; hostility is toward AI‑proxy contributors, not serious new programmers willing to learn.

---

### LLM perspective
- View: This codifies a social contract: AI may assist, but cannot replace contributor understanding or accountability.
- Impact: Raises the bar for AI-assisted drive‑by PRs; favors regular contributors and serious newcomers over anonymous AI proxies.
- Watch next: Whether other infra projects adopt similar “extractive” labels and whether tooling emerges to pre‑screen AI slop before review.
