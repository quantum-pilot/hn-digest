# Why We Abandoned Matrix (2024)

- Score: 172 | [HN](https://news.ycombinator.com/item?id=46376201) | Link: https://forum.hackliberty.org/t/why-we-abandoned-matrix-the-dark-truth-about-user-security-and-safety/224

### TL;DR

Hack Liberty says it replaced Matrix with self-hosted SimpleX after two years administering federated services. Its polemic cites Matrix metadata exposure, homeserver impersonation possibilities, complex state resolution, advisory deletion, media-replication abuse, resource costs, prior Megolm research, and difficult federation-wide moderation; it presents SimpleX’s identifier-free queues, temporary relays, mandatory encryption, and Tor options as safer. HN corroborated Matrix’s operational complexity but challenged sweeping claims: some reported years of trouble-free use, maintainers cited 2025 state-resolution improvements, and SimpleX critics noted default IP exposure, concentrated hosting, and immature group migration.

### Comment pulse

- Operational burden → large rooms, Synapse storage, state history, and federation complexity frustrate admins, though newer work reportedly reduced state resets.
- Threat-model dispute → Matrix leaks metadata; SimpleX avoids application identifiers but still reveals IPs to chosen relays without optional Tor.
- User experience → Matrix works smoothly for many private communities and bridges — counterpoint: onboarding, voice changes, and missing social features drove others away.

### LLM perspective

- View: The post mixes documented weaknesses, administrator experience, outdated points, and advocacy; its absolute conclusions require independent scrutiny.
- Impact: Communities must choose between Matrix’s mature federation and SimpleX’s metadata-focused design, smaller ecosystem, and different operational risks.
- Watch next: Audit current Matrix fixes, SimpleX relay diversity, Tor usability, group reliability, migration, moderation, and reproducible resource measurements.
