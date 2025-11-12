# Firefox expands fingerprint protections

- Score: 256 | [HN](https://news.ycombinator.com/item?id=45888891) | Link: https://blog.mozilla.org/en/firefox/fingerprinting-protections/

- TL;DR
  - Firefox 145 rolls out stronger anti-fingerprinting in Private Browsing and ETP Strict, using real‑world data to curb leaks (fonts, graphics, hardware metrics) and halve uniquely identifiable users, while preserving needed features. It’s not default yet but headed there. HN welcomes the move, shares tactics (Temporary Containers, profiles, Tor), flags limits from Firefox’s smaller anonymity set, and reports mixed field tests (stable hashes, canvas‑size uniqueness) where letterboxing/jitter or privacy browsers like Mullvad/Tor can do better.

- Comment pulse
  - Session isolation via Temporary Containers/profiles/Tor → reduces cross-site correlation; GDPR supplies consent baseline — counterpoint: breaks logins and everyday workflows.
  - Firefox’s smaller population weakens anonymity sets → easier to fingerprint; some prioritize exploit/malvertising defense with NoScript+uBlock over chasing uniformity.
  - Live tests show persistent hashes; viewport/canvas size dominates → ask for smarter letterboxing or per-container jitter; Mullvad Browser groups users better than mainline Firefox.

- LLM perspective
  - View: Entropy reduction beats blacklist blocking; staged rollout with exceptions keeps sites functional while shrinking unique identifiers.
  - Impact: Fingerprinters pay higher costs to track; privacy-first users benefit now; sites see fewer breakages versus heavy-handed blocking.
  - Watch next: Default-on timeline, independent entropy audits, canvas/viewport strategies, and alignment with Tor/Mullvad and W3C Privacy Budget proposals.
