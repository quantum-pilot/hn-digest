# ChatGPT conversations still lack timestamps after years of requests

- Score: 237 | [HN](https://news.ycombinator.com/item?id=46391472) | Link: https://community.openai.com/t/timestamps-for-chats-in-chatgpt/440107?page=3

- TL;DR
    - Users have been asking since early 2023 for simple per-message timestamps in ChatGPT, to reconstruct long projects, correlate bugs, and meet compliance or journaling needs. OpenAI clearly stores timestamps (visible in the DOM and data exports), but the interface still hides them, forcing people into hacks, scripts, and Chrome extensions. Hacker News discussion speculates about motives—avoiding LLM time-bias, UI clutter, legal risk, or revealing session length—and laments OpenAI’s focus on new features over obvious usability fixes.

- Comment pulse
    - OpenAI stores timestamps but hides them → evidence in DOM and data exports; users script/browser-extensions to surface them, plus build offline searchable archives.
    - Missing timestamps seen as UX/product choice → theories: avoid LLM time-bias, UI clutter, legal risk— counterpoint: optional UI-only display or tools would avoid these.
    - Omission erodes trust and utility → breaks journaling, debugging, workouts tracking, compliance; users feel ignored as basic requests languish while flashy new features ship.

- LLM perspective
    - View: Lack of timestamps is a rare case where trivial-feeling UI change intersects with safety, liability, and engagement incentives.
    - Impact: Power users, enterprises, and regulators will increasingly demand auditable histories; competing clients with richer logs may gain stickier usage.
    - Watch next: Browser extensions, third-party wrappers, and API-side logging standards; any official setting to expose timestamps without altering prompt context.
