# Microsoft 365 now tracks you in real time?

- Score: 354 | [HN](https://news.ycombinator.com/item?id=46827003) | Link: https://ztechtalk.com/microsoft-teams

### TL;DR
Microsoft is rolling out a Microsoft 365 / Teams feature that can show coworkers whether you’re in-office and, when on corporate Wi‑Fi, which building you’re in. The article portrays this as real‑time, everywhere tracking that reveals SSIDs like “Starbucks_Guest_WiFi” to your manager, but HN comments (including a Teams engineer) say that’s inaccurate: it’s a calendar/location‑sharing setting plus an upcoming “auto-set office building on corp Wi‑Fi” option. Discussion focuses on privacy, admin-enforced policies, legality, and the article’s AI-generated, clickbait style.

---

### Comment pulse
- Teams insider: feature is calendar-based location sharing (office/remote/building/none), not arbitrary Wi‑Fi SSID exposure—counterpoint: tenant admins can restrict options, effectively forcing tracking.  
- Infra/security folks: IT already sees Wi‑Fi SSID, IP, VPN via endpoint tools; this only surfaces it in Teams status, but still feels invasive.  
- Others: question EU legality and “toxic manager” cultures; also note article reads like low-effort LLM output and misrepresents what Microsoft actually shipped.

---

### LLM perspective
- View: Real risk is admin-enforced, normalized presence tracking, not the sensational “Starbucks GPS” framing.  
- Impact: Hybrid workers, EU-regulated employers, and orgs with low trust will feel this most; good cultures may ignore it.  
- Watch next: Tenant policy defaults, auditability, and whether regulators or large customers push back on granular workplace location features.
