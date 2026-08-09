# Codex pricing to align with API token usage, instead of per-message

- Score: 194 | [HN](https://news.ycombinator.com/item?id=47650726) | Link: https://help.openai.com/en/articles/20001106-codex-rate-card

### TL;DR

OpenAI changed Codex credit accounting for new and existing Business plans and new Enterprise plans, charging credits according to API-equivalent input, cached-input, and output tokens; fast mode doubles consumption. Existing Plus, Pro, Enterprise, and Edu users temporarily remain on legacy per-message rates, with migration expected. OpenAI estimates typical use at $100–$200 per developer monthly, but output-heavy work varies widely. Commenters objected that credits obscure currency costs, while noting the change is accounting alignment—not proof subscriptions are disappearing.

### Comment pulse

- Token accounting better tracks actual compute → opaque credits still make upfront task cost difficult to estimate.
- The headline suggests unbundling → current subscriptions remain, though listed cohorts are scheduled to migrate.
- Output and fast mode dominate spend → terse workflows and caching can materially alter consumption.

### LLM perspective

- **View:** API alignment improves internal consistency, but credits need clear currency conversion and per-task cost telemetry.
- **Impact:** Business teams can attribute heavy agents more accurately; individual subscribers face less predictable effective allowances after migration.
- **Watch next:** Plus and Pro migration terms, Enterprise timing, regional credit pricing, dashboards, caps, and overage controls.
