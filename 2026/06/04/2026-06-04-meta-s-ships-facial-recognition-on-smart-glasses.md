# Meta's ships facial recognition on smart glasses

- Score: 200 | [HN](https://news.ycombinator.com/item?id=48403588) | Link: https://www.buchodi.com/meta-glasses-facial-recognition/

### TL;DR

A reverse engineer found a complete but dormant facial-recognition stack in Meta’s Stella Android companion app for smart glasses. By directly invoking its handler, they made bundled models detect, align, and encode a face into 2,048 dimensions, query a local cosine index, notify on a match, and persist unmatched crops plus embeddings. Stock accounts showed no UI, enrollment data, or active recognition, so production use is unproven. HN saw strong accessibility value for prosopagnosia if fully offline, but overwhelmingly feared nonconsensual identification, cloud linkage, and Meta’s privacy record.

### Comment pulse

- Offline recognition could be transformative → face-blind users want a private, user-supplied database that identifies friends without involving any vendor cloud.
- Bystander consent is the central problem → wearable recognition can identify people who never enrolled — counterpoint: accessibility benefits need not require centralized data collection.
- Social defenses may emerge → commenters favored excluding wearers or detecting nearby Meta glasses, echoing Google Glass’s earlier prohibition on facial recognition.

### LLM perspective

- **View:** The decisive boundary is enrollment governance: who can add identities, whose consent counts, and where unmatched biometrics travel.
- **Impact:** Meta must earn consent from both wearer and bystander, a harder standard than ordinary app permissions.
- **Watch next:** Feature flags, server population of person_profiles, retention controls, biometric-law review, and independent traffic monitoring.
