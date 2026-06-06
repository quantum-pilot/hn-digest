# From Supabase to Clerk to Better Auth

- Score: 186 | [HN](https://news.ycombinator.com/item?id=48038827) | Link: https://blog.val.town/better-auth

## TL;DR
Val Town recounts moving from Supabase’s integrated stack to a custom database with Clerk for auth, then abandoning Clerk for Better Auth. Clerk’s model of being both users and sessions storage clashed with Val Town’s social product: severe rate limits, webhook-based data syncing, and frequent outages turned it into a brittle single point of failure. Better Auth lets them own their data and session lifecycle while using an open-source, framework-integrated library. HN debates vendor risk, “never roll your own auth,” and auth’s true complexity.

## Comment pulse
- Own your auth stack → VC-backed auth SaaS is seen as lock‑in and future price gouging; outages and rate limits threaten core functionality.  
- Auth is deceptively complex → SSO, SAML, OAuth, 2FA, and nonstandard integrations consume huge engineering time—counterpoint: small apps can safely manage simple tables themselves.  
- Different comfort levels with risk → Some prefer Auth0-style outsourcing to reduce PII exposure; others want full control despite security responsibility.

## LLM perspective
- View: Treat auth as infrastructure: outsource primitives and libraries, not your canonical user data or session critical path.  
- Impact: Social or collaborative products must budget engineering for identity modeling, migrations, and failure scenarios beyond wiring an auth provider.  
- Watch next: Maturing open-source auth stacks, browser-level identity APIs, and more postmortems quantifying long-term costs of auth SaaS dependencies.
