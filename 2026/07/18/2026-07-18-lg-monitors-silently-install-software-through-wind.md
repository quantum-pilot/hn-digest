# LG monitors silently install software through Windows Update without consent

- Score: 968 | [HN](https://news.ycombinator.com/item?id=48956688) | Link: https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent

### TL;DR
LG is using Windows Update’s device-metadata mechanism so that when certain LG monitors are plugged in, Windows silently downloads and installs LG’s “utility” software as a signed driver package, with no prompts, sandboxing, or easy opt‑out. Commenters argue this effectively turns Windows into an involuntary software-distribution channel for vendors, likening it to malware and citing similar behavior from Razer and printer makers. Workarounds require obscure group policies, leaving typical users exposed and raising calls for Microsoft to tighten policy and enforcement.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Windows auto-installs vendor “apps” with drivers, a long-standing behavior used by Razer, printers, etc. → systemic Microsoft design issue — counterpoint: LG still abused that trust.

- Mitigations: group policy and Device Installation Settings can block manufacturer apps, but are hidden, complex, and often bypassed by cached drivers.

- Some argue only Microsoft can fix this by revoking abusers’ Windows Update privileges; others note enterprises often bypass Windows Update and won’t feel pressure.

---

### LLM perspective
- View: Treat “driver+app bundles” as a security boundary; require explicit consent for any executable beyond minimal driver code.

- Impact: Hardware vendors lose a dark-pattern distribution channel; Windows users regain control but may see rougher plug‑and‑play experiences.

- Watch next: Audits of other vendors’ driver packages; Microsoft policy changes around device metadata; security research on spoofed USB identities.
