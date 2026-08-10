# A domain can now say it is for sale, in DNS

- Score: 328 | [HN](https://news.ycombinator.com/item?id=49221668) | Link: https://specification.website/spec/foundations/for-sale-dns/

### TL;DR

RFC 10023 defines an IANA-registered `_for-sale` DNS leaf that lets an owner advertise a live domain without parking it. A TXT record carries `v=FORSALE1;` plus one price, contact URI, free-text note, or proprietary code; multiple records can coexist. Records should use short TTLs, disappear when the offer ends, and ideally be DNSSEC-signed. Prices are nonbinding, while text and URIs are untrusted. HN welcomed a machine-readable discovery channel but raised trademark-dispute risks and cautioned that no record means only “not advertised,” not “unavailable.”

### Comment pulse

- The signal fills a discovery gap: privacy-redacted registration data makes welcome purchase inquiries indistinguishable from spam.
- Public sale declarations may complicate trademark disputes; owners should consider legal posture before advertising a domain they actively use.
- Absence means “not advertised here,” not necessarily unavailable; adoption must precede reliable negative inference.

### LLM perspective

- **View:** A reversible DNS convention beats replacing a functioning site with a parking page.
- **Impact:** Brokers gain machine-readable inventory; owners gain visibility without sacrificing traffic or mail.
- **Watch next:** Registrar tooling, broker adoption, DNSSEC validation, abusive records, and dispute-panel treatment.
