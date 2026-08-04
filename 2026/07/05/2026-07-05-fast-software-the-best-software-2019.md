# Fast Software, the Best Software (2019)

- Score: 125 | [HN](https://news.ycombinator.com/item?id=48792008) | Link: https://craigmod.com/essays/fast_software/

### TL;DR

The essay argues that software speed is undervalued craft: instant response preserves flow, makes tools feel tactile, and becomes a proxy for reliability and engineering care. nvALT, Sublime Text, Figma, and Things earn trust through responsiveness; Ulysses, Photoshop, Lightroom, and Google Maps lose it through lag, bloat, or needless interaction steps. Speed includes work per user action, not just CPU time. HN agreed, citing migrations to lighter tools, offline OpenStreetMap apps, and client-side datasets that avoid API latency. Commenters disputed whether animations help, with many preferring direct feedback over masking.

### Comment pulse

- Latency shapes trust → lag on simple tasks suggests hidden engineering rot, even when no data loss or correctness failure has occurred.
- Local work can beat lean downloads → shipping a compressed dataset once may make repeated search faster than architecturally elegant API round trips.
- Animations can communicate progress → visible activity softens unavoidable waits — counterpoint: decorative transitions add latency and increasingly signal slow software rather than polish.

### LLM perspective

- **View:** Perceived speed combines latency, predictability, interaction count, and feedback; optimizing only benchmark throughput misses the user’s actual cycle time.
- **Impact:** Responsiveness compounds for tools used all day, affecting trust, adoption, retention, and willingness to pay more for simpler software.
- **Watch next:** Input latency, cold-start time, p95 interactions, local-versus-network tradeoffs, animation budgets, bundle growth, and performance regressions across releases.
