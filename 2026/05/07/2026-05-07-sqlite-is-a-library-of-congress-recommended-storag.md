# SQLite Is a Library of Congress Recommended Storage Format

- Score: 596 | [HN](https://news.ycombinator.com/item?id=48042434) | Link: https://sqlite.org/locrsf.html

## TL;DR
SQLite’s file format was named a Recommended Storage Format for datasets by the US Library of Congress, alongside XML, JSON, and CSV. Their criteria emphasize openness, adoption, transparency, self-documentation, minimal dependencies, and lack of patents/DRM—qualities SQLite’s simple, well-documented binary format fits well. HN commenters celebrate SQLite’s reliability and performance for most apps, debate its single-node durability and security risks as a “just a file” database, and mention niche alternatives plus the Library’s longer-term preservation thinking.

## Comment pulse
- SQLite praised as default store; WAL handles many workloads. — counterpoint: some argue single-node file storage lacks durability of replicated database clusters.  
- File-like nature makes SQLite easy but risky: databases can be copied, spreading PII; firms sometimes ban it, likening risks to Excel or Access "shadow IT".  
- Readers admire Library of Congress planning centuries ahead but note 2018 designation feels dated; 2026 list now includes more formats and even favors XLS.  

## LLM perspective
- View: LoC endorsement validates SQLite as not just an embedded DB but a durable archival container for structured datasets.  
- Impact: Encourages researchers, governments, and app developers to ship queryable data bundles instead of ad hoc CSV or JSON piles.  
- Watch next: standardized tooling for versioning, encrypting, and replicating SQLite-based archives to mitigate single-file loss and organizational governance concerns.
