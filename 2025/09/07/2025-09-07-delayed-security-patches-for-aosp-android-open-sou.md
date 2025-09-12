# Delayed Security Patches for AOSP (Android Open Source Project)

- Score: 221 | [HN](https://news.ycombinator.com/item?id=45158523) | Link: https://twitter.com/grapheneos/status/1964561043906048183

TL;DR
GrapheneOS says the post title misreads their complaint: AOSP isn’t uniquely delayed. Google shifted Android to quarterly public security updates while giving OEMs 3–4 months’ early access (formerly ~1), weakening embargoes and permitting binary‑only fixes. Monthly AOSP tags have stopped, and a quarterly release was late, delaying some non‑security fixes. Commenters see this as Google tightening control over Android/Chromium, argue regulation or divestiture is needed, and suggest Firefox over Chromium for forks. Security teams fear early‑access leaks and longer exposure windows.
- Content unavailable; summarizing from title/comments.

Comment pulse
- Misleading title → Security backports landed in AOSP; Android-wide change moves to quarterly releases with 3–4 month OEM lead and binary-only exceptions, weakening embargo secrecy.
- Missing monthly tags/QPR delays → Non‑security fixes stall; GrapheneOS can ship security patches via OEM access — counterpoint: broader delay increases exposure across Android devices.
- Longer OEM lead creates leak risk → Broad pre-release distribution leaks; binary-only patches are easily reversed (especially Java/Kotlin), nullifying secrecy.

LLM perspective
- View: Longer OEM lead times trade OEM readiness for user risk; transparency and synchronized source releases matter more than embargo theatrics.
- Impact: Security teams/OEMs gain planning buffer; aftermarket OSes and researchers face delayed sources; attackers benefit from leaked or reversible fixes.
- Watch next: Track CVE disclosure-to-public-source lag, AOSP tag cadence, and OEM patch SLAs; note any reversal of binary-only exceptions or cadence policy.
