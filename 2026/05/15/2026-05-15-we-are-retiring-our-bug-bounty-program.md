# We are retiring our bug bounty program

- Score: 344 | [HN](https://news.ycombinator.com/item?id=48148391) | Link: https://turso.tech/blog/the-wonders-of-ai

### TL;DR

Turso is ending its $1,000 reward for reproducible data-corruption bugs after maintainers became overwhelmed by AI-generated submissions that manufactured corruption, mislabeled intended behavior, or reopened rejected claims. The program had previously paid five skilled researchers and improved testing around Turso’s SQLite rewrite, but generating junk now takes minutes while evaluation consumes hours. A vouching and auto-close system only shifted spam into appeals and duplicate accounts. HN largely accepted the decision, framing review and comprehension as software’s scarce resource while debating fees, platform enforcement, and contributor access.

### Comment pulse

- Reading is the bottleneck → prolific code generation transfers cost to reviewers, debugging, and future maintainers who must establish genuine understanding.
- Refundable submission fees could deter spam → critics predicted payment overhead, endless disputes, unfair losses, and barriers for legitimate reporters.
- Platforms should police automated abuse → some viewed junk PRs as GitHub-scale spam, while bot honeypots offered a playful but temporary countermeasure.

### LLM perspective

- View: Open contribution depends on asymmetric trust; cheap, persistent generation makes human attention the exploitable resource.
- Impact: Legitimate researchers lose a cash incentive, while maintainers preserve review capacity and keep contributions open.
- Watch next: Repository-level rate limits, reputation gates, proof-of-work mechanisms, and whether high-quality vulnerability reports decline.
