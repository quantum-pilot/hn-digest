# GitHub is sinking

- Score: 210 | [HN](https://news.ycombinator.com/item?id=48085095) | Link: https://dbushell.com/2026/04/29/github-is-sinking/

### TL;DR

David Bushell argues GitHub’s worsening outages, bot activity, AI-generated code volume, fake stars, Actions complexity, and Microsoft-era product direction make it a liability rather than essential infrastructure. Because Git is distributed, he recommends gradual migration or mirroring to alternatives such as Codeberg and Forgejo, self-hosting, or even plain SSH, while keeping an exit plan. Commenters confirmed rate-limit and availability frustrations but disputed causation: some blamed agent-driven load or Azure migration, while others noted the chart’s perfect pre-acquisition uptime looks like inconsistent status reporting rather than proof Microsoft caused the decline.

### Comment pulse

- Unauthenticated users reported secondary rate limits on ordinary commit-history views; logging in or hard-refreshing sometimes bypassed the failure.
- AI may have multiplied repository and CI load — counterpoint: the cited reliability decline begins years before agentic coding became widespread.
- Alternative-forge users disagreed sharply over GitLab and Bitbucket usability, reinforcing that migration trades one platform’s weaknesses for another’s.

### LLM perspective

- View: The strongest argument is portability and redundancy; the weakest is attributing a noisy availability graph to one corporate event.
- Impact: Projects can reduce lock-in by mirroring code, externalizing CI, exporting issues, and documenting recovery paths.
- Watch next: GitHub’s capacity fixes, status methodology, AI workload growth, migration tooling, federation progress, and reliability data across alternatives.
