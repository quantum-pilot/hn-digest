# OCSP Service Has Reached End of Life

- Score: 97 | [HN](https://news.ycombinator.com/item?id=45242591) | Link: https://letsencrypt.org/2025/08/06/ocsp-service-has-reached-end-of-life

- TL;DR
    - Let’s Encrypt shut down OCSP and now publishes revocations only via CRLs. OCSP URLs were removed from certificates ~90 days ago, so affected certs have expired. Rationale: OCSP leaks browsing activity to CAs and adds operational complexity; LE previously handled 340B monthly OCSP requests via Akamai. HN debates: CRLite and browser-managed revocation lists vs OCSP stapling and short-lived certs; deployability and privacy drive consensus, with Chrome’s CRLSets and Firefox options shaping real-world behavior.

- Comment pulse
    - CRLs are clunky; stapled OCSP could work → Real-time status; Must-Staple mitigates privacy; DNS already leaks domains — counterpoint: stapling isn’t deployable at Web scale.
    - Browsers shifted to central revocation (CRLite/CRLSets) → Works now, no server changes; OCSP failures caused soft-fail; short-lived certs reduce need for revocation.
    - Chrome’s CRLSets ignore enterprise CRLs/OCSP → Periodic Google blacklist means internal CA revocations aren’t checked by default, surprising admins.

- LLM perspective
    - View: Privacy and simplicity justify the move; client-side aggregated revocation (CRLite/CRLSets) is the pragmatic near-term path.
    - Impact: Minimal for mainstream browsers; enterprises and air-gapped networks must ensure CRL distribution and verification policies are correctly configured.
    - Watch next: Browser CRL compression/coverage metrics, CRLite parity across vendors, potential certificate lifetime reductions, and policy shifts on stapling requirements.
