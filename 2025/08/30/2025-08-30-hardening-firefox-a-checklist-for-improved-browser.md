# Hardening Firefox – a checklist for improved browser privacy

- Score: 267 | [HN](https://news.ycombinator.com/item?id=45073746) | Link: https://andrewmarder.net/firefox/

- TL;DR
  - A concise Firefox hardening guide: switch to a private search engine, enable HTTPS‑Only, disable telemetry, set Enhanced Tracking Protection to Strict; add uBlock Origin, ClearURLs, Privacy Badger; consider first‑party isolation but skip resistFingerprinting if it breaks sites. HN discussion questions the limits of such tweaks amid Firefox’s background connections and shifting defaults, warns anti‑fingerprinting can backfire, and notes Tor best reduces tracking but harms site compatibility. Broader trust concerns surface around defaults like Cloudflare DoH.

- Comment pulse
  - Prefer a host firewall → Firefox makes unsolicited connections; per-process/domain blocking exposes and controls them — counterpoint: RFP covers some; disabling APIs can increase uniqueness.
  - Hard to avoid fingerprinting → Tests show browsers remain identifiable; Tor reduces linkage but breaks payments and triggers fraud checks.
  - Hardening erodes over time → Defaults and policies change; past example cited: silent switch to Cloudflare DoH, undermining trust.

- LLM perspective
  - View: Treat privacy as defense-in-depth: browser settings + extension hygiene + network enforcement + periodic audits.
  - Impact: Improves tracker blocking and data minimization; won’t defeat determined fingerprinting or account-level tracking tied to logins and payments.
  - Watch next: Test connections with Little Snitch/Wireshark; compare against arkenfox; review DoH/ML defaults; evaluate NextDNS/Pi‑hole; measure fingerprint changes, not just point scores.
