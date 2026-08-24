# After two years of vibecoding, I'm back to writing by hand

- Score: 604 | [HN](https://news.ycombinator.com/item?id=46765460) | Link: https://atmoio.substack.com/p/after-two-years-of-vibecoding-im

### TL;DR

After two years using coding agents, the author concludes they are impressive on isolated tasks but poor at sustaining a coherent codebase. Detailed specifications did not solve the problem because implementation continually reshapes design; agents instead preserved early decisions and accumulated locally plausible, structurally inconsistent changes. A cover-to-cover review exposed enough cleanup that manual coding looked faster for a product handling sensitive data. Commenters split between similar atrophy and maintenance concerns and reports that iterative supervision, explicit rules, and newer models work well.

### Comment pulse

- Architecture remains the human bottleneck → generated patches can pass local review while violating neighboring patterns and system-wide constraints.
- Agents fit inspectable chores → tedious code is useful when correctness is cheap to verify, unlike critical business logic or generated tests.
- Skill erosion is plausible → outsourcing basic exercises weakens intuition — counterpoint: disciplined iteration can preserve ownership and deliver strong results.

### LLM perspective

- View: Productivity claims should include specification, review, cleanup, and architectural repair, not generation speed alone.
- Impact: Teams handling user data need stricter human design authority and whole-repository review.
- Watch next: Compare supervised agent workflows against manual work on codebase coherence, defects, and total engineering time.
