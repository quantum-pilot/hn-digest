# Claude Code users hitting usage limits 'way faster than expected'

- Score: 263 | [HN](https://news.ycombinator.com/item?id=47586176) | Link: https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/

### TL;DR

Anthropic acknowledged that Claude Code users were exhausting quotas much faster than expected and made the investigation its top priority. Possible overlapping causes include peak-hour reductions affecting about 7% of users, expiration of a doubled-usage promotion, five-minute prompt-cache lifetimes, and reported cache-invalidating bugs that can multiply token use. Exact plan allowances remain undisclosed, making diagnosis and capacity planning difficult. HN users disputed whether identified resume and string-replacement bugs explain the wider spike, demanded quota credits and transparency, and warned that automated retries can silently consume budgets.

### Comment pulse

- Opaque, shifting allowances feel like pricing experiments because customers cannot distinguish policy changes, corrected undercounting, and software defects.
- Cache invalidation on resume or certain text may waste tokens — counterpoint: severe reports also occur in small, simple, non-resumed sessions.
- Heavy users still prefer Claude on complex repositories but are testing longer-lasting subscriptions and capable local models.

### LLM perspective

- **View:** Undefined quotas turn every regression into an unresolvable trust dispute between provider and customer.
- **Impact:** Automated workflows must recognize rate limits, cap retries, and avoid treating generic failures as permission to spend again.
- **Watch next:** Root-cause disclosure, fixed client versions, restored quota, customer credits, explicit allowance units, and cache-usage telemetry.
