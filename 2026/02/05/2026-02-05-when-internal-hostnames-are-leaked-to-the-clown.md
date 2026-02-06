# When internal hostnames are leaked to the clown

- Score: 425 | [HN](https://news.ycombinator.com/item?id=46895972) | Link: https://rachelbythebay.com/w/2026/02/03/badnas/

### TL;DR
A NAS device’s web UI used Sentry for client-side error logging. Those JavaScript traces included full URLs, so internal hostnames like `nas.internal.example.com` were sent to Sentry. Sentry’s backend then tried to connect back to those hostnames (likely for UI niceties like favicons), but due to wildcard DNS/HTTPS on the vendor’s side, that traffic hit a public “clown” (cloud) host, exposing private naming schemes. HN discussion centers on misunderstanding the cause, how private hostnames really are, and defenses against this kind of telemetry leak.

*Content unavailable; summarizing from title/comments.*

---

### Comment pulse
- Real issue is Sentry client traces → Sentry backend making follow-up HTTP requests to internal hostnames → wildcard DNS routes them to cloud host.  
- Hostnames are inherently leaky via DNS, TLS, logs; keep secrets in HTTPS paths or opaque IDs instead—counterpoint: any URL segment can still reach third parties via telemetry.
- Defenses: block telemetry with uBlock/AdGuard or DNS, front NAS with a reverse proxy adding strict CSP/referrer policies, or replace firmware with trusted, non–phone-home systems.

---

### LLM perspective
- View: Treat all device web UIs as internet-facing; anything rendered in a browser can be exfiltrated by bundled third-party scripts.
- Impact: NAS/IoT vendors must audit telemetry integrations; privacy-conscious users should assume commercial firmware leaks metadata by default.
- Watch next: Better defaults in observability tools (no automatic follow-up requests), stricter CSP templates, and vendor guidance on hostname/URL hygiene.
