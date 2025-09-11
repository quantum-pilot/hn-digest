# Source code for the X recommendation algorithm

- Score: 244 | [HN](https://news.ycombinator.com/item?id=45183039) | Link: https://github.com/twitter/the-algorithm

• TL;DR (70–90 words)
X open-sourced the architecture behind its recommendation stack: shared data/services, candidate sources (search ~50% in-network, GraphJet/UTEG out-of-network), light/heavy rankers, Home/Push mixers, visibility filters, and ML models (SimClusters, TwHIN). No model weights, datasets, or prod build path; contributions invited. HN readers say this helps understand system design, not actual feed behavior, citing redactions and likely non-prod parity. Noted signals: screenshot events, NSFW/soft-NSFW, “slop” score, tweet-length bins. Recommended Notifications stack is also included.

• Comment pulse
- Unverifiable prod parity → ex-employees say this is a grab-bag, not what's running; heavy redactions limit auditability — counterpoint: open source rarely ensures prod parity.
- Politics/Elon labels controversy → earlier author_is_elon/democrat/republican removed; replaced by Grok topic tags marked metrics-only, not used for ranking.
- Telemetry and heuristics intrigue → screenshot events tracked; 'slop' author score; length buckets; hardcoded top-level topics (e.g., Anime); unknown impact on virality.

• LLM perspective
- View: Understanding real ranking requires A/B logs, training corpora, and policy configs; architecture alone is insufficient.
- Impact: Best for teaching recsys patterns and comparing pipelines; minimal value for accountability without datasets and evaluation harnesses.
- Watch next: Look for reproducible offline ranking tasks, public eval sets, and third-party audits diffing repo behavior against live timelines.
