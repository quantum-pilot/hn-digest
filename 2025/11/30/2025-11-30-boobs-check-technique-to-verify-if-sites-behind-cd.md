# "Boobs check" – Technique to verify if sites behind CDN are hosted in Iran

- Score: 155 | [HN](https://news.ycombinator.com/item?id=46100323) | Link: https://twitter.com/hkashfi/status/1995109785679573167

### TL;DR

A short self-post proposes requesting a blocked-looking image path through a site’s CDN; a 403 response containing a 10.10.34.x address allegedly indicates that the origin is inside Iran and subject to local censorship filtering. The source says it works “most of the time” but supplies no test set or confirmed examples. Discussion narrows the mechanism: it depends on the backend or upstream network seeing the URL path, such as plaintext CDN-to-origin HTTP or locally terminated TLS, so proper origin TLS can defeat it.

### Comment pulse

- TLS protects the client-to-CDN path, not necessarily the CDN-to-origin hop → flexible proxy configurations can expose requested paths upstream.
- Commenters proposed compliance, propaganda screening, and avoiding business ties as motives, but the source states no intended use.
- Requests for reproducible sample sites received no confirmed example in the supplied discussion.

### LLM perspective

- View: This is a heuristic for one filtering artifact, not reliable proof of physical hosting location.
- Impact: Investigators could misclassify sites when CDN routing, origin encryption, or error-page behavior differs.
- Watch next: Validation needs controlled Iranian and non-Iranian origins, repeated routes, and documented false-positive rates.
