# Ollama Web Search

- Score: 156 | [HN](https://news.ycombinator.com/item?id=45377641) | Link: https://ollama.com/blog/web-search

- TL;DR
    - Ollama launched a web search and fetch API with a free tier, Python/JS/REST tooling, MCP integrations, and examples for building agentic workflows. Results return titles, URLs, and page text; long contexts (~32k) are recommended. HN asks who powers search and what rights users have over results; Ollama says zero data retention and users “own” results, but readers want formal policies. Debate continues over Ollama’s local-first identity vs selling cloud access to very large models; some report good early results (e.g., YouTube), mixed on X.

- Comment pulse
    - Unclear provider and result licensing → legal/privacy uncertainty; CCPA cited; Exa suspected. Ollama: zero retention, results yours—counterpoint: vague policies and “training” loopholes worry users.
    - Local-first vs cloud pivot → perceived dissonance. Supporters: cloud enables 120B–671B models and monetization; evaluate before local download.
    - DIY works (DDG/Google + prompt stuffing) → fast wins but rate limits and GPU pain; early tests: strong on YouTube, inconsistent on X.

- LLM perspective
    - View: A standardized search/fetch tool reduces custom scraping, improving agent reliability and recency.
    - Impact: Local stacks gain “browse” parity; cloud models become practical for research workflows without bespoke pipelines.
    - Watch next: Provider disclosure, ToS on caching/republishing, rate limits/pricing, snippet quality, platform coverage, and agent eval benchmarks.
