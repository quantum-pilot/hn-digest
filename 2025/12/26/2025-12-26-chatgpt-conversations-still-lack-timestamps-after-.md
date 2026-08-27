# ChatGPT conversations still lack timestamps after years of requests

- Score: 237 | [HN](https://news.ycombinator.com/item?id=46391472) | Link: https://community.openai.com/t/timestamps-for-chats-in-chatgpt/440107?page=3

### TL;DR

ChatGPT users have requested visible conversation and message timestamps since 2023, arguing that long-running chats used as journals, coaching logs, or project records lose essential chronology. The underlying exports already contain timestamps, enabling scripts and third-party search tools, but the normal interface omits them. HN proposed reasons ranging from cleaner UX to avoiding temporal context that might confuse models, yet considered those separable engineering concerns. Suggested workarounds include modifying exported HTML or prompting ChatGPT to print times, though generated timestamps may be inaccurate.

### Comment pulse

- Exports prove chronology exists → users can expose dates or build private, searchable archives without waiting for interface changes.
- Display and model context are separable → frontend timestamps need not consume prompts or imply model awareness.
- Prompt-generated timestamps are unreliable → reported times can drift or reflect an earlier session rather than each message.

### LLM perspective

- View: Chronology is core data for persistent assistants, not decorative metadata suitable for indefinite omission.
- Impact: Researchers, journalers, and long-running project users currently bear needless export and indexing work.
- Watch next: Native per-message dates, optional model access to time, and accurate cross-branch chronology would resolve the ambiguity.
