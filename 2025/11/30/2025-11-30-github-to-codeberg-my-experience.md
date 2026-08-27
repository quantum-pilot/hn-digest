# GitHub to Codeberg: my experience

- Score: 109 | [HN](https://news.ycombinator.com/item?id=46097829) | Link: https://eldred.fr/blog/forge-migration/

### TL;DR

One developer migrated 45 repositories from GitHub to Codeberg in roughly a weekend. Forgejo imported repositories, issues, pull requests, wikis, and releases, but API limits made the per-repository process manual and serial. Repointing links and archiving GitHub stubs was scriptable. Forgejo Actions required modest YAML changes, fewer preinstalled tools, and Linux-only runners; the author also reduced unnecessary CI. Because Codeberg Pages is in maintenance mode, the website moved to git-pages through Grebedoc, preserving paths, redirects, headers, and zero-downtime DNS migration.

### Comment pulse

- Technical parity is adequate for many projects → GitHub’s documentation, integrations, identity, and network effects remain the larger moat.
- Codeberg serves public free-software projects; private teams may need self-hosted Forgejo, GitLab, SourceHut, or another provider.
- Free CI exists but capacity is constrained, encouraging lighter pipelines or self-hosted runners.

### LLM perspective

- View: Repository migration is straightforward; social discovery, CI capacity, and hosted pages carry the real switching cost.
- Impact: Small maintainers can reduce platform dependence without immediately deleting historical GitHub links.
- Watch next: Track contribution rates, runner reliability, Pages migration, redirects, and maintenance effort over the next year.
