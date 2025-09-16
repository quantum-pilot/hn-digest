# Do the simplest thing that could possibly work

- Score: 1111 | [HN](https://news.ycombinator.com/item?id=45068091) | Link: https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/

- TL;DR
  - The author argues for always starting with the simplest design that satisfies today’s needs: fewer components, looser coupling, and lower operational overhead beat speculative “web‑scale” architectures. Examples include leaning on Unix primitives, boring REST, and in‑memory or proxy rate limiting before adding Redis—upgrade only when requirements force it. Objections addressed: hacks aren’t simple, “simple” favors operational stability, and over‑decoupling often reduces flexibility. HN debates center on unavoidable complexity at scale, chronic overengineering, the judgment needed to pick “simple,” and what “works” really means.

- Comment pulse
  - Scale mandates complexity → many edge cases and dependencies; beware removing unknown “fences” — counterpoint: lots was overengineered; simpler designs have served millions reliably.
  - Simplicity needs judgment → “simplest” isn’t a hack; choose partial implementations that evolve toward the desired architecture, avoiding one‑way doors.
  - Define “works” precisely → prototypes that “demo” omit reliability, security, and operations; later teams rebuild under pressure, paying deferred costs.

- LLM perspective
  - View: Operationalize “simple” with a scorecard: moving parts, coupling, run-cost, oncall toil, rollback ease; prototype, then ratchet when SLOs demand.
  - Impact: Shift teams to constrain infra SKUs, favor one-service ownership, and budget complexity explicitly via error budgets and deprecation plans.
  - Watch next: Define migration seams; prefer “two‑way door” changes; run probes and cost tracking before adding distributed components.
