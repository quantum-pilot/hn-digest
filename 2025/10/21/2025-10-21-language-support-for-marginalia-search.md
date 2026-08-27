# Language Support for Marginalia Search

- Score: 161 | [HN](https://news.ycombinator.com/item?id=45653143) | Link: https://www.marginalia.nu/log/a_126_multilingual/

### TL;DR

Marginalia Search added experimental German, French, and Swedish support by parameterizing language detection, normalization, stemming, part-of-speech tagging, and keyword patterns. Separate language indexes avoid cross-language homophones, lexicon growth, collisions, and slower ranking, while sharing document lists. The larger obstacle is corpus imbalance: 112.8 million English documents versus 7.6 million German, 4.9 million French, and 1 million Swedish. A new domain-discovery process has found roughly 800,000 viable domains and may improve multilingual crawling, but evaluation remains data-starved.

### Comment pulse

- Readers valued the implementation detail → the author uses explanatory release notes to clarify both the work and his own reasoning.
- Human inspection remains necessary → language nuance exceeds regression suites, motivating a tool that exposes intermediate annotations.
- Site-specific search is planned → ad-hoc domain filters may eventually reach the public API after performance work.

### LLM perspective

- View: Multilingual search is primarily a corpus and linguistic-model problem, not a simple interface translation.
- Impact: Separate indexes preserve speed and relevance but require users or callers to choose a result language upfront.
- Watch next: Measure recall per language, seed non-English domains, inspect normalization errors, and monitor hash-collision costs as corpora grow.
