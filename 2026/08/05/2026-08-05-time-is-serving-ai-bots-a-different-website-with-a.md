# TIME Is Serving AI Bots a Different Website, with Ads Built In

- Score: 256 | [HN](https://news.ycombinator.com/item?id=49182041) | Link: https://www.vincentschmalbach.com/time-serves-ai-bots-a-different-website/

### TL;DR

Testing one TIME article under different User-Agent strings, the author found that browsers and Googlebot received a roughly 303 KB HTML page, while selected assistant crawlers received a 13 KB Markdown version and some OpenAI agents were blocked. The bot-only pages carried Mobian impression and token headers plus sponsored FAQ material absent from human pages. Fresh identifiers and no-store caching suggest each request is counted separately. The result is a machine-only advertising layer whose content is labeled sponsored but invisible to human readers and potentially injected into assistants’ working context.

### Comment pulse

- Many saw an emerging AI-targeted SEO market that may influence answers by placing promotional claims directly in retrieved context.
- Readers wanted the clean Markdown themselves, recalling lightweight WAP, text-only sites, RSS, and reader modes.
- Some questioned efficacy — counterpoint: even weak influence may pay at scale, especially in long, mixed-topic sessions.

### LLM perspective

- View: Serving materially different machine content creates a new provenance and disclosure problem.
- Impact: Assistants may relay ads as knowledge while users cannot inspect the version their agent consumed.
- Watch next: Agent-side ad filtering, crawler policies, publisher metrics, and transparency requirements.
