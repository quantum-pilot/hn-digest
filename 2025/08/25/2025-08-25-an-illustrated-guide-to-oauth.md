# An illustrated guide to OAuth

- Score: 355 | [HN](https://news.ycombinator.com/item?id=45013131) | Link: https://www.ducktyped.org/p/an-illustrated-guide-to-oauth

- TL;DR
    - The piece demystifies OAuth via a YNAB–Chase example: redirect to the authorization server, user consents to scopes, receive an authorization code, exchange it server‑side for an access token. It clarifies roles (client, resource/authorization servers), redirect URIs, client ID/secret, and why PKCE is used for public clients; notes token expiry/refresh and OIDC for login. HN readers say implementation remains tricky; specs and OAuth 2.1 with PKCE are best practice, front/back‑channel was oversimplified, and they want concrete, cURL-level examples.

- Comment pulse
    - Implementing is hard → Read RFCs; use Authorization Code + PKCE; libraries miss app-specific surfaces; refresh tokens often expire; resources: Aaron Parecki, Duende IdentityServer.
    - Front vs back channel nuance → Both are HTTPS-encrypted; risk is URLs in history/logs and browser referrers vs server-to-server exchanges crossing different trust boundaries.
    - OAuth2 criticized → Code/hash leaks, weak redirect validation, optional state; prefer stricter 2.1 defaults. — counterpoint: It’s a flexible skeleton; careful config and PKCE mitigate.

- LLM perspective
    - View: Use authorization code + PKCE, strict redirect whitelists, state+nonce, and referrer policies; never expose tokens in URLs.
    - Impact: Teams building clients/servers need threat models, end-to-end tests, and operational token rotation; choose mature providers or audited OSS implementations.
    - Watch next: Track OAuth 2.1 finalization, OIDC updates (FAPI/Browser changes), and browser referrer policy defaults; demand API docs with cURL flows and error cases.
