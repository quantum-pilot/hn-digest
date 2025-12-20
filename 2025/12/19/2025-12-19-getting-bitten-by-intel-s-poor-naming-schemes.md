# Getting bitten by Intel's poor naming schemes

- Score: 276 | [HN](https://news.ycombinator.com/item?id=46322540) | Link: https://lorendb.dev/posts/getting-bitten-by-poor-naming-schemes/

### TL;DR
A hobbyist tried to upgrade a Dell Precision T3610 from a Xeon E5‑1650 v2 to a cheap Xeon E7‑8890 v4 after Intel’s spec pages claimed both used the “FCLGA2011” socket. In reality, they use incompatible socket variants: LGA2011‑0 (Socket R) vs LGA2011‑1 (Socket R2). Intel’s public docs flatten these into the same label, turning a supposedly simple upgrade into an expensive paperweight. HN commenters pile on with more examples of chaotic CPU/GPU naming and opaque hardware capability signaling.

---

### Comment pulse
- Hardware naming is fragmented (codenames, CPUID bits, marketing names) → impossible to correlate vulnerabilities or features without booting hardware—counterpoint: some OS devs just hard-require “last 10 years” and hope.
- Consumer/mobile CPU names hide huge performance/TDP gaps (e.g., Intel U vs H vs HX) → ordinary buyers can’t tell that “similar” model numbers differ drastically.
- Sockets and platforms are named inconsistently across vendors → Intel uses near-identical names for incompatible sockets; AMD’s longer-lived sockets improve resale and reduce upgrade surprises.

---

### LLM perspective
- View: Hardware naming is optimized for marketing and segmentation, not user comprehension; even vendors’ own docs leak abstraction layers inconsistently.
- Impact: Self-hosters, OS authors, and small IT shops pay in wasted money, time, and unnecessary hardware churn.
- Watch next: Community-maintained “caniuse for CPUs” databases, better CPUID-to-marketing-name mappings, and vendors pressured to expose clearer compatibility matrices.
