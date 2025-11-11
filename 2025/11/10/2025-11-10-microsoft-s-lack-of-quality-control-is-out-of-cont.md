# Microsoft's lack of quality control is out of control

- Score: 209 | [HN](https://news.ycombinator.com/item?id=45873876) | Link: https://www.theregister.com/2025/11/08/microsoft_lacks_quality_control/

TL;DR
- The Register argues Microsoft’s quality slid after 2014 tester layoffs and a shift to agile/telemetry, yielding recurring Windows update snafus (e.g., 2018 file deletion) and Azure outages from bad config rollouts. HN expands: auto-translated docs break code; role compression and frictionless internet delivery erode pre-release rigor; Microsoft maintains backward compatibility but not reliability. Debate on consequences: some foresee slow drift to Apple/Linux and multi-cloud; others say subscriptions/lock-in mute accountability, so little changes.

Comment pulse
- Killing dedicated QA hurt reliability → Devs juggle full‑stack and ops; fewer independent checks before release reduce defect interception.
- Auto-translation breaks docs → Reserved words/code blocks get translated, causing errors; localized Excel formulas confuse — counterpoint: most vendors ship similarly flawed MT.
- Consequences remain limited → Subscriptions and lock-in cushion backlash; attrition to Apple/Linux and multi-cloud is gradual, not existential.

LLM perspective
- View: Telemetry and rapid cadences can’t replace disciplined staging and rollback; OS/cloud need dedicated QA and change-control gates.
- Impact: IT teams will harden update policies, delay adoption, and hedge with macOS/Linux endpoints and multi-cloud to reduce single-vendor blast radius.
- Watch next: Track Azure postmortems, Windows update failure rates, rollback automation, and any investment in docs translation QA or restored testing headcount.
