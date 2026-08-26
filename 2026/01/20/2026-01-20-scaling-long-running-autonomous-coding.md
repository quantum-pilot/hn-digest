# Scaling long-running autonomous coding

- Score: 162 | [HN](https://news.ycombinator.com/item?id=46686418) | Link: https://simonwillison.net/2026/Jan/19/scaling-long-running-autonomous-coding/

### TL;DR

Cursor coordinated hundreds of agents through planner, worker, and judge roles, producing FastRender: more than one million lines across 1,000 files after nearly a week. Initial skepticism centered on failing CI and absent build instructions, but by this article’s snapshot the README had been updated and the author built a functioning macOS browser that rendered recognizable pages with obvious glitches. HN debated whether this demonstrates scalable autonomy or an unusually favorable benchmark, citing reused libraries, unclear human involvement, enormous token cost, weak standards compliance, and unresolved correctness, security, and maintainability.

### Comment pulse

- Benchmark fit → browsers offer specs, tests, references, decomposable parts, and partial credit — counterpoint: production correctness is vastly harder.
- “From scratch” → dependencies such as html5ever and Taffy accelerated progress but weakened claims of an independently implemented engine.
- Verification gap → commenters wanted conformance tests, fuzzing, autonomy disclosures, cost accounting, and evidence that humans could maintain the code.

### LLM perspective

- View: The demo proves broad autonomous construction, not production-browser completeness or a repeatable engineering method.
- Impact: As code generation scales, trustworthy evaluation and lifecycle ownership become the limiting resources.
- Watch next: Track Web Platform Test results, fuzzing, security audits, token costs, human interventions, and sustained maintenance.
