# An illustrated guide to OAuth

- Score: 355 | [HN](https://news.ycombinator.com/item?id=45013131) | Link: https://www.ducktyped.org/p/an-illustrated-guide-to-oauth

### TL;DR

The guide explains OAuth through a budgeting app requesting limited bank-account access without receiving the user’s password. After user authentication and consent at the authorization server, the client receives a short-lived authorization code through the redirect, then exchanges it for an access token through a protected channel. Registered redirect URIs, client identifiers, secrets, and scopes constrain the flow; public clients should use PKCE because embedded secrets cannot remain secret. The article also distinguishes authorization from OpenID Connect login and notes refresh tokens and alternative flows.

### Comment pulse

- Implementers said introductory guides often omit details needed for secure, interoperable code.
- Readers corrected the claim that HTTPS POST alone defines a back channel or uniquely encrypts request data.
- Experienced practitioners favored authorization code with PKCE and warned against deprecated implicit and password flows.

### LLM perspective

- View: OAuth’s complexity reflects trust boundaries and accumulated attack lessons, not merely verbose terminology.
- Impact: Simplified explanations can become dangerous when they blur browser exposure, transport encryption, and client confidentiality.
- Watch next: Validate state, PKCE, redirect matching, token storage, rotation, revocation, and provider-specific deviations.
