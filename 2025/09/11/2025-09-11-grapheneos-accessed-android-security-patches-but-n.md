# GrapheneOS accessed Android security patches but not allowed to publish sources

- Score: 242 | [HN](https://news.ycombinator.com/item?id=45208925) | Link: https://grapheneos.social/@GrapheneOS/115164133992525834

- TL;DR
  - Google’s updated Android patch embargo lets OEMs ship binary fixes immediately but withholds sources for 3–4 months. GrapheneOS can see patches yet can’t publish code or ship source-based updates, leaving its users exposed while OEM devices get binaries. Critics argue attackers can diff binaries or rely on leaks, making the embargo counterproductive; others see faster OEM binaries as a small win. Debate centers on whether the policy prioritizes OEM logistics over security and open-source transparency.
  - Content unavailable; summarizing from title/comments.

- Comment pulse
  - Attackers get 3–4 months of early insight → embargo leaks through bin-diffing and vendor leaks—counterpoint: OEMs can ship binaries immediately, slightly reducing exposure.
  - GPL leverage → kernel and driver sources must be provided on request, often within 30 days; binary releases can trigger mandatory disclosures.
  - Proposed path → ship opt‑in binaries, crowdsource GPL requests and reverse‑engineering; later publish sources once public evidence exists, demonstrating policy incoherence.

- LLM perspective
  - View: Security-by-obscurity period shifts risk to aftermarket ecosystems and long-tail devices; coordinated release needs better disclosure choreography, not prolonged secrecy.
  - Impact: Breaks trust in AOSP openness; projects like GrapheneOS must delay or adopt awkward binary pipelines, fragmenting Android security delivery.
  - Watch next: Signals from OEM patch cadence, any GPL enforcement actions, and whether community diffing accelerates exploit development post-binary releases.
