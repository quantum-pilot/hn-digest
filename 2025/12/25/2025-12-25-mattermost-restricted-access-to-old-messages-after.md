# Mattermost restricted access to old messages after 10000 limit is reached

- Score: 328 | [HN](https://news.ycombinator.com/item?id=46383675) | Link: https://github.com/mattermost/mattermost/issues/34271

### TL;DR

After upgrading, a school running self-hosted Mattermost for more than 2,000 active users and 470,000 posts found older messages hidden once the free Entry offering’s 10,000-message history limit applied. Users said retroactively gating data on their own server destroyed trust, especially when available plans mismatched high-user, low-feature deployments. Workarounds discussed include Team Edition, staying on v10.11 ESR temporarily, rebuilding source without the limit, or migrating. HN supplied code changes, questioned the mixed licensing, and recommended forks or alternatives.

### Comment pulse

- Self-hosting made the restriction feel illegitimate → customers supply storage and infrastructure yet lost ordinary access to existing history.
- Communication compounded the pricing change → commenters saw inadequate migration guidance and simultaneous user or SSO reductions as coercive.
- Source availability offers an escape hatch → custom builds can remove limits, though maintenance burden and licensing complexity remain.

### LLM perspective

- View: Retroactive access limits convert a pricing decision into a trust and data-governance failure.
- Impact: Administrators must choose paid plans, maintained forks, older supported releases, or costly migrations under time pressure.
- Watch next: Monitor official remediation, v10.11 support deadlines, fork sustainability, export completeness, and licensing clarification.
