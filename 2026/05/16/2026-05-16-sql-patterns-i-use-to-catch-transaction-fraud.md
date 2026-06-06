# SQL patterns I use to catch transaction fraud

- Score: 308 | [HN](https://news.ycombinator.com/item?id=48155212) | Link: https://analytics.fixelsmith.com/posts/sql-fraud-patterns/

### TL;DR
The post describes six SQL-based fraud heuristics: high-velocity transactions, “impossible travel” between distant locations, suspicious amounts (round numbers and threshold-hugging), merchant-level spikes, off-hours usage based on per-user history, and a window-function layer that turns these ideas into composable filters. The author stresses combining multiple weak signals, tuning thresholds, handling nulls, and avoiding auto-blocking on a single rule. HN commenters argue many examples are US-centric, naïve, or unrealistic, and several suspect the piece and its author are LLM-generated.

### Comment pulse
- Heuristics seem oversimplified and US-specific → round amounts, off-hours rules, and border-crossing checks would cause many false positives in Europe and elsewhere.  
- Article quality questioned → contradictions, hand‑wavy caveats, and odd details (GPS-like locations, nulls aside) read as speculative or LLM-written — counterpoint: criticise content, not authorship.  
- Practitioners note real systems → use IP-based impossible travel, special handling for VPN/relays, better statistics; bulk precise geolocation for swipes is uncommon.

### LLM perspective
- View: SQL heuristics are a decent teaching scaffold but should be framed as toy examples, not production-ready playbooks.  
- Impact: Useful for junior analysts learning window functions; dangerous if managers treat them as drop‑in fraud-defence recipes.  
- Watch next: Open, realistic fraud-detection datasets and benchmarked rules/ML models would ground these discussions beyond speculative or AI-written blogs.
