# The RCE that AMD won't fix

- Score: 369 | [HN](https://news.ycombinator.com/item?id=46906947) | Link: https://mrbruh.com/amd/

### TL;DR
A now-removed blog post reportedly showed that an AMD Windows utility/driver updater fetches executables over plain HTTP from an ATI domain, allowing trivial remote code execution via DNS/router/Wi‑Fi man‑in‑the‑middle. AMD allegedly declined to fix it, treating it as out-of-scope. HN discussion focuses on why Linux’s in-repo drivers avoid such fragile updaters, why outbound HTTP from system tools is a major red flag, and how this could force enterprises to blacklist AMD’s updater or even AMD hardware.

---

### Comment pulse
- Linux packaging GPU drivers → avoids third‑party updaters that can’t be sandboxed; distro maintainers prioritize security more than hardware vendors focused on shipping hardware generations.  
- Plain HTTP for auto‑updates → seen as unacceptable; enables MITM binary injection and privacy leaks—counterpoint: signed payloads over HTTP can be as safe as HTTPS if done rigorously.  
- Threat model → single poisoned DNS/Wi‑Fi hop can subvert the updater; enterprises may respond by disabling/banning it despite users’ mitigations like VPNs or manual updates.

---

### LLM perspective
- View: This reflects systemic negligence in update infrastructure design, not an exotic bug; transport security on updaters should be non-negotiable.  
- Impact: Security-conscious organizations will likely require disabling AMD’s updater, favor curated driver distribution, or reassess AMD adoption on managed fleets.  
- Watch next: Whether a CVE is assigned, corporate advisories appear, or OS vendors start blocking non-TLS auto-updaters by policy.
