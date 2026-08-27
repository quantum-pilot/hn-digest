# Mistakes I see engineers making in their code reviews

- Score: 75 | [HN](https://news.ycombinator.com/item?id=45701404) | Link: https://www.seangoedecke.com/good-code-reviews/

### TL;DR

The author argues valuable code review evaluates a change against the whole system, not just its diff. Reviewers should notice missing reuse and architectural inconsistency, consolidate repetitive feedback, and avoid imposing personal implementation taste when multiple approaches work. Review status must be explicit: approve when comments are optional, block when merging would be unacceptable, and expect most ordinary product changes to pass. AI-generated changes deserve stricter gatekeeping because generation is cheap but contextual review remains hard. The recommendations express the author’s taste and depend on codebase risk and review goals.

### Comment pulse

- Readers agree personal taste should not block changes, but mature-codebase consistency can turn apparent taste into maintainability policy.
- Tooling should remove formatting noise so humans can focus on correctness, architecture and omitted work.

### LLM perspective

- View: Review quality comes from prioritization and system context, not comment count or visible strictness.
- Impact: Clear blocking semantics reduce social guesswork while concise feedback keeps critical defects from disappearing among nits.
- Watch next: Teams should measure whether review practices catch incidents without creating bottlenecks or unrelated scope expansion.
