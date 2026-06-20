# Many Let's Encrypt renewals had errors today

- Score: 156 | [HN](https://news.ycombinator.com/item?id=48594715) | Link: https://letsencrypt.status.io/#2026

### TL;DR
Let’s Encrypt had a short API incident where traffic between datacenters was disrupted, causing increased 400/500 errors and “degraded performance” but not a full outage. Staff say it lasted roughly 90 minutes and most issuance still succeeded, but multiple users report repeated renewal failures throughout the day, criticizing the status page wording as minimizing impact. Discussion widens to certificate-expiry UX, the push for ever-shorter certificate lifetimes, operational best practices for renewals, and whether viable, similarly free ACME-based alternatives to Let’s Encrypt exist.

---

### Comment pulse
- Scope of incident → LE says ~90 minutes of partial failures; several admins report 0% success for many attempts, questioning “degraded performance” wording and asking for concrete success-rate metrics.  
- Expired certs and UX → Some want softer warnings for just-expired certs; others argue strict blocking plus pre-expiry alerts is essential to expose broken renewal processes.  
- Ecosystem / alternatives → ZeroSSL, Google Trust Services, SSL.com cited; others worry about CA centralization, suggest DNS-published keys or regional public CAs—counterpoint: replacing Web PKI is extremely hard.

---

### LLM perspective
- View: Incidents like this stress why clients must retry, randomize renewal times, and avoid running certs close to expiry.  
- Impact: Sysadmins and IoT vendors need monitoring on expiry windows, not just “did ACME run today,” plus clearer mapping from ACME errors to alerts.  
- Watch next: More multi-CA ACME support, government-backed free CAs, and status pages that publish real-time success-rate graphs to reduce confusion.
