# Don't use passkeys for encrypting user data

- Score: 235 | [HN](https://news.ycombinator.com/item?id=47189749) | Link: https://blog.timcappalli.me/p/passkeys-prf-warning/

### TL;DR

The author supports passkeys for phishing-resistant authentication but warns against making a WebAuthn PRF-derived secret the sole key for durable encrypted data. Authentication credentials are expected to be replaceable; losing an encryption key permanently destroys access. Current managers may let users delete an unfamiliar passkey without revealing that backups, messages, files, or wallets depend on it. HN largely agreed the lifecycle mismatch is dangerous, while distinguishing it from passkeys generally and favoring passwords, recovery codes, devices, or social recovery as independent fallback paths.

### Comment pulse

- Deletion warnings cannot repair a sole-key design → users need an independent recovery path before credentials disappear.
- Passkey UX remains fragmented → OS, browser, and manager boundaries make creation, storage, synchronization, and deletion hard to reason about.
- Key loss is intrinsic to encryption → informed irrecoverability can be valid — counterpoint: hidden coupling denies users that informed choice.

### LLM perspective

- **View:** Use PRF output as one unlock factor, never the only durable key.
- **Impact:** Relying parties and credential managers need dependency-aware lifecycle UX.
- **Watch next:** Adoption of PRF-usage metadata and deletion warnings across major credential managers.
