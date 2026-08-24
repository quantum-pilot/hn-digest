# Writing a good Claude.md

- Score: 251 | [HN](https://news.ycombinator.com/item?id=46098838) | Link: https://www.humanlayer.dev/blog/writing-a-good-claude-md

### TL;DR

A project instruction file should briefly orient a coding agent to what the repository contains, why it exists, and how work is verified. Because that file enters every session, broadly applicable guidance deserves priority; extra instructions dilute attention and may be dismissed as irrelevant. The article recommends progressive disclosure through clearly named supporting documents and pointers to authoritative code, deterministic linters instead of prose style rules, and careful manual curation instead of automatic initialization. Commenters debate whether this setup beats ordinary documentation and task-specific context.

### Comment pulse

- Table-of-contents guidance preserves attention → agents load specialized build, storage, or style notes only when a task requires them.
- Deterministic tools should enforce formatting → hooks and autofixers are faster and more reliable than persistent prose instructions.
- Setup value depends on workflow → autonomous feature work benefits from durable context — counterpoint: surgical edits may need only selected code and conversation.

### LLM perspective

- View: Instruction files are routing layers, not encyclopedias; value comes from steering attention toward authoritative evidence when needed.
- Impact: Smaller defaults leave more context for task evidence and reduce the chance that unrelated rules dilute critical instructions.
- Watch next: Teams should measure instruction adherence and task quality before expanding files or trusting automatic initialization.
