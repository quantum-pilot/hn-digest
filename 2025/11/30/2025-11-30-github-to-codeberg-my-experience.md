# GitHub to Codeberg: my experience

- Score: 109 | [HN](https://news.ycombinator.com/item?id=46097829) | Link: https://eldred.fr/blog/forge-migration/

### TL;DR

One developer moved 45 repositories from GitHub to Codeberg in roughly a weekend. Forgejo imported issues, pull requests, wikis, and releases reliably, though each repository required manual handling and API limits blocked parallel imports. The remaining work was rewriting links and remotes, archiving GitHub stubs, porting selected workflows to leaner Linux-only Forgejo Actions runners, and replacing GitHub Pages with Grebedoc's git-pages service. The author reports zero website downtime and modest effort, while accepting reduced discoverability, fewer contributions, and continued dependence on GitHub for upstream participation.

### Comment pulse

- GitHub's strongest moat is social → commenters cited discoverability, familiar documentation, integrations, free CI capacity, and contributor identity rather than core forge features.
- Small teams have several alternatives → self-hosted Forgejo, GitLab, SourceHut, and private runners trade convenience, resources, and ecosystem reach differently.
- Compute restraint split readers → Codeberg frames limited CI as financial and environmental discipline — counterpoint: critics prefer performance language over emissions messaging.

### LLM perspective

- View: Repository transport is straightforward; ecosystem and hosting edges create most migration cost.
- Impact: Independent maintainers gain control but assume integration choices and audience friction.
- Watch next: git-pages adoption, Forgejo Actions maturity, CI capacity, and contribution trends after migration.
