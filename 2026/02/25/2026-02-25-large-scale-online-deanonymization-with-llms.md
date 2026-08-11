# Large-Scale Online Deanonymization with LLMs

- Score: 170 | [HN](https://news.ycombinator.com/item?id=47139716) | Link: https://simonlermen.substack.com/p/large-scale-online-deanonymization

### TL;DR

Researchers show that LLM agents can connect pseudonymous posts to identities by extracting biographical clues, narrowing candidates with embeddings, then reasoning over matches. Their proxies relink anonymized Hacker News accounts to known LinkedIn profiles and split Reddit histories across time or communities, outperforming activity-based baselines at high precision as candidate pools grow. In a real-world test without ground truth, manual review credited 9 of 125 anonymized scientist interviews as identified. HN anticipated chilling effects and broader harassment, while some argued governments and corporations already possess easier identification channels.

### Comment pulse

- Small clues combine into unique fingerprints → city, job, conferences, hobbies, and repeated phrasing can collapse anonymity without explicit identifiers.
- Cheaper automation expands the attacker pool → adversaries without government data access can target activists, workers, or ordinary ideological opponents.
- Public knowledge may contract → counterpoint: real-name participation can encourage accountability, though it does not prevent profiling or retaliation.

### LLM perspective

- **View:** Pseudonymity now offers separation by convention, not durable protection against correlation.
- **Impact:** Platforms must treat bulk profile access as sensitive infrastructure rather than harmless public data.
- **Watch next:** Rate limits, scraping detection, benchmark replication, false matches, refusal bypasses, and measurable chilling effects.
