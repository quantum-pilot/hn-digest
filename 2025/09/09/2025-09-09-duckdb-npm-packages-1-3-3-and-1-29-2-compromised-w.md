# DuckDB NPM packages 1.3.3 and 1.29.2 compromised with malware

- Score: 389 | [HN](https://news.ycombinator.com/item?id=45179939) | Link: https://github.com/duckdb/duckdb-node/security/advisories/GHSA-w62p-hx95-gf2c

TL;DR
Attackers phished a DuckDB maintainer via a convincing npmjs.help clone, reset 2FA, minted an API token, and pushed four npm releases containing malware targeting crypto transactions: @duckdb/node-api, @duckdb/node-bindings, and duckdb 1.3.3, plus @duckdb/duckdb-wasm 1.29.2. DuckDB detected it within hours, deprecated and had npm delete the versions, and re-released safe builds (1.3.4/1.30.0); no “legit” 1.3.3 will ship. HN debates mitigations: signed emails vs phishing-resistant auth (passkeys) and publish freezes; broader calls for end‑to‑end artifact signing and multi‑maintainer approvals.

Comment pulse
- Enforce passkeys and publish-freeze → Cooldown after 2FA/token changes would block takeover — counterpoint: signed emails often fail; users miss absent signals.
- Require end‑to‑end artifact signing → Offline/HSM keys + verify packages from signed Git tags; multi-maintainer approvals make stolen accounts insufficient to publish malware.
- Distrust email links → Use bookmarks and password managers’ domain checks; browsers could warn on mismatched origins; link tracking conditions users to ignore suspicious URLs.

LLM perspective
- View: Account phishing enabled a supply‑chain attack; pair phishing‑resistant auth with independent artifact trust roots.
- Impact: Auto‑update consumers are exposed; registries and tools will push passkeys, cooldowns, and default signature verification.
- Watch next: Registry freezes after auth changes, mandatory passkeys for maintainers, and signed, reproducible releases tied to Git tags.
