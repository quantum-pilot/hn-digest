# DuckDB NPM packages 1.3.3 and 1.29.2 compromised with malware

- Score: 389 | [HN](https://news.ycombinator.com/item?id=45179939) | Link: https://github.com/duckdb/duckdb-node/security/advisories/GHSA-w62p-hx95-gf2c

### TL;DR

Attackers phished a DuckDB maintainer through a pixel-perfect npm clone at `npmjs.help`, proxied a real login and two-factor reset, then created an API token. They published four malicious Node packages designed to interfere with cryptocurrency transactions: three at version 1.3.3 and the WASM package at 1.29.2. DuckDB detected the incident within four hours, deprecated and removed those releases, rotated credentials, and published higher safe versions. Maintainers warned that no legitimate DuckDB 1.3.3 will exist and are reviewing release controls.

### Comment pulse

- Commenters favored phishing-resistant passkeys, signed packages, and mandatory publication freezes after authentication or token changes.
- Others argued security guidance should discourage following emailed links, since missing authenticity signals are easy to overlook.

### LLM perspective

- View: TOTP protected the login ceremony but not a real-time proxy that controlled the entire credential-reset flow.
- Impact: Brief maintainer compromise can expose downstream dependency users before registries or teams react.
- Watch next: Passkey enforcement, release provenance, token scoping, auth-change freezes, anomaly detection, and lockfile audits.
