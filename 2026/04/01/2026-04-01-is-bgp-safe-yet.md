# Is BGP safe yet?

- Score: 234 | [HN](https://news.ycombinator.com/item?id=47600382) | Link: https://isbgpsafeyet.com/

### TL;DR

Cloudflare’s tracker still answers no: BGP accepts route announcements without built-in authentication, allowing mistakes or hijacks to redirect or black-hole traffic. Resource Public Key Infrastructure lets networks cryptographically validate whether an autonomous system may originate a prefix, and many major transit providers now sign routes and reject invalid announcements; Sparkle joined them in February 2026. Coverage remains incomplete, and HN emphasized a deeper limitation: origin validation does not authenticate the full AS path. Commenters cited 254 listed unsafe operators and called for tracking newer path-validation efforts such as ASPA.

### Comment pulse

- BGPSec is widely considered undeployable; alternatives discussed include ASPA and proof-carrying data, both still anchored in RPKI.
- The collapsed major-operator view looks encouraging — counterpoint: the expanded table includes many unsafe networks, regional gaps, and inconsistent provider subsidiaries.
- Readers want ASPA-invalid testing because route leaks and path manipulation can occur beyond the origin that current site checks validate.

### LLM perspective

- **View:** Routing security is a deployment gradient; a binary headline usefully motivates action but overstates what origin validation guarantees.
- **Impact:** Transit filtering contains bad announcements, while unprotected edge and regional networks preserve pathways for disruption.
- **Watch next:** ASPA deployment, path-aware tests, unsafe-operator reductions, inconsistent ASN results, and updates beyond February 2026.
