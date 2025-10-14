# Software update bricks some Jeep 4xe hybrids over the weekend

- Score: 305 | [HN](https://news.ycombinator.com/item?id=45568700) | Link: https://arstechnica.com/cars/2025/10/software-update-bricks-some-jeep-4xe-hybrids-over-the-weekend/

- TL;DR
  - A Friday OTA telematics update for Jeep Wrangler 4xe (Uconnect) caused vehicles to lose propulsion while driving; some were stranded on highways. Stellantis pulled the update, told owners to ignore prompts and avoid hybrid/EV modes, and pushed a fix Sunday. Owners describe poor communication, contradictory guidance, and no way to confirm whether the bad or fixed build is installed. HN debates OTA safeguards (A/B slots, motion gating), the auto industry’s BOM-driven tradeoffs, and Stellantis’ shaky software quality.

- Comment pulse
  - Safety/comms: Owners report highway power loss; no official guidance; dealers uninformed; can’t verify bad/fixed build — counterpoint: Updates should block in-motion via UDS; evidence unclear.
  - Engineering: A/B slots and rollback common even in cheap IoT; auto BOM constraints and dependencies complicate OTA; likely buggy firmware, not boot corruption.
  - Reputation/culture: Longstanding Stellantis QC complaints; Wagoneer glitch anecdotes; mockery of “vibe coding” mandate as misaligned with safety-first engineering.

- LLM perspective
  - View: Treat infotainment/telematics updates as non-safety; hard-isolate from powertrain, require park/charger, staged rollouts, canaries, and automatic fleet rollback.
  - Impact: Expect NHTSA investigations and recall; OEMs will adopt stricter OTA gating, A/B everywhere, and better owner comms with VIN-level status.
  - Watch next: Watch for Stellantis root-cause postmortem, revalidation plan, and compensation; telemetry changes to block in-motion updates; dealer reflash procedures.
