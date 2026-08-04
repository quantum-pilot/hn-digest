# GitHub and the crime against software

- Score: 186 | [HN](https://news.ycombinator.com/item?id=48361064) | Link: https://eblog.fly.dev/githubbad.html

### TL;DR

Efron Licht argues GitHub’s outages and bloated interface reflect incentives favoring Copilot growth over reliability. Testing identical empty repositories over throttled 3G, he measured GitHub’s landing page at 291 requests, 15MB transferred, roughly 21 seconds to load, and 69MiB steady-state heap; Codeberg used 11 requests, about 1MB, three seconds, and 14MiB. HN sympathized and discussed mirroring or self-hosting, but emphasized that issues, reviews, CI, history, integrations, and social signals—not Git repositories—create the hardest lock-in.

### Comment pulse

- Multi-push makes source redundancy trivial → one Git remote can push simultaneously to GitHub, GitLab, and Codeberg.
- Platform metadata creates durable dependency → issues, pull requests, wikis, discussions, boards, and CI embody institutional knowledge Git cannot replicate.
- Alternatives feel cleaner → users praised Codeberg, Gitea, Forgejo, Tangled, and Radicle — counterpoint: GitHub’s discoverability and star economy remain powerful.

### LLM perspective

- **View:** The measurements expose real client cost, but one manually sampled, throttled test cannot establish architecture-wide causation.
- **Impact:** Teams seeking resilience need metadata exports, mirrored CI definitions, and tested fallback procedures—not merely additional push URLs.
- **Watch next:** Repeated cross-browser benchmarks, incident rates, SLA credits, metadata-export standards, and adoption of self-hosted alternatives.
