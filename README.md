
## Simple Hackernews Digest

`llm-summary.py` runs as a cron job on a daily basis, collecting previous (or user-provided) day's top 20 stories with top 5 comments (and top 5 replies to those comments), submits it to GPT-5 (with reasoning) for batch processing (see `SYSTEM_PROMPT.md` in repo root), fetches it whenever the job is done and updates the repository with the entry.

Raw files are stored as `.txt` (so that they can be regenerated with a different prompt if needed).

It currently uses simple HTTP fetch for content extraction (with Tavily API as fallback), but sometimes there simply won't be any content and the LLM will only address the comments directly.
