# Claude's memory architecture is the opposite of ChatGPT's

- Score: 181 | [HN](https://news.ycombinator.com/item?id=45214908) | Link: https://www.shloked.com/writing/claude-memory

### TL;DR

The author describes Claude's then-observed memory as explicit retrieval over raw chat history: conversations begin without a preloaded profile, and user prompts trigger keyword or temporal searches. They contrast this with ChatGPT's automatically loaded, summarized personalization, arguing that Claude favors controllable professional workflows while ChatGPT favors frictionless consumer use. Commenters liked retrieval control but questioned search quality, especially for indirect references, and debated whether profiling implies future advertising. Others noted an announced memory change, making the comparison a time-specific product snapshot rather than a settled architecture.

### Comment pulse

- Explicit retrieval reduces unwanted cross-context associations → users value choosing when old chats influence a new task.
- Automatic memory removes friction → others prefer relevant context appearing without remembering a special invocation.
- Raw search may miss abstractions → commenters expect weak recall when queries do not share obvious terms with past conversations.

### LLM perspective

- View: Memory design trades immediate personalization against provenance, control, latency, and retrieval recall.
- Impact: Professional users can isolate contexts more deliberately, while casual users may experience extra prompting and missed associations.
- Watch next: Anthropic's announced changes, indirect-reference retrieval tests, user controls, and long-horizon memory accuracy.
