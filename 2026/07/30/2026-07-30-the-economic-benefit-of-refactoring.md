# The Economic Benefit of Refactoring

- Score: 183 | [HN](https://news.ycombinator.com/item?id=49111176) | Link: https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html

### TL;DR

An agent-written 150,000-line application put its Rust data layer in one 17,155-line file. After 15 guided refactoring stages, identical changes by fresh agents used 27,360 input tokens versus 159,564 initially, an 83% drop, while output stayed similar. Total layer size barely changed; logical file boundaries helped agents select less code. One change saved about $0.40 at cited pricing, but the unknown refactoring cost weakens payback claims. Commenters welcome quantitative evidence while stressing human architecture and risks from optimizing code solely for models.

### Comment pulse

- Old practice gains a new metric → commenters see modularity and embedded documentation helping agents just as they have long helped humans.
- Human direction remains decisive → agents can execute specific transformations, but discovering coherent abstractions requires architectural intent and whole-system knowledge.
- Optimization target divides opinion → compact context may improve reasoning and correctness — counterpoint: minimizing tokens could sacrifice human readability.

### LLM perspective

- View: The gain comes from semantic locality, not file count; arbitrary splitting merely distributes search cost.
- Impact: Agent-heavy teams should budget cleanup as recurring infrastructure work, not discretionary polish.
- Watch next: Replicate across codebases, task complexity, languages, models, output tokens, and fully measured refactoring costs.
