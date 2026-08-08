# From Supabase to Clerk to Better Auth

- Score: 186 | [HN](https://news.ycombinator.com/item?id=48038827) | Link: https://blog.val.town/better-auth

### TL;DR

Val Town replaced Clerk with Better Auth because Clerk’s hosted user records and session refreshes conflicted with a social application. A five-request-per-second user API forced webhook synchronization into a second users table, creating dual authority and incomplete-signup states; outages also locked out signed-in users. Better Auth keeps user and session data under Val Town’s control while offering open-source integrations and a stateless dashboard. The migration accepted both cookie formats for two weeks. Discussion split between owning core identity data and outsourcing SSO, MFA, anti-abuse, and integration edge cases.

### Comment pulse

- Some insisted authentication should never be outsourced — counterpoint: SSO, SAML, SCIM, OAuth, MFA, and provider quirks consume serious support expertise.
- Others valued hosted identity for reducing password handling, PII exposure, and duplicated login work across small sites.
- Readers praised the unusually candid account of a long-lived architectural decision and delayed migration.

### LLM perspective

- Separate identity, profile, and session authority explicitly; convenience SDKs can blur boundaries until production scale exposes them.
- Critical dependencies need graceful degradation, cached verification, migration exports, and tested provider-failure drills.
- Watch maintainer concentration, security disclosures, non-JavaScript support, and operational behavior at larger scale.
