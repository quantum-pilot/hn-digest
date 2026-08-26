# New information extracted from Snowden PDFs through metadata version analysis

- Score: 264 | [HN](https://news.ycombinator.com/item?id=46564762) | Link: https://libroot.org/posts/going-through-snowden-documents-part-4/

### TL;DR

Analysis of two published Snowden documents found older PDF revisions retaining sections that had been deleted from the visible files. Those sections identify Potomac and Consolidated Denver Mission Ground Stations, connect them to public cover names, and show a pattern: detailed domestic-site entries disappeared while foreign-site descriptions remained. Timestamps place two Pine Gap revisions minutes apart before publication, and identical files went to The Intercept and ABC. Commenters focused on incremental PDF saves, robust sanitization, inspection tooling, and unresolved reasons for editorial removal.

### Comment pulse

- Revision mechanics → Incremental PDF updates append changes, allowing earlier bodies to survive and sometimes be recovered near EOF markers.
- Sanitization tradeoffs → Rasterizing pages may remove revision history — counterpoint: printer identifiers, accessibility loss, and hidden watermarks create new risks.
- Better inspection needed → qpdf and reverse-engineering toolkits exist, but commenters wanted approachable interfaces and publisher explanations.

### LLM perspective

- View: Document release security requires forensic validation of the entire container, not confidence in its visible rendering.
- Impact: Publishers handling sensitive archives need reproducible flattening, metadata scrubbing, and accessibility checks before distribution.
- Watch next: Independent extraction results, Ryan Gallagher’s response, and broader audits of versioned Snowden PDFs.
