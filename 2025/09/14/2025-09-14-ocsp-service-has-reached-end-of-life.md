# OCSP Service Has Reached End of Life

- Score: 97 | [HN](https://news.ycombinator.com/item?id=45242591) | Link: https://letsencrypt.org/2025/08/06/ocsp-service-has-reached-end-of-life

### TL;DR

Let’s Encrypt shut down OCSP after allowing every certificate containing its responder URL to expire, and will publish revocations only through certificate revocation lists. It cites privacy—OCSP reveals a visitor’s IP and requested site to the certificate authority—and operational simplification. The retired system once handled about 340 billion monthly requests. HN agreed OCSP had deployment and fail-open problems but debated whether CRLs are an elegant replacement, noting stale or large lists, browser-specific distribution systems, and OCSP stapling’s weak adoption.

### Comment pulse

- CRLs avoid per-visit disclosure → their size and update latency require compressed or centrally distributed browser mechanisms.
- Mandatory stapling could preserve OCSP privacy and freshness → counterpoint: server adoption is too low for enforcement without widespread breakage.
- Short-lived certificates reduce revocation pressure → very short lifetimes increase issuance, validation, transparency-log, and outage costs.

### LLM perspective

- View: Let’s Encrypt chose deployable privacy and operational simplicity over OCSP’s theoretically fresher status checks.
- Impact: Clients must depend on CRLs or browser-managed revocation data rather than Let’s Encrypt responders.
- Watch next: CRL propagation latency, browser coverage, enterprise-CA behavior, and certificate-lifetime reductions.
