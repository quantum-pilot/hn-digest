# ZoomInfo CEO blocks researcher after documenting pre-consent biometric tracking

- Score: 108 | [HN](https://news.ycombinator.com/item?id=46050471) | Link: https://github.com/clark-prog/blackout-public

### TL;DR
A security researcher inspected ZoomInfo’s GTM Studio product page and found extensive tracking and behavioral biometrics firing before any cookie consent: 50+ pre-consent requests, 118 tracking domains, Sardine.ai biometrics (`enableBiometrics: true`), PerimeterX fingerprinting, and session fingerprinting APIs. After posting this under the CEO’s LinkedIn demo, the researcher was quickly blocked and responded by publishing a reproducible “evidence pack” with network traces and legal analysis arguing potential GDPR/CCPA/CIPA exposure. HN discussion splits between alarm over stealth surveillance and shrugs that this is now standard martech practice.

---

### Comment pulse
- This is serious surveillance/compliance risk → pre-consent biometrics plus 100+ trackers could interest DPOs, regulators, and plaintiffs; CEO blocking worsens reputational exposure.  
- This is just how modern web marketing works → nearly every commercial site runs many third-party trackers under “fraud prevention” or “legitimate interest” — counterpoint: biometrics cross a qualitative line.
- Post doubles as an ad for the researcher’s product → some see clever marketing more than pure disclosure; others blame browser design allowing arbitrary third-party JavaScript.

---

### LLM perspective
- View: Pre-consent behavioral biometrics on sales sites suggests privacy-invasive fraud tooling is bleeding into routine marketing without governance.
- Impact: Security, legal, and procurement teams will scrutinize tracking stacks, not just app security, especially for EU-facing vendors.
- Watch next: Whether regulators or class actions start citing such public evidence packs, and whether browsers clamp down on biometric-style telemetry.
