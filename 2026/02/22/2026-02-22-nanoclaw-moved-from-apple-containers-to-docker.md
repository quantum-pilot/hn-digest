# NanoClaw Moved from Apple Containers to Docker

- Score: 89 | [HN](https://news.ycombinator.com/item?id=47113731) | Link: https://twitter.com/Gavriel_Cohen/status/2025603982769410356

### TL;DR

NanoClaw changed its default runtime from Apple Containers to Docker after growing from a Mac-centered personal project into software used by thousands, including production and business workloads. The maintainer chose Docker for universal availability and maturity, while keeping Apple Containers supported through a conversion command that applies a mostly deterministic Git merge in about 30 seconds. Commenters debated whether containerization meaningfully secures autonomous agents, proposed lightweight Unix daemons and per-user isolation, and noted that some workloads needing SSH or nested Docker may favor full virtual machines.

### Comment pulse

- Broader Linux access was viewed as community service rather than enterprise drift, though the announcement’s adoption language drew jokes.
- Containers limit filesystem damage — counterpoint: agents connected to email, secrets, and unrestricted networks retain serious application-level risks.
- QEMU appealed to developers needing SSH and nested container workflows, despite greater operational weight.

### LLM perspective

- **View:** Runtime portability solves installation reach; it does not reduce the agent’s application-level authority once credentials enter the sandbox.
- **Impact:** Operators still need separate secret boundaries, network policy, plugin identities, and escalation controls beyond Docker.
- **Watch next:** Linux reliability, Apple conversion conflicts, nested-container demand, VM support, secret isolation, and documented threat models.
