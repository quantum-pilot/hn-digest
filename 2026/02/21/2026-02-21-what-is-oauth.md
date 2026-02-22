# What Is OAuth?

- Score: 201 | [HN](https://news.ycombinator.com/item?id=47096520) | Link: https://leaflet.pub/p/did:plc:3vdrgzr2zybocs45yfhcr6ur/3mfd2oxx5v22b

## TL;DR
OAuth was created at Twitter in 2006 to let third‑party apps act on a user’s behalf without ever seeing their password, replacing many bespoke, insecure schemes. Blaine Cook explains its core as simple delegation: with user consent, a service issues a reusable secret (token) to a third party, then defines how that token can be used to access resources; OpenID Connect layers sign‑in on top. HN discussion focuses on how later OAuth 2.0 evolution turned that simple core into a sprawling, sometimes painful framework.

## Comment pulse
- OAuth 2.0 criticized as over-engineered enterprise framework and consulting vehicle; original editor quit — counterpoint: security folks appreciated removing fragile crypto and relying on TLS.  
- Practitioners: OAuth is sprawling but lets you pick flows (auth code, device, client credentials, PKCE); preferable to SAML’s monolithic, frozen, XML-based 800‑page spec.  
- Many still find explanations opaque; mental model that helps: three-way protocol where a user grants limited, revocable rights for one service to act against another.

## LLM perspective
- View: Treat OAuth as “token minting plus token use” and hide flow details behind well-maintained libraries or managed providers.  
- Impact: Standardized delegation lets small teams integrate securely with major platforms instead of inventing fragile, one-off authentication schemes.  
- Watch next: Better conformance test suites, clearer teach-from-provider-perspective docs, and slimmer profiles for common cases could reduce perceived complexity.
