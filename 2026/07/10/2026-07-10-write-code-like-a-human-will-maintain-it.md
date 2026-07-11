# Write code like a human will maintain it

- Score: 322 | [HN](https://news.ycombinator.com/item?id=48859701) | Link: https://unstack.io/write-code-like-a-human-will-maintain-it

### TL;DR
- Theme: even in an AI-heavy workflow, you should write and shape code as if a human teammate will maintain it, not an agent.
- Commenters report LLMs happily churn out code but often ignore project conventions, abstractions, and even explicit instructions, leading to duplication and brittle patterns over time.
- Some build elaborate `/review` commands and multi-role AI code reviews; others find extra prompts and checklists degrade results and prefer LLMs only for exploration and review, writing production code themselves.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Build AI review workflows → custom `/review` checklists and multi-role reviews catch many issues and evolve over time — counterpoint: long, generic lists worsen instruction-following and hide failures.  
- Prefer human-authored core code → use LLMs for exploration/debug/review; agents on mature codebases erode mental models and structure, making maintenance harder.  
- LLMs resist abstractions → they re-implement basics instead of reusing APIs, so people add “final tidy/professional check” prompts to push toward separation-of-concerns and cleanup.

---

### LLM perspective
- View: Treat models as fast but forgetful juniors: let them draft, but humans own architecture, abstractions, and final diffs.  
- Impact: Teams should encode standards in tests/linters and review culture, not ever-growing prompt walls and ad hoc checklists.  
- Watch next: Better constraint-following, repo-aware agents, and scheduled AI code-review/refactor passes will decide if agent-maintained codebases stay humane.
