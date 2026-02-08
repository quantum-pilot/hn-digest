# When internal hostnames are leaked to the clown

- Score: 448 | [HN](https://news.ycombinator.com/item?id=46895972) | Link: https://rachelbythebay.com/w/2026/02/03/badnas/

- TL;DR  
  An owner of a consumer NAS used an internal hostname with a wildcard TLS cert and a hosts-file entry. They later observed Google Cloud machines connecting to that supposedly private hostname via SNI. Root cause: the NAS’s web UI embeds Sentry, whose client-side error reporting sent the page hostname to sentry.io, which then probed it. HN focuses on hostname privacy, involuntary data exposure via third-party telemetry, and mitigations like adblocking, custom firmware, and reverse proxies.

- Comment pulse  
  - Leak isn’t from certificate transparency; Sentry’s browser traces include the NAS hostname, which Sentry’s backend then connects to—raising abuse potential as an indirect port scanner.  
  - Some argue hostnames aren’t private anyway; secrets should live in HTTPS paths, not DNS-visible names — counterpoint: paths also leak to whoever receives telemetry.  
  - Defenses suggested: run open-source NAS firmware, block Sentry and trackers via uBlock/AdGuard, or front devices with Nginx adding strict CSP and referrer policies.

- LLM perspective  
  - View: External telemetry in consumer appliances effectively expands your attack surface to every analytics provider they embed, often without disclosure.  
  - Impact: Vendors should treat hostnames and URLs as sensitive PII in error reports, with opt-out-by-default collection and strict redaction on servers.  
  - Watch next: Worth probing: can Sentry or similar services be coerced into high-volume scans of restricted IP ranges, triggering automated abuse defenses.
