# Hashcards: A plain-text spaced repetition system

- Score: 218 | [HN](https://news.ycombinator.com/item?id=46264492) | Link: https://borretti.me/article/hashcards-plain-text-spaced-repetition

### TL;DR

A local-first study tool stores card content as lightly marked-up Markdown decks while keeping review history in a colocated SQLite database. It serves drills through localhost, schedules with FSRS, identifies cards by text hashes, and lets users edit with any editor or apply Git, Unix tools, and generation scripts. The creator aims to combine Anki’s scheduling with Mochi’s low-friction authoring, using compact question-answer and cloze syntax. HN liked plain-text ownership but challenged the Anki critique and asked whether correcting card text destroys its accumulated history.

### Comment pulse

- One reader applies scheduled prompts to relationship habits and Kindle highlights, treating repetition as lifelong behavioral reinforcement rather than academic memorization.
- Anki defenders called its hierarchy, WYSIWYG default, HTML editing, and plugins practical — counterpoint: supporters said the author only needed personally motivating tradeoffs.
- Markdown users valued portability, editor freedom, cross-linking, Git, and extensibility; Emacs users pointed to org-drill as an existing plain-text option.

### LLM perspective

- View: Separating readable card content from scheduler state preserves ownership without rejecting a database where state is useful.
- Impact: Power users gain scriptable decks; edits, synchronization, and card identity become their operational responsibility.
- Watch next: Typo-safe identity, import compatibility, mobile workflows, conflict handling, FSRS tuning, and long-term history portability.
