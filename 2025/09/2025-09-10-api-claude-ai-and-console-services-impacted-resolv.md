# API, Claude.ai, and Console services impacted [resolved]

- Score: 160 | [HN](https://news.ycombinator.com/item?id=45200118) | Link: https://status.anthropic.com/incidents/k6gkm2b8cjk9

TL;DR (70–90 words)
Anthropic experienced a broad outage affecting the API, Claude.ai, and the Console, identified at 16:28 UTC and marked resolved by 17:36 after multiple “fix implemented” updates; no cause disclosed. HN reactions mix jokes about coding without AI with pointed reliability critiques—several report Anthropic as least stable versus OpenAI and Gemini, with some preferring Bedrock/Vertex as hosting backstops. Others note outages correlate with US work hours, while EU mornings run smoother. Takeaway: plan multi-provider failover and expect intermittent instability from fast-moving AI platforms.

Comment pulse
- Reliability concern → Users cite frequent Anthropic errors versus steadier OpenAI/Gemini; enterprises route via Bedrock/Vertex. — counterpoint: all labs have incidents; OpenAI stability improved.
- Time-zone effect → EU users see smoother mornings; performance degrades as US comes online; late-night US worsens, likely shifting global demand.
- Coping strategies → Fall back to docs/Stack Overflow humor; practical advice: maintain alternate LLMs, failover, and budget for outages.

LLM perspective
- View: Cross-provider abstraction and graceful degradation beat single-vendor dependence when incidents strike without RCA or SLAs.
- Impact: Product teams, CI, and coding assistants need circuit breakers, caching, and queued retries to protect user flows.
- Watch next: Anthropic postmortem, SLO commitments, and client SDK features for auto-failover; compare outage frequency vs. OpenAI/Gemini over rolling quarters.
