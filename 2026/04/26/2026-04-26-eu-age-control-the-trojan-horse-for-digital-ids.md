# EU Age Control: The trojan horse for digital IDs

- Score: 328 | [HN](https://news.ycombinator.com/item?id=47907130) | Link: https://juraj.bednar.io/en/blog-en/2026/04/17/eu-age-control-the-trojan-horse-for-digital-ids/

### TL;DR

The piece dissects the EU’s age‑verification “reference app” and argues it’s effectively a rollout vehicle for an attested, revocable digital ID stack. Legally, big platforms may skip the “privacy‑preserving” wallet and keep using full‑KYC providers, so privacy is optional marketing. Technically, the reference implementation doesn’t actually use zero‑knowledge proofs; unlinkability hinges on wallet behavior and is vulnerable to replay and large‑scale relay (“Grandma‑as‑a‑Service”) attacks. Hardware attestation ties access to Apple/Google‑approved phones, deepening platform lock‑in and enabling future function creep.

---

### Comment pulse

- Intent vs trojan horse → Some say digital ID is openly stated EU policy, with age checks just a pilot; others argue online IDs enable unprecedented tracking and industrialized circumvention.

- Root cause → One camp blames the age app; another says the real Trojan horse is locked‑down iOS/Android, sold as “security” yet excluding user‑controlled OSes.

- Crypto/design tradeoffs → Defenders cite secure‑element limits and favor ES256 + rotation; critics worry about revocation deanonymizing users and dismiss “fearmongering” — counterpoint: states already overreach with weaker tools.

---

### LLM perspective

- View: The central hazard is normalization: routine browsing and speech gradually conditioned on real‑world, revocable, device‑attested identity.

- Impact: Alternative OS users, minors routing around controls, and political dissidents face disproportionate exclusion or coercion.

- Watch next: Compare national wallet tenders, attestation policies, and emerging secure‑element support for stronger unlinkability schemes like BBS+/CL.
