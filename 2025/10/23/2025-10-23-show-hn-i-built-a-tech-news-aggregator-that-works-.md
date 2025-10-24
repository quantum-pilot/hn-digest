# Show HN: I built a tech news aggregator that works the way my brain does

- Score: 129 | [HN](https://news.ycombinator.com/item?id=45684689) | Link: https://deadstack.net/recent

- TL;DR
  - A solo dev launched DeadStack, a Techmeme-style tech aggregator that clusters related coverage, tags topics, and shows concise on‑page summaries to speed scanning. Its “editorial” is fully automated with LLMs (o3‑mini). HN liked the snappy in‑place overview and agreed LLMs fit this task, but flagged scanability issues (blue links, spacing, font); the author iterated quickly. Requests included auto‑hide/mark‑as‑read for ignored items and not resurfacing scrolled‑past stories, with self‑hosted examples cited.

- Comment pulse
  - Improve scanability → Blue link color, spacing, and font create a wall-of-text; author switched titles to black and adjusted cues quickly.
  - Hide what I ignored → Users want auto mark-as-read and no resurfacing; feasible with backend state or accounts — counterpoint: client-only struggles without user management.
  - LLMs fit the job → String-manipulation and summarization praised; author uses o3‑mini to automate the entire editorial workflow.

- LLM perspective
  - View: Automated clustering + summarization can deliver timely, skimmable pages; risks include hallucinated details, biased tagging, and weak deduplication.
  - Impact: Reduces manual curation for solo makers; shifts readers to on-page synthesis, lowering bounce and increasing time-to-insight.
  - Watch next: Per-user memory (mark-as-read, muting), explicit citations, accuracy audits, and UI A/B tests to validate scanability and trust.
