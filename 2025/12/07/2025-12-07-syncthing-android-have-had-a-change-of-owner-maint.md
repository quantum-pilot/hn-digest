# Syncthing-Android have had a change of owner/maintainer

- Score: 105 | [HN](https://news.ycombinator.com/item?id=46184730) | Link: https://github.com/researchxxl/syncthing-android/issues/16

### TL;DR
Syncthing’s popular Android client (Syncthing-Fork / syncthing-android) has a new maintainer, “researchxxl”, who received the repo and signing keys from the previous maintainer, Catfriend1. A prior contributor, “nel0x”, is helping handle builds and Play Store publishing. They’re setting up GitHub Actions with protected signing keys, coordinating with F-Droid, and relying on reproducible builds and F-Droid verification to prove nothing malicious changed. HN discussion focuses on confusing forks, trust in the new owner, and broader Syncthing privacy/Android issues.

---

### Comment pulse
- Confusion about ecosystem → multiple repos (original, Fork, wrapper, new fork), several maintainers, and changing package names obscure who’s “official” and trustworthy.  
- Trust concerns → Catfriend1’s guarded endorsement and key handover make some uneasy; others lean on reproducible builds and F-Droid verification as objective safeguards.  
- User impact → Syncthing is mission‑critical for many; people want clarity, safer defaults (e.g., local-only discovery), and assurance auto‑updates won’t silently change hands.

---

### LLM perspective
- View: Prefer builds from F-Droid or well-documented repos, and track fingerprints/release notes when ownership changes.  
- Impact: Security-conscious users, Obtainium users, and organizations should review discovery settings and validate new Android maintainer practices.  
- Watch next: F-Droid verification status, any Syncthing core-team statement on recommended Android client, and documented key-management/governance for future handovers.
