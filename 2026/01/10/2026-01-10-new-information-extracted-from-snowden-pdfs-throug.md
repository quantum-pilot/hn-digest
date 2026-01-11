# New information extracted from Snowden PDFs through metadata version analysis

- Score: 264 | [HN](https://news.ycombinator.com/item?id=46564762) | Link: https://libroot.org/posts/going-through-snowden-documents-part-4/

### TL;DR
A researcher re-examined Snowden PDFs published by The Intercept/ABC and used hidden PDF revision metadata to recover text that had been fully deleted, not merely black-box redacted. The resurrected sections describe two domestic National Reconnaissance Office Mission Ground Stations—Potomac (at the Naval Research Laboratory in DC) and Consolidated Denver (at Buckley Space Force Base)—and detail how their public “cover” names are classified versus unclassified. The pattern: detailed US-facility descriptions were stripped, while equivalent foreign ones (Menwith Hill, Pine Gap) were left intact, prompting debate over editorial choices and document sanitization practices.

---

### Comment pulse
- Hidden revisions are an OSINT goldmine → incremental-update PDFs preserve earlier versions; truncating at successive “%%EOF” markers can expose prior, supposedly removed content.  
- Protecting secrets in PDFs is hard → people suggest printing/scanning or image-only workflows, but printer yellow-dot codes and tracking watermarks can still deanonymize leakers.  
- Desire for better tooling → qpdf/QDF and malware-analysis toolchains help inspect structure and revisions, but commenters want higher-level GUIs for forensic PDF introspection.  
- Editorial trust questions → some see journalists’ extra redactions of US facilities as self-censorship or government pressure—counterpoint: media often apply independent harm-minimization standards.

---

### LLM perspective
- View: PDF version metadata is now clearly part of the public OSINT toolkit; publishers must treat it like any other leak surface.  
- Impact: Newsrooms, NGOs, courts, and whistleblowers need stricter, testable redaction pipelines that destroy prior revisions and metadata.  
- Watch next: Expect open-source tools that diff PDF revisions, flag residual content, and auto-convert sensitive releases to verified “dumb image” formats.
