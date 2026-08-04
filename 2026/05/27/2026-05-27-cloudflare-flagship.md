# Cloudflare Flagship

- Score: 342 | [HN](https://news.ycombinator.com/item?id=48287468) | Link: https://developers.cloudflare.com/flagship/

### TL;DR

Cloudflare’s Flagship adds managed feature flags with native Workers evaluation and an OpenFeature-compatible JavaScript SDK for Workers, Node.js, and browsers. Teams can target users with grouped rules, run consistent percentage rollouts, and return booleans, strings, numbers, or JSON without redeploying. HN agreed that reliable flag delivery has real operational value despite booleans-as-a-service jokes, but debated local versus fetched evaluation and warned against conflating flags with configuration or entitlements. The sharpest concern was browser tokens spanning every app in an account; app-scoped tokens are still being built.

### Comment pulse

- Local evaluation maximizes agility → in-memory rules make checks constant-like — counterpoint: periodic customer-specific snapshots may be simpler than maintaining multilingual edge SDKs.
- Flags need semantic boundaries and cleanup → configuration, experiments, and entitlements have different lifecycles; unchecked flexibility creates governance debt.
- Account-wide browser tokens expand exposure → clients may evaluate flags across apps; a Cloudflare engineer said app-scoped tokens are in progress.

### LLM perspective

- **View:** Feature flags are distributed control-plane state; value comes from consistency, latency, auditability, and cleanup—not the boolean itself.
- **Impact:** Workers users gain native integration, while browser deployments must treat flag data and targeting inputs as publicly observable.
- **Watch next:** Verify browser threat modeling, offline-evaluation semantics, SDK caching, propagation latency, audit logs, limits, pricing, and stale-flag tooling.
