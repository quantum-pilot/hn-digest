# How to Code Claude Code in 200 Lines of Code

- Score: 240 | [HN](https://news.ycombinator.com/item?id=46545620) | Link: https://www.mihaileric.com/The-Emperor-Has-No-Clothes/

### TL;DR
Article walks through building a minimal “Claude Code–style” coding agent in ~200 lines of Python: an interactive chat loop around an LLM plus three tools (read file, list files, edit/replace). The LLM is prompted with tool descriptions and emits tool calls as specially formatted text; your code parses, runs them, and returns results. HN likes the demystification but emphasizes that real tools layer on planning/TODO mechanisms, durable context and history, robust code-editing primitives, queues, subagents, and richer prompts.

---

### Comment pulse
- Planning/TODO lists are crucial → dynamic task lists, reinserted into context, dramatically improve performance on complex tasks and prevent agents from “giving up” early.  
- Production agents are far from 200 LOC → transcripts reveal UUID threading, queues, subagents, file-history snapshots; editing reliability and context management dominate real-world complexity.  
- Minimal loop explains the “magic” → LLMs just follow tool descriptions, but early stopping and long tasks need explicit TODO/working-memory tools—counterpoint: toy agents remain great for learning.

---

### LLM perspective
- View: Treat the 200-line agent as a didactic skeleton; real value comes from progressively adding planning, memory, and safety layers.  
- Impact: Lowers the barrier for engineers to prototype custom devtools, but risks underestimating production reliability and evaluation work.  
- Watch next: Compare planning strategies (TODO tools vs. summaries), standardize code-edit tool schemas, and share open traces of industrial agent workflows.
