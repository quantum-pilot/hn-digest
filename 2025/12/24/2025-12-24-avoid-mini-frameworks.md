# Avoid Mini-Frameworks

- Score: 108 | [HN](https://news.ycombinator.com/item?id=46374856) | Link: https://laike9m.com/blog/avoid-mini-frameworks,171/

- TL;DR  
    - An engineer from Google Ads argues that team-specific “mini‑frameworks” (wrappers over shared stacks that introduce new concepts) usually cause more pain than they solve. His internal example: an abstraction layer over a solid distributed framework dragged migrations out for a year, made simple tasks take weeks, fragmented the tech stack, and became unmaintainable once its few authors were overloaded or left. He recommends favoring simple libraries, avoiding new concepts, and treating framework creation as a serious, org‑level product decision.

- Comment pulse  
    - Framework vs library → commenters: key distinction is inversion of control; wrapping big frameworks is risky, but adapters around libraries can simplify usage and replacement.  
    - Abstractions misused → many see devs abstract to remove repetition, not complexity, yielding leaky, inflexible layers; better to implement something painfully ~10 times before generalizing.  
    - Org incentives → limited control over core systems and promotion for 'platforms' push teams toward wrappers, just relocating complexity—counterpoint: sometimes core owners block straightforward fixes.

- LLM perspective  
    - View: Mini-frameworks are often social problems—ego, incentives, ownership—masquerading as technical design decisions or productivity improvements.  
    - Impact: Stronger review cultures could demand deletion plans, ownership commitments, and user research before approving any new internal framework.  
    - Watch next: Dependency-mapping and migration-cost tools could quantify when wrappers are riskier than fixing issues in shared upstream frameworks.
