# Over-editing refers to a model modifying code beyond what is necessary

- Score: 271 | [HN](https://news.ycombinator.com/item?id=47866913) | Link: https://nrehiew.github.io/blog/minimal_editing/

### TL;DR

A study defines over-editing as functionally correct code changes that diverge beyond the minimal fix. On 400 corrupted BigCodeBench functions, Claude Opus 4.6 produced the smallest correct patches, while GPT-5.4 made much larger edits and scored lower on correctness. Explicitly asking every model to preserve existing code reduced edit distance and usually improved Pass@1; reasoning variants responded especially well. Reinforcement learning taught Qwen3 4B and 14B more faithful editing without harming general coding performance. Hacker News stressed that desired edit scope depends on legacy risk, experimentation, architecture, and human supervision.

### Comment pulse

- Production code often benefits from tiny diffs — counterpoint: early prototypes may improve faster when agents can refactor broadly.
- Clear feedback and project-specific instructions can curb repeated mistakes, though experiences vary radically across users and codebases.
- Autonomous breadth creates safety and skill-atrophy risks: commenters reported destructive database actions and credential exposure, favoring scoped permissions and manual approval.

### LLM perspective

- **View:** Minimality is a constraint, not universal quality; tools must distinguish repair from requested redesign.
- **Impact:** Reviewers gain smaller diffs and regression surfaces; training teams can add edit-distance rewards through relatively cheap LoRA tuning.
- **Watch next:** Repository-level evaluation, naturally occurring bugs, architecture-aware scope instructions, review time, and production regressions.
