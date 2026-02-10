# AT&T, Verizon blocking release of Salt Typhoon security assessment reports

- Score: 262 | [HN](https://news.ycombinator.com/item?id=46945497) | Link: https://www.reuters.com/business/media-telecom/senator-says-att-verizon-blocking-release-salt-typhoon-security-assessment-2026-02-03/

### TL;DR
Senator Maria Cantwell says AT&T and Verizon are blocking Congress from seeing Mandiant’s security assessment of “Salt Typhoon,” an alleged large-scale Chinese espionage campaign against U.S. telecom networks. She wants their CEOs questioned publicly on why Americans should trust their networks, given FBI claims that hackers used lawful-intercept capabilities to geolocate millions, track movements, and record calls, including of officials. HN commenters emphasize that government‑mandated interception backdoors and chronically weak telco security made such abuse almost inevitable.

---

### Comment pulse
- Lawful-intercept backdoors are structurally dangerous → LI consoles are designed to bypass operators and logs, so a compromise yields invisible, pinpoint wiretaps—counterpoint: some ops staff can still infer LI paths.
- CALEA and similar laws backfired → government required intercept capability, then is shocked when nation-states weaponize it; critics say remove mandated backdoors rather than add new rules.
- Telcos are soft targets → anecdotes of whole networks owned via trivial issues (e.g., exposed Jenkins), and black-box LI appliances shielded from audits, suggest systemic underinvestment in security.

---

### LLM perspective
- View: Mandated interception plus poor operational security created a high-value, low-visibility control plane attackers predictably targeted.
- Impact: Telcos, interception vendors, and regulators face pressure for deeper audits, mandatory disclosure, and redesign of LI architectures.
- Watch next: Congressional hearings, technical postmortems of LI systems, and any moves to revise or roll back CALEA-style requirements.
