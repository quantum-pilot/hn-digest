# Who owns your ATProto identity?

- Score: 160 | [HN](https://news.ycombinator.com/item?id=48619140) | Link: https://kevinak.se/blog/who-actually-owns-your-atproto-identity-hint-its-probably-not-you

### TL;DR

ATProto Personal Data Servers hold users’ signing and rotation keys, so an operator or attacker can create valid activity as them, redirect their DID, or lock them out. Because one repository can span Bluesky, code, publishing, and apps, compromise expands across the ecosystem and is cryptographically hard to disavow. A higher-priority self-controlled rotation key limits lockout but is not default and does not stop signing impersonation. HN commenters debated threat likelihood versus architectural promises, emphasizing that self-hosting and migration exist but convenience keeps most users dependent on hosted PDSes.

### Comment pulse

- PDS trust differs from ordinary hosting → a provider can produce signatures indistinguishable from yours, unlike DNS redirection or unsigned account takeover.

- Portability exists only while key control cooperates → self-hosting is cheap, yet hosted defaults and migration friction keep most identities operator-dependent.

- Operator abuse is unlikely for ordinary users → hosted services resemble familiar trust models — counterpoint: high-risk users need self-controlled keys and verifiable disavowal.

### LLM perspective

- **View:** ATProto decentralizes data placement more than key custody; genuine identity sovereignty depends on who can authorize and revoke signatures.

- **Impact:** Journalists, maintainers, activists, and shared-identity users carry the highest impersonation costs and benefit most from independent rotation control.

- **Watch next:** Track default backup-key enrollment, client-side signing, audit logs, migration success rates, recovery drills, and app-specific key separation.
