# AI assistants misrepresent news content 45% of the time

- Score: 390 | [HN](https://news.ycombinator.com/item?id=45668990) | Link: https://www.bbc.co.uk/mediacentre/2025/new-ebu-research-ai-assistants-news-content

- TL;DR
  - An EBU/BBC-led study of 3,000+ answers from ChatGPT, Copilot, Gemini, and Perplexity found 45% had significant issues: 31% poor sourcing and 20% major inaccuracies. Gemini fared worst (76%), largely from weak citations. With 7% of online news users—and 15% under-25s—now turning to assistants, the BBC warns of eroding trust; audiences often blame news outlets too. The EBU released a toolkit, urged regulators to enforce integrity laws, and called for continuous monitoring. HN debates methods but shares frequent hallucinations and bad “summaries.”

- Comment pulse
  - Methodology is weak: sourcing dominates errors, model variants unclear, Anthropic omitted; article mixes old/new results—counterpoint: fabricated links/policies show real accuracy failures.
  - User reports: Gemini hallucinated articles, links, and business hours; many assistants give “random condensation” summaries; some claim SOTA models fare better than lightweight/mini ones.
  - Mitigation: verify cited links, prefer assistants with retrieval on, and demand source attributions—counterpoint: some reports show hallucinations even when web search is enabled.

- LLM perspective
  - View: Most failures are ungrounded claims and weak attribution; enforce claim-grounding, link validation, and temporal awareness before summarizing news.
  - Impact: Newsrooms, platforms, and regulators must align: assistants should default to citations, show recency, and degrade gracefully when retrieval is unavailable.
  - Watch next: Track citation validity rate, grounded-claim accuracy, model/version transparency, and cross-lingual results; include Anthropic and enterprise tiers in follow‑ups.
