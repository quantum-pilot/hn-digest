# The GitHub Actions control plane is no longer free

- Score: 213 | [HN](https://news.ycombinator.com/item?id=46291500) | Link: https://www.blacksmith.sh/blog/actions-pricing

### TL;DR

Third-party runner vendor Blacksmith interprets GitHub's new $0.002-per-minute Actions platform fee, effective March 1, 2026, as monetizing the control plane even when customers supply compute. It argues that simultaneous hosted-runner price cuts make GitHub's own capacity more attractive and establish a revenue floor across runner choices. Blacksmith's proposed response is predictable but concrete: reduce billed minutes through faster processors, persistent Docker-layer caching, and pre-hydrated service containers. Its economic explanation remains a vendor's inference, not GitHub's stated motive.

### Comment pulse

- Commenters dispute whether the fee legitimizes third-party runners or deliberately nudges users back toward GitHub-hosted capacity.
- Others suggest per-job pricing would better reflect control-plane work than charging by execution time.

### LLM perspective

- View: The fee turns CI duration into both a compute metric and a platform-tax multiplier.
- Impact: Faster third-party runners may remain economical, but vendors must now explain savings against a less intuitive baseline.
- Watch next: Compare full bills, not headline rates, once GitHub's hosted cuts and self-hosted fee coexist.
