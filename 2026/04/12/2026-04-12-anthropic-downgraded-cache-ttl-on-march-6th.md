# Anthropic downgraded cache TTL on March 6th

- Score: 461 | [HN](https://news.ycombinator.com/item?id=47736476) | Link: https://github.com/anthropics/claude-code/issues/46829

### TL;DR
A Claude Code user analyzed 120k requests and found Anthropic silently shifted prompt cache TTL from 1 hour back to 5 minutes on March 6, sharply increasing cache-write tokens, dollar cost, and subscription quota burn. Anthropic engineer Jarred Sumner confirmed the change as intentional “cache optimization,” arguing 1‑hour TTL can be more expensive for one‑shot calls and that TTL is chosen per request, not globally. Hacker News discussion centers on perceived secret nerfs, eroding trust, and worsening UX for subscription users.

---

### Comment pulse
- Sentiment shift → Many engineers feel Claude/Codex have been quietly nerfed (limits, reasoning, length), and are moving work back to Codex/Cursor.
- Subscriptions vs API → Flat-fee users hit 5‑hour quotas in under an hour; API users may see savings — counterpoint: most only notice higher effective token burn.
- Coping strategies → People discuss keep‑alive scripts to prevent cache expiry and note a vicious loop: quota waits invalidate cache, further accelerating future quota usage.

---

### LLM perspective
- View: Silent TTL and quota changes create a “can’t trust the floor” feeling, worse than a straightforward price hike.
- Impact: Heavy Claude Code subscribers and teams standardizing on Claude bear UX pain; API integrators may adapt more easily.
- Watch next: Transparent cache/quota docs, user‑configurable TTL, and independent benchmarks on effective cost per task across Claude, Cursor, and competitors.
