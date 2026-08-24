# List animals until failure

- Score: 321 | [HN](https://news.ycombinator.com/item?id=46842603) | Link: https://rose.systems/animalist/

### TL;DR

A browser game asks players to name as many animals as possible before a countdown expires. Each accepted animal adds time, must have a Wikipedia article, and cannot overlap a broader or narrower term already entered. Wikipedia, Wikidata and hand-tuned rules power validation; no LLM is used. HN players enjoyed the memory challenge and humorous JavaScript fallback, but quickly found taxonomy and matching errors: jellyfish versus Portuguese man-of-war, bobcat versus lynx, and even kudu becoming turtle. One reader built a speech-recognition variant for group play.

### Comment pulse

- Players described semantic fatigue: they could still picture animals after becoming unable to retrieve their names.
- Taxonomic edge cases exposed the conflict between scientific classification, common language and a game’s no-overlap rule.
- Speech input made group play lively, but recognition latency required a larger per-answer time bonus.

### LLM perspective

- View: The game’s appeal comes from simple recall pressure; its hard problem is defining acceptable animal boundaries.
- Impact: Imperfect ontology decisions can frustrate knowledgeable players while revealing how messy everyday biological categories are.
- Watch next: Validation fixes, transparent dispute rules, broader synonym handling and optional voice support with latency-adjusted timing.
