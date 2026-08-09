# The peril of laziness lost

- Score: 271 | [HN](https://news.ycombinator.com/item?id=47743628) | Link: https://bcantrill.dtrace.org/2026/04/12/the-peril-of-laziness-lost/

### TL;DR

Bryan Cantrill revisits Larry Wall’s “laziness” as an engineering virtue: spending effort to create abstractions that save future human time. LLMs invert that incentive because producing work costs them nothing and cognitive load does not constrain them. He contrasts a boast of 37,000 generated lines per day with an artifact reportedly bloated by test harnesses, sample code, an editor, and duplicate logos. His conclusion is not to reject AI, but to subordinate it to human judgment, using it for debt reduction and rigor while optimizing for smaller, composable systems.

### Comment pulse

- Experienced users said LLM-generated tests often optimize for passing, not coverage, requiring humans to define and protect meaningful assertions.
- Some prefer duplication until a third use case proves an abstraction; premature platforms can impose more complexity than they remove.
- Judging output quality still divided readers. — counterpoint: net value must include maintenance, security, deployment, and legal costs, not just features.

### LLM perspective

- **View:** AI makes code cheap, so deletion, boundaries, and comprehensibility become more valuable engineering outputs.
- **Impact:** Teams chasing throughput metrics can accumulate hidden operational and security liabilities faster than review capacity grows.
- **Watch next:** Measure changed behavior, defect escape, maintenance burden, and code removed—not prompts, tests, commits, or lines generated.
