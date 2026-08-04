# OpenAI reduces Codex Model Context Size from 372k to 272k

- Score: 293 | [HN](https://news.ycombinator.com/item?id=48965850) | Link: https://github.com/openai/codex/pull/33972/files

### TL;DR

A Codex metadata backport appears to reduce the model’s advertised context window from 372k to 272k tokens; the supplied GitHub page exposes the PR title but not its diff or rationale. HN users said the smaller ceiling compounds an auto-compaction system that cannot be disabled or rolled back, often discarding crucial detail in large codebases, research, and reverse engineering. Others argued that long contexts degrade attention and cost, favoring modular plans, persistent Markdown memory, fresh sessions, and smaller task slices over continually expanding the prompt.

### Comment pulse

- Compaction can erase working state → users reported forgotten constraints, rereads, hallucinations, and repeated threshold loops.
- External memory works for structured projects → versioned plans and feature-specific Markdown enable clean restarts — counterpoint: dense papers and reverse engineering resist lossy summaries.
- Bigger is not always better → some users see quality decay above 100–300k, while others need 1M for multi-agent planning and review.

### LLM perspective

- **View:** Context capacity and context quality are separate resources; mandatory compaction trades exact recall for continuity without user control.
- **Impact:** Researchers and large-codebase teams lose effective working memory; disciplined artifact-based workflows become more important.
- **Watch next:** Publish the rationale, effective usable window, compaction trigger, rollback controls, quality benchmarks, and token-efficiency comparisons.
